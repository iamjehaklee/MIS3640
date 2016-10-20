# fin = open('words.txt')

# 1
# def read_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
#     for word in fin:
#         words = word.strip()
#         if len(words) > 20:
#             print(words) 

# read_long_words()
     
# 2

# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter “e” in it.
#     """
#     for i in word:
#         if i == 'e':
#             return False 
#     return True

# print(has_no_e('hidsfdsfewiuwjidse'))

# 3

# def avoids(word, forbidden):
#     """
#     takes a word and a string of forbidden letters, and that returns True
#     if the word doesn’t use any of the forbidden letters.
#     """
#     for i in word:
#         if i in forbidden:
#             return False
#     return True

# print(avoids('Babson','plplpplplb'))

# 4 
# def uses_only(word, available):
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
#     for i in word:
#         if i not in available:
#             return False
#     return True

# print(uses_only('Babson','aBbsonxyz'))

# 5 
# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     return(uses_only(required, word))


# print(uses_all('Babson','aBbsonxyz'))

#6 
def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    x = len(word)
    y = 0 
    for i in range(x):
        if i + 1 == x:
            pass
        else:
            if word[i+1] >= word[i]:
                y = y + 1
    if y == x-1:
        return True
    return False


print(is_abecedarian('ab'))
print(is_abecedarian('ba'))
print(is_abecedarian('abcdza'))
print(is_abecedarian('abfaabcd'))