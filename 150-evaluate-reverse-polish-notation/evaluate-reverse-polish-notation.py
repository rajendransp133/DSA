class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        ops = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": lambda a, b: int(a / b) }

        stack=[]
        for i in tokens:
            if(i=="+" or i=="-" or i=="*" or i=="/"):
                right=stack.pop()
                left=stack.pop()
                stack.append(ops[i](left, right))
            else:
                stack.append(int(i))

        return stack[-1]
        