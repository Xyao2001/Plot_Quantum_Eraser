class Solution(object):

    
                
    def find_the_shortest_word(self, strs):
        count_total=[]
        min_word=[]
        for i in range(len(strs)):
            count=0
            for j in range(len(strs[i])):
                count+=1
            count_total.append(count)
        print(f"the range of len(count_total is {range(len(count_total))}")
        min_count=count_total[0]
        for z in reversed(range(len(count_total))):
            if count_total[z]<min_count:
                min_count=count_total[z]
       
        for x in range(len(strs)):
            if count_total[x]==min_count:
                min_word.append(strs[x])
            

        print(f"the shortest words are {min_word}, which has a length of {min_count}")
        return min_word
        

lis = ["flower","flow","flight","fly","flaunt","fake","flo","confused","st"]

p = Solution()  #instantiate a class instance here.
p.find_the_shortest_word(lis)
