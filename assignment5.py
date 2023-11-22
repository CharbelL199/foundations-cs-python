#Sorting Strings
def sort_strings_alphabetically(strings):
    n = len(strings)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if strings[j].lower() > strings[j+1].lower():
                return strings

input_strings = ["aA", "b", "BD", "Bc", "D"]
output_strings = sort_strings_alphabetically(input_strings)

print(output_strings)

#Sorting numbers descending 
def sort_numbers_descending(numbers):
    n = len(numbers)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
                return numbers

input_numbers = [3, 5, 1, 8, -10]
output_numbers = sort_numbers_descending(input_numbers)

print(output_numbers)