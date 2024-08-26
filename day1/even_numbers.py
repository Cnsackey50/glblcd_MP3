def is_even(numbers):
    return numbers % 2==0
values = [1,56,234,87,4,76,24,69,90,135]
Filter =[]
for number in values:
    if is_even(number):
         
         Filter.append(number)
print(Filter)

even_numbers = list(filter(lambda numbers: numbers % 2 ==0, values))
print(even_numbers)

odd_numbers = list(filter(lambda numbers: numbers % 2 !=0, values))
print(odd_numbers)

filtered_odd_numbers = [number for number in values if not is_even(number)]
print(filtered_odd_numbers)

