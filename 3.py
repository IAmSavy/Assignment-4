from random import randint

for loop_variable in range(10):
    Number1 = randint(0,10)
    Number2 = randint(0,10)
    if int(input('Question: ' + str(Number1) + ' x ' + str(Number2) + ' = ')) == Number1 * Number2: print('Right!')
    else: print('Wrong. The answer is ', Number1 * Number2)