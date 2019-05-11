
def collatz(x):
    if x % 2 == 0:  # if even
        return x // 2
    elif x % 2 == 1:
        return 3 * x + 1


print('Input the initial number for the Collatz Sequence (different from 1, and larger than 0):')
try:
    num_input = int(input())
    if num_input == 1:
        print('1 is the converged final value of the sequence')
    else:
        print('Collatz Sequence:')
        while num_input != 1:
            num_input = collatz(num_input)
            print(num_input)
except ValueError:
    print('Error: Please input the integer')

