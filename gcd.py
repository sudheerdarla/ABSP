def test(num1, num2):
    minnum = min(num1, num2)

    num1list = []
    num2list = []
    
    for i in range(num1):
        if num1 % (i+1) == 0:
            num1list.append(i+1)
    print(num1list)
    for j in range(num2):
        if num2 % (j+1) == 0:
            num2list.append(j+1)
    print(num2list)
    gcdset = set(num1list).intersection(num2list)
    gcd = sorted(list(gcdset))
    print(gcd[-1])
    
test(200, 30)
