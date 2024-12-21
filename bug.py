def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0  # Or raise an exception: raise ValueError("List cannot be empty")
    total = sum(numbers)
    average = total / len(numbers) 
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will return 0