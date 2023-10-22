users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict_ = {
    "Общее количество": '',
     "Уникальные посещения": ''
}

dict_["Общее количество"] = len(users)
dict_["Уникальные посещения"] = len(set(users))

print(dict_)
