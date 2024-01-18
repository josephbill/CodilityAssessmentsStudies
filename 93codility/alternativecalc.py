def calculate_alternative_notation(expression):
    tokens = expression.split()

    stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # If the token is a number, push it onto the stack
            stack.append(float(token))
        elif token in operators:
            # If the token is an operator, pop operands from the stack and perform the operation
            num_operands = len(token)
            operands = [stack.pop() for _ in range(num_operands)]
            result = operators[token](*operands[::-1])  # Reverse the order for correct operation
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid expression: Stack should have exactly one result.")

    return stack[0]  # The final result should be the only element left on the stack


# Test cases
expression_1 = "+ 3 4"
expression_2 = "- 3 * 4 5"
expression_3 = "* + 3 4 5"
expression_4 = "/ - 3 4 + 5 2"

result_1 = calculate_alternative_notation(expression_1)
result_2 = calculate_alternative_notation(expression_2)
result_3 = calculate_alternative_notation(expression_3)
result_4 = calculate_alternative_notation(expression_4)

print(f"Result 1: {result_1}")
print(f"Result 2: {result_2}")
print(f"Result 3: {result_3}")
print(f"Result 4: {result_4}")
