def test_square_root(a):
    a = float(a)
    x = 5
    while True:
        y = (x + (a/x))/2
        if abs(y-x) < 0.0000001:
            break
        x = y
    return x

print(test_square_root(9))


for z in range(1, 9):
    print(z)
