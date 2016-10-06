#Professor Li. I keep getting an error and I don't know why or how I can fix the error. TypeError: slice indices must be integers or None or have an __index__ method


def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    while x in my_list:
        my_list = my_list[0:((len(my_list)-1)/2)]
        x in my_list 
    while x in my_list:
        my_list = my_list[((len(my_list)-1)/2):]
        x in my_list 
    pass

test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None
