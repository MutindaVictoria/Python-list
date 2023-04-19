#Given two lists, write a function to 
#remove the common elements between them and return them in a new list.
def common_elements(name1):
    my_list=(set(name1))
    print(my_list)


 #Write a function that takes in a list of numbers and
 # returns a new list containing only the prime numbers.
def prime_numbers(nums):
    primes=[]
    for num in nums:
        if num >1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:primes.append(num)
    return primes
#Write a function that defines a Python list for the days of the week and 
#then use a loop (while or for) to print that list.
def week_Days(days):
    for day in range(len(days)):
    print(days[i])      



#Write a function that takes in two lists of integers and 
#returns a new list containing the common elements in both lists, but with their order reversed.
def reverse_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2)) 
    reversed_common_elements = common_elements[::-1] 
    return reversed_common_elements


    #Write a function that takes in a list of integers and 
    #returns the length of the longest increasing subsequence of the list.
def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n # initialize the dynamic programming array to 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)