"""
a = [19,2,31,45,6,11,121,27]
print(a)
for i in range(len(a)-1,0,-1):
    #print('i ',i, ' ',a[i])
    for j in range(i):
         print(a[j], ' next ',a[j+1])
         if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        print('ul ',len(unsorted_list))
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    #print('m ',middle)
    left_list = unsorted_list[:middle]
    #right_list = unsorted_list[middle:]
    print('llb ',left_list)
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    print('llafter ',left_list)
    #return list(merge(left_list, right_list))


a = [23,4,12,567,34,56,678,78,112,3,54]
a = [34,5,12,3]
print(a)
merge_sort(a)


def permute(list, s):
    if list == 1:
        return s
    else:
        return [ print("YX: ",y, x)
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]

print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)
for n in range(10):
    #print(n)
    f = fibonacci(n)
    print(f)

def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i

r = twoSum([1,2,4,4], 8)
print(r)
#[1,2,4,4] target - 8
def two_sum(series, target):
    seen = {}
    if len(series) <= 1:
        return False
    for i in range(len(series)):
        if series[i] in seen:
            return(seen[series[i]], i)
        seen[target - series[i]] = i

s = two_sum([4,-2,4,9], 7)
print(s)

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
def add_two_numbers(a,b):
    carry = 0
    answer = []
    for i in range(len(a)):
        add_num = a[i] + b[i]
        if (add_num % 10) == 0:
            answer.append(1)
            continue
        elif (add_num % 10) > 0:
            answer.append(add_num % 10)
            carry = add_num % 10

"""

"""
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
"""
routes = [[1, 2, 7], [3, 6, 7], [23, 4], [67,7]]
start = None
r_sort = {}
s = 1
t = 67
points = 0


for i,j in enumerate(routes):
    if s in j or t in j:
        points = points + 1
        if t in j:
            points = points + 1
            break

print(points)

"""
for i in routes:
    for j in i:
        if j == s:
            points = points + 1
        print(j)
    #r_sort[i] = sorted(i)
print(r_sort)
"""









