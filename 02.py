# author: @derurknallwareininsidejob
# this program runs through several numbers' collatz sequence
# halts when n == s, starts at starting number

def collatz(n):
    while True:
        s = n
        print('\n')
        print(n,end='\n')
        while n >= s:
            print('')
            if (n % 2):
                n = 3*n + 1
                print('%', end=' ')
            else:
                n = n//2
                print('/', end=' ')
            if (n == s):
                raise ValueError('found loop @ ',n)
        n = s + 1


n = int(input('Enter Starting Number: '))
e = int(input('to the power of: '))
print('minus 1\n')
n = (n ** e) - 1

print('Starting Point: ',n, end='\n')
input("Press Enter to continue")

collatz(n)
