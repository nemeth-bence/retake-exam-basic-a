# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases

def min_max_diff(numbers):
    difference = []
    try:
        for number in range(len(numbers)):
            if max(numbers) - min(numbers) == number:
                difference.append(number)
        return sum(difference)
    except ZeroDivisionError:
        return None

min_max_diff([4,7,3,2,9])
