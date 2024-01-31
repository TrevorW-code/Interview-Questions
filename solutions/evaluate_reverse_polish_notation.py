class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+','-','*','/']

        for token in tokens:
            if token in operations:
                sec_arg = stack.pop()
                frst_arg = stack.pop()
                answer = int(eval(frst_arg+token+sec_arg))
                stack.append(str(answer))
                print(f'{frst_arg}{token}{sec_arg}={answer}')
            else:
                stack.append(token) # store values to do operations on

        return int(stack[0])