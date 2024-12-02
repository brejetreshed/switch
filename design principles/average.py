def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """

    sum_of_numbers = sum(numbers)
    
    for index in range(len(numbers)):
        if not isinstance(numbers[index], (int, float)):
            raise TypeError(f"Element at index {index} is not a number")
    

    average = sum_of_numbers / len(numbers)
    return round(average, 2)


# Usage
try:
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"The average is: {result}")
except (TypeError, ValueError) as e:
    print(f"Error: {str(e)}")