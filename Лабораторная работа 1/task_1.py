numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missed_number_id = 4

# Замена значений пропущенного элемента средним арифметическим
summ_numbers = sum(numbers[:missed_number_id]+numbers[missed_number_id+1:])
count_numbers = (len(numbers[:missed_number_id]+numbers[missed_number_id+1:]) + 1)

numbers[missed_number_id] =  summ_numbers / count_numbers

print("Измененный список:", numbers)
