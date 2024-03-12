# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

def plusMinus(arr):
    size_of_array = len(arr)
    more_than_zero = 0
    less_than_zero = 0
    equal_zero = 0

    for i in arr:
        if i > 0:
            more_than_zero += 1
        if i < 0:
            less_than_zero += 1
        if i == 0:
            equal_zero += 1

    ratios_positive = more_than_zero / size_of_array
    ratios_positive_formatted = f'{ratios_positive:.6f}'
    ratios_negative = less_than_zero / size_of_array
    ratios_negative_formatted = f'{ratios_negative:.6f}'
    ratios_zero = equal_zero / size_of_array
    ratios_zero_formatted = f'{ratios_zero:.6f}'

    print(ratios_positive_formatted)
    print(ratios_negative_formatted)
    print(ratios_zero_formatted)
