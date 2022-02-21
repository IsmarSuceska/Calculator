import math
score=0
new_score=0
numx=0

  #Make sure to check if the value is correct mathemathical sign!

class Operations:

    def score(self):
        self.score=score

    def subtraction(self):
        self.score=num1+num2
        return self.score
    def deduction (self):
        self.score=num1-num2
        return self.score
    def multiply(self):
        self.score=num1*num2
        return self.score

    def division (self):
        self.score=num1/num2
        return self.score

opy=Operations()
play=True

num1=int(input('PLease enter first number: '))
operation=input('Enter mathemathical operation: ')  # Let it be saved here, we will use it later on in the project
num2=int(input('Enter second number: '))

  #Calculation time!

def just_two(num1,num2):
    if operation=='+':
        return opy.subtraction()
    elif operation=='-':
        return opy.deduction()
    elif operation=='*':
        return opy.multiply()
    elif operation =='/':
        return opy.division()

def more_then_two():
    numx=int(input('Yo, add another one brah: '))
    operation = input('Enter mathemathical operation: ')

    if operation=='+':
        new_score = opy.score + numx
        return new_score
    elif operation=='-':
        new_score= opy.score - numx
        return new_score
    elif operation == '/':
        new_score=opy.score/numx
        return new_score
    elif operation == '*':
        new_score=opy.score * numx
        return new_score

play_on=input('Would you like to continue ')

if play_on == 'Y':
    print(more_then_two())
else:
    print(just_two(num1,num2))

    #Comments
    # Fix the bug with def more_then_one
