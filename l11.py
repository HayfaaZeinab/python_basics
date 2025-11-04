#find x sum of all k long subarrays
class Solution(object):
    def findXSum(self, nums, k, x):
        answer=[]
        for i in range(len(nums)-k+1):
            subarray=nums[i:i+k]
            freq={}
            
            for num in subarray:
                #freq[num] = freq.get(num, 0) + 1
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1

            sorted_items=sorted(freq.items(),key=lambda item:(item[1],item[0]),reverse=True)

            #top_x_elements=set([item[0]for item in sorted_items[:x]])
            top_x_list=[]
            for item in sorted_items[:x]:
                top_x_list.append(item[0])
            top_x_elements=set(top_x_list) 


            #x_sum=sum(num for num in subarray if num in top_x_elements)
            x_sum=0
            for num in subarray:
                if num in top_x_elements:
                    x_sum+=num


            answer.append(x_sum)
        return answer


#power of 2
class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0  #binary + aan nadakunne
       
      """while n%2==0:
            n//2
        return n==1"""




        
        
