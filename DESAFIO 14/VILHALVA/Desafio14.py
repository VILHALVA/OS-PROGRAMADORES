import sys

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read().split("\n")
            expressions = []

            for expression in data:
                if expression != "":
                    expression = expression.replace(" ", "")
                    expressions.append(expression)

            return expressions
    except Exception as err:
        print(err, "Read Failed")
        return err

def is_valid_expression(expression):
    have_parentheses = "(" in expression

    if have_parentheses:
        expression = list(expression)

        amount_opening_parentheses = expression.count("(")
        amount_closing_parentheses = expression.count(")")

        if amount_opening_parentheses != amount_closing_parentheses:
            return False

    operators = ["+", "-", "*", "/", "^"]

    for i in range(len(expression)):
        current_char = expression[i]

        if i + 1 < len(expression):
            next_char = expression[i + 1]

            if current_char in operators and next_char in operators:
                return False

    return True

def infix_to_postfix(expression):
    precedence = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2
    }

    result = []
    stack = []

    for token in expression:
        is_number = token.isdigit()

        if is_number:
            result.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                last_operator = stack.pop()
                result.append(last_operator)

            stack.pop()
        else:
            while stack and precedence[token] <= precedence[stack[-1]]:
                last_operator = stack.pop()
                result.append(last_operator)

            stack.append(token)

    while stack:
        result.append(stack.pop())

    return result

def solve_postfix_expression(expression):
    stack = []

    for token in expression:
        is_number = token.isdigit()

        if is_number:
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand0 = stack.pop()

            if token == "+":
                stack.append(operand0 + operand1)
            elif token == "-":
                stack.append(operand0 - operand1)
            elif token == "*":
                stack.append(operand0 * operand1)
            elif token == "/":
                if operand1 == 0:
                    return "ERR DIVBYZERO"
                stack.append(operand0 / operand1)
            elif token == "^":
                stack.append(operand0 ** operand1)

    result = stack.pop()

    return result

def main():
    if len(sys.argv) < 2:
        print("Erro de Sintaxe: python nome_do_programa.py nome_do_arquivo")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_file(file_name)

    for expression in data:
        is_valid = is_valid_expression(expression)

        if not is_valid:
            print("ERR SYNTAX")
            continue

        expression = list(filter(None, re.split(r'([()+\-/*^])', expression)))

        postfix = infix_to_postfix(expression)

        result = solve_postfix_expression(postfix)

        print(result)

if __name__ == "__main__":
    main()
