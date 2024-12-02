# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, sep=','):
    list1 = participants1.split(sep)
    list2 = participants2.split(sep)
    intersection_set = set(list1).intersection(set(list2))
    return sorted(intersection_set)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, sep ="|"))
# TODO Провеьте работу функции с разделителем отличным от запятой

