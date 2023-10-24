def find_common_participants(group_1, group_2, key=','):
    common = list(set(group_1.split(key)).intersection(set(group_2.split(key))))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники: ", find_common_participants(participants_first_group, participants_second_group, '|'))
