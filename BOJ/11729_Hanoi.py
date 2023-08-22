def hanoi(n, start, temp, target):
    if n == 1:
        print(start, target)
        return
    if n < 1:
        return

    hanoi(n-1, start, target, temp)
    hanoi(1, start, temp, target)
    hanoi(n-1, temp, start, target)
    return

def hanoi_1numb(n1):
    print(2 ** n1 - 1)
    hanoi(n1,1,2,3)



a = int(input())


hanoi_1numb(a)
