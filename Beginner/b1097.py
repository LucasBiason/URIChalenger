''' Sequencia IJ3

Make a program that prints the sequence like the following exemple.
	
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''

if __name__ == '__main__':
    
    print("> First try:")
     
    j_control = 7 # Control 7,9,11,13,15,....
    for i in range(1, 10, 2): # 9 times, 2 steps
        j = j_control
        for control in range(1,4): # 3 times
            print('I={} J={}'.format(i, j))
            j -= 1
        j_control +=2

    print("> Refactor:")
    
    j_control = map(lambda x: 7 - x, range(1,4)) # Always be: [6, 5, 4]
    for i in range(1, 10, 2): # 9 times, 2 steps
        for j in j_control: # 3 times
            print('I={} J={}'.format(i, i+j))
    
    print("> Final Refactor:") ## This is the final answer
    
    for i in range(1, 10, 2): # 9 times, 2 steps
        for j in [6, 5, 4]: # 3 times adding to i
            print('I={} J={}'.format(i, i+j))