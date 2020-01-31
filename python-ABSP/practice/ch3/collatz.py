def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

n = None
while not n:
    print('Enter number:')
    try:
        n = int(input())
    except:
        print('Invalid input')
        n = None
        continue 

while n != 1:
    n = collatz(n)
