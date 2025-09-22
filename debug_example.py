def calculate_sum(numbers):
    total = 0
    
    for i in range(0, len(numbers)):
        total += numbers[i] 
    return total

my_list = [10, 20, 30]
result = calculate_sum(my_list)
print(f"Сумма списка {my_list} равна {result}")