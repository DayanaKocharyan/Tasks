count = 0
def Pakagcer(n, a, b, line):
    global count 
    if a > n:
        return
    if 2 * n == a + b:
        print(line)
        count += 1
        return
    if b == a:
        Pakagcer(n, a + 1, b, line + "(")
    elif a >= b:
        Pakagcer(n, a+1, b, line + "(")
        Pakagcer(n, a, b+1, line + ")")

n = int(input('Enter the number: '))
Pakagcer(n, 0, 0, '')
print(f'Count is {count}')