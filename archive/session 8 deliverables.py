#Exercise 1
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    # print(letter + suffix)

# Exercise 2
def count(word,letter):
    counter = 0
    for letter in word:
        counter += 1 
    return counter

# print(count('testttttt','t'))

# Exercise 4
food =['bananas','rice','paprika','potato chips']
costs = []
for i in food:
    itemcost = 0
    if i == 'a':
        itemcost = itemcost + 1
        costs.append(itemcost)
    elif i == 'b':
        itemcost = itemcost + 2
        costs.append(itemcost)
    else:
        pass
# print(costs)

#Exercise 5
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
print(any_lowercase1('SSSsSss'))
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3('asdas'))

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
