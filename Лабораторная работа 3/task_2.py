def find_common_participants(first_group, second_group, separator=','):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)

    group_intersection = list(set(first_group).intersection(set(second_group)))
    group_intersection.sort()

    return group_intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Общие участники:
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
