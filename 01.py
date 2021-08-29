# author: @derurknallwareininsidejob
# this program prints out a sequence of n 
# defined by the collatz conjecture aka. 3n+1 problem

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            print(end='%')
            # n is an odd number
            n = 3*n + 1
        else:
            print(end='/')
            # n is an even number
            n = n//2
    print(1, end='')
 
 
n = int(input('Enter n: '))
print('Sequence: ', end=' ')


collatz(n)
print('')
