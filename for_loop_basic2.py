# Biggie Size
# def biggieSize(list):
#     for x in range(0,len(list)):
#         if list[x] > 0:
#             list[x]="big"
#     print(list)

# biggieSize([-1,3,5,-5])



# # Count Positives
# def countPositives(list):
#     count = 0;
#     for x in range(0, len(list)):
#        if list[x] > 0:
#            count +=1
#     list[x]=count
#     print(list)
#     return(list)    
    
# countPositives([-1,1,1,1,1])
# countPositives([1,6,-4,-2,-7,-2])



# # Sum Total
# def sumTotal(list):
#     sum = 0;
#     for x in range(0,len(list)):
#         sum+=list[x]
#     print(sum)

# sumTotal([1,2,3,4])
# sumTotal([6,3,-2])



# # Average
# def average(list):
#     sum = 0;
#     for x in range(0,len(list)):
#         sum+=list[x]    
#     print(sum/len(list))
#     return(sum/len(list))

# average([1,2,3,4])



# # Length
# def length(list):
#     print(len(list))  
    
# length([1,2,3,4,5,6,7,8,9])
# length([])



# # Minimum
# def minimum(list):
#     min = 0
#     for x in range(0,len(list)):
#         if list[x] < min:
#             min = list[x]
#     print(min)

# minimum([37,2,1,-9,5])



# Maximum
# def maximum(list):
#     max = 0
#     for x in range(0,len(list)):
#         if list[x] > max:
#             max = list[x]
#     print(max)

# maximum([37,2,1,-9,5])



# # Ultimate Analysis
# def ultimateAnalysis(list):
#     min = 0
#     max = 0
#     sum = 0
#     for x in range(0,len(list)):
#         if list[x] < min:
#             min = list[x]
#         if list[x] > max:    
#             max = list[x]
#         sum+=list[x] 
#     print({
#         'sumTotal': sum,
#         'average': sum/len(list),
#         'minimum': min,
#         'maximum': max,
#         'length': len(list)
#     })

# ultimateAnalysis([37,2,1,-9])