def fizzbuzz(x, y):# Defining 

    s = len(x)+len(y)
    
    if (s%3==0 and s%5==0):
        print('fizzbuzz')
    elif s%5 == 0:
        print('Buzz')
    elif s%3==0:
        print('fizz')
    else:
        print (s)

x = [3,4,6,5]
y = [1,3,5,3,3,4,5,7,8,9]

fizzbuzz(x,y)
