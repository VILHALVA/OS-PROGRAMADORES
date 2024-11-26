import sys

BASE_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def main():
    if len(sys.argv) < 2:
        print('Você precisa fornecer um arquivo como argumento, utilize o arquivo teste "baseconv.txt"')
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            print(convert_from_base_to_base(line))

def convert_from_base_to_base(element):
    params = element.split()[:3]
    input_base, output_base, input_number = map(int, params[:2]), params[2]
    validation_result = validate_input(input_base, output_base, input_number)

    if validation_result == "valid":
        number_in_decimal = convert_to_decimal(input_base, input_number)
        return convert_decimal_to_base(output_base, number_in_decimal)
    else:
        return validation_result

def validate_input(input_base, output_base, input_number):
    max_base, min_base = 62, 2

    if not (min_base <= input_base <= max_base and min_base <= output_base <= max_base):
        return "???"
    
    if int(input_number) < 0:
        return "???"

    valid_digits_for_input_base = set(BASE_CHARS[:input_base])
    if any(digit not in valid_digits_for_input_base for digit in input_number):
        return "???"

    number_in_decimal = convert_to_decimal(input_base, input_number)
    limit = convert_to_decimal(max_base, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

    if number_in_decimal > limit:
        return "???"

    if number_in_decimal == 0:
        return "0"

    return "valid"

def convert_decimal_to_base(output_base, number_in_decimal):
    result = []
    output_base = int(output_base)
    while number_in_decimal > 0:
        remainder = number_in_decimal % output_base
        result.append(BASE_CHARS[remainder])
        number_in_decimal //= output_base
    return ''.join(reversed(result))

def convert_to_decimal(input_base, input_number):
    number_in_decimal = 0
    exponent = len(input_number) - 1

    for digit in input_number:
        digit_value = BASE_CHARS.index(digit)
        number_in_decimal += digit_value * (input_base ** exponent)
        exponent -= 1

    return number_in_decimal

if __name__ == "__main__":
    main()
