class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if(i>0):
                stack.append(i)
            else:
                breaked=False
                while(stack):
                    peak_value=stack[-1]
                    if(peak_value<0):
                        stack.append(i)
                        breaked=True
                        break
                    if(peak_value>0 and peak_value>abs(i)):
                        breaked=True
                        break
                    elif(peak_value>0 and peak_value==abs(i)):
                        stack.pop()
                        breaked=True
                        break
                    else:
                        stack.pop()
                if(len(stack)==0 and not breaked):
                    stack.append(i)
        return stack
                    


                    

