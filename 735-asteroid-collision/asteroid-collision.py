class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        breaked=False
        for i in asteroids:
            if(i<0):
                breaked=False
                while(stack):
                    poped_value=stack.pop()
                    if(poped_value<0):
                        stack.append(poped_value)
                        stack.append(i)
                        breaked=True
                        break
                    if(poped_value>0 and poped_value>abs(i)):
                        stack.append(poped_value)
                        breaked=True
                        break
                    elif(poped_value>0 and poped_value==abs(i)):
                        breaked=True
                        break
                    else:
                        pass
                if(len(stack)==0 and not breaked):
                    stack.append(i)
            else:
                stack.append(i)
        return stack
                    


                    

