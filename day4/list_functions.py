days_list = ["day1", "day2", "day3", "day4", "day5"]
days_list.append('day6')
days_list.extend(['day7', 'day8', 'day9'])


# days_list.insert(0, "January")      # insert value at particular position (index, value)
# days_list.remove('day8')    # raise value error if item not found
# days_list.pop()         # remove last element of our list

popped_element = days_list.pop(6)         # pop ith index element from list and return it.
print(popped_element)