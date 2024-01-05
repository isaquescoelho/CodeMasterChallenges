# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    minimum_number = min(arr)
    maximum_number = max(arr)

    maximum_sum = sum(arr) - minimum_number
    minimum_sum = sum(arr) - maximum_number

    print(f'{minimum_sum} {maximum_sum}')
