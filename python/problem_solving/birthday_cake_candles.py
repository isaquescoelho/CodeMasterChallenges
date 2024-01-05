# You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
# Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    maximum_number = max(candles)
    amount_tallest_candles = candles.count(maximum_number)

    return amount_tallest_candles
