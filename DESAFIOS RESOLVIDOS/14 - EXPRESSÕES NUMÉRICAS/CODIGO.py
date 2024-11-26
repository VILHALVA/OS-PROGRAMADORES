import sys
import re

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read().split("\n")
            expressions = [expression.replace(" ", "") for expression in data if expression]
            return expressions
    except Exception as err:
        print(f"Erro ao ler o arquivo: {err}")
        sys.exit(1)

def is_valid_expression(expression):
    stack = []
    operators = ["+", "-", "*", "/", "^"]

    for i, char in enumerate(expression):
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()

        if i + 1 < len(expression):
            if char in operators and expression[i + 1] in operators:
                return False

    return not stack

def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    result = []
    stack = []

    for token in expression:
        if token.isdigit():
            result.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop() 
        else:
            while stack and stack[-1] != "(" and precedence[token] <= precedence[stack[-1]]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return result

def solve_postfix_expression(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2:
                return "ERR SYNTAX"
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
                stack.append(operand0 // operand1)
            elif token == "^":
                stack.append(operand0 ** operand1)

    if len(stack) != 1:
        return "ERR SYNTAX"

    return stack.pop()

def main():
    if len(sys.argv) < 2:
        print("Erro de Sintaxe: python CODIGO.py")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_file(file_name)

    for expression in data:
        if not is_valid_expression(expression):
            print("ERR SYNTAX")
            continue

        tokens = list(filter(None, re.split(r'([()+\-/*^])', expression)))
        postfix = infix_to_postfix(tokens)
        result = solve_postfix_expression(postfix)
        print(result)

if __name__ == "__main__":
    main()
