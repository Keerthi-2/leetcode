class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        num = 0

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in {'+', '-', '*', '/'}:
                num_stack.append(num)
                num = 0
                while op_stack and self.precedence(op_stack[-1]) >= self.precedence(char):
                    self.apply_operator(num_stack, op_stack)
                op_stack.append(char)

        num_stack.append(num)

        while op_stack:
            self.apply_operator(num_stack, op_stack)

        return num_stack[0]

    def precedence(self, op: str) -> int:
        if op in {'+', '-'}:
            return 1
        if op in {'*', '/'}:
            return 2
        return 0

    def apply_operator(self, num_stack, op_stack):
        if len(num_stack) < 2 or len(op_stack) < 1:
            raise ValueError("Invalid expression")

        num2 = num_stack.pop()
        num1 = num_stack.pop()
        operator = op_stack.pop()

        if operator == '+':
            num_stack.append(num1 + num2)
        elif operator == '-':
            num_stack.append(num1 - num2)
        elif operator == '*':
            num_stack.append(num1 * num2)
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Division by zero")
            num_stack.append(int(num1 / num2))

        