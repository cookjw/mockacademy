def uniq(my_list):
    for item in my_list:
        while my_list.count(item) > 1:
            first_index = my_list.index(item)
            second_index = my_list.index(item, first_index+1)
            del my_list[second_index]
    return my_list