# author: @derurknallwareininsidejob
# this program runs through several numbers' collatz sequence
# counts number of steps in sqc, prints highest number of steps

def collatz(n):
    ch = 0
    while n < h:
        c = 0
        s = n
        while n > 1:
            if (n % 2):
                n = 3*n + 1
#                print('%', end='')
                c = c+1
            else:
                n = n//2
#                print('/', end='')
                c = c+1
        if (c >= ch):
            ch = c
            nh = s
            print(nh,end=': ')
            print(ch, end=' steps')
            print('')
        n = s + 1
    print('')
    print(ch,' steps by # ',nh)

n = int(input('Enter Starting Number: '))
h = int(input('Enter End Number: '))

print('Starting Point: ',n, end='\n')
print('End Point: ',h, end='\n')
input("Press Enter to continue")

collatz(n)
