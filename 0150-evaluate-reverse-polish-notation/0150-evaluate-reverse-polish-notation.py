class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "-":
                x,y=stack.pop(),stack.pop()
                stack.append(y-x)
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "/":
                x,y=stack.pop(),stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(i))
        return stack[0]