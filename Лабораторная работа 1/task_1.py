numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missed_number_id = 4

# Замена значений пропущенного элемента средним арифметическим
numbers_uniq = numbers[:missed_number_id]+numbers[missed_number_id+1:]
numbers[missed_number_id] = sum(numbers_uniq) / (len(numbers_uniq) + 1)

print("Измененный список:", numbers)
