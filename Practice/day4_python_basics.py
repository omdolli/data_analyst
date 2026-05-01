#
# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     print(num)

#sum list
# nnumbers = [1,2,3,4,5]
# total = 0
# for num in nnumbers:
#     total += num
# print(total)

# larget number
# nnnumbers = [1,2,3,4,5,6]
# largest = nnnumbers[0]
# for num in nnnumbers:
#     if num>largest:
#         largest = num
# print(largest)

# even number
# nums = [1,2,3,4,5,6,7,8,9,0]
# count = 0
# for num in nums:
#     if num % 2==0:
#         count += 1
# print(count)

# remove duplicate
# numbers = [1,2,3,4,5,2,3,6]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# second largest number
# numberss = [1,2,3,4,5,6]

# largest = numberss[0]
# second_largest = numberss[0]
# for num in numberss:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
# print(second_largest)

# reverse number
numbers = [1,2,3,4,5,6,7,8]
reverse= []
for num in numbers:
    reverse.insert(0,num)
print(reverse)
