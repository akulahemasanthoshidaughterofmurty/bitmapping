class Solution:
	def setBits(self, N):
		# code here
        count=0
        while(N!=0): #loop iterates until it becomes 0
            if(N & 1==1): #checking weather the bit is set or not by doing and opearion with 1
                count+=1
            N=N>>1 #to check the next bit we right shifting the number
        return count #returning the count
