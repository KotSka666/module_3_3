def print_params(a=1, b="строка", c= True):
    print(a, b, c)


print_params(5, 'String', False)
print_params('Run', False)
print_params('String')
print('---------------------------------------')

values_list = [4, 9.1, 'low']
values_dict = {'a': 2, 'b': 'Спелое', 'c': False}

print_params()
print_params(*values_list)
print_params(values_list, 3)
print_params('a' ,values_list, 3.14)
print_params(**values_dict)
print_params(10, values_dict, 'None')
print('---------------------------------------')

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)