''' Six Odd Numbers

Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.
Input

The input will be a positive integer value.
Output

The output will be a sequence of six odd numbers.

'''

if __name__ == '__main__':
    
    x = input()
    y = int(x)
    counter = 0
    while counter < 6:
        if y % 2 != 0:
            print(y)
            counter +=1
        y += 1
    