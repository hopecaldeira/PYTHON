# countdown
def new_num(x):
    list = []
    for new_num in range(x, -1, -1):
        list.append(new_num)
    return list
print(new_num(6))

# print and return
def two(x,y):
    print(x)
    return y
two(3,8)

# first plus length
def first_plus_length(x):
    return x[0] + len(x)
print(first_plus_length([6,7,8,9]))

# values greater than second
def values_greater_than_second(x):
    list = []
    if values_greater_than_second([x] <= 1):
        return False

values_greater_than_second([5,2,3,2,1,4])

# this length that value
def length_and_value(x,y):
    list = []
    len(list) = length_and_value(x)
    list = length_and_value(y) * 1
    return list
length_and_value(3,4)