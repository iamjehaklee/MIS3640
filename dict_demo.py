grades ={'Rose': 90, 'Jerry': 75, 'Alex': 85}
grades['Brian'] = 90

# print('Jerry' in grades)
# print(90 in grades.values())

# print(grades)
# print(grades['Jerry'])


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram('bookkeeper'))