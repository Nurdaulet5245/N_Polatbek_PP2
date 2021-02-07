def numIdenticalPairs(nums: []) -> int:
    pairs = 0
    for i in range(len(nums) - 1):
      for j in range(len(nums) - i - 1):
        if (nums[i] == nums[j + 1 + i] and i < j + 1 + i):
          pairs += 1
    print(pairs)

n=int(input())
l = []
for i in range(0, n):
  el=int(input())
  l.append(el)

numIdenticalPairs(l)

# lst = [] 
  

# n = int(input("Enter number of elements : ")) 
  
# for i in range(0, n): 
#     ele = int(input()) 
  
#     lst.append(ele)  
      
# print(lst)