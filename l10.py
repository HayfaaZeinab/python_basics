#minimum time to make rope colourful

class Solution(object):
    def minCost(self, colors, neededTime):
        total=0
        maxtime=neededTime[0]

        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                total+=min(maxtime,neededTime[i])
                maxtime=max(maxtime,neededTime[i])
            else:
                maxtime=neededTime[i]

            

        return total

#find the value of variable after performing operations
class Solution(object):
    def finalValueAfterOperations(self, operations):
        count=0
        for i in operations:
            if (i=="++X") or (i=="X++"):
                count+=1
            elif i=="--X" or i=="X--":
                count-=1
        return count
