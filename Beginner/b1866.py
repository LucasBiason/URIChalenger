''' Bill
Two friends ask the attendant a snack bar propose a challenge , 
so that whoever hit him more , would not pay the bill. 

Then the following is proposed : 
Given the following sum below report the result , 
with the same number of terms : 
S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ... 

Write a program that , given a number of terms, report the result of the sum above.
'''

c = int(input()) # number of cases

for case in range(c):
    n = int(input())
    # If n is odd, S = 1, if n is even, S =0 always
    print(0 if n % 2 == 0 else 1)
        