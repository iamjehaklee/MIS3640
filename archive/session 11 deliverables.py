#Number 1.

def histogram(s):
    d = dict()
    for c in s:
        letters = d.get(c,0)
        d[c] = letters
    for c in s:
        d[c] += 1 
    return d

print(histogram('Bookkeeper'))

#Number 4 
def loadWords():
    inFile = open("words.txt", 'r')
    line = inFile.readline()
    wordlist = line.split()
    x = dict()
    for words in wordlist:
        x[words] = 1
    return x

print(loadWords())

#number 2
def hasduplicates(s):
    z = dict()
    for c in s:
        z[c] = 0    
    for c in s:
        z[c] += 1
#    if the value of a dictionary is > 1, then return true. but how do i find the value of a dictionary that is greater than 2? 


test = ['a','b','c', 'c']

hasduplicates(test)