import math

class Circle:
    def __init__(self, r):
        self.r = r    
    
    def obim(self):
        return 2*self.r*3.14

class Operations:
    def __init__(self, score):
        self.score = score
    def addition(self, num):
        self.score += num
        return self.score
    def deduction (self, num):
        self.score -= num
        return self.score
    def multiply(self,num):
        self.score *= num
        return self.score
    def division (self, num):
        self.score /= num
        return self.score


def main():
    num1 = int(input('PLease enter first number: '))
    opy = Operations(num1)

    play = True
    b = 1
    while(play):
        operation = input('Enter mathemathical operation: ')  # Let it be saved here, we will use it later on in the project
        num2 = int(input('Enter second number: '))

        if operation=='+':
            opy.addition(num2)
        elif operation=='-':
            opy.deduction(num2)
        elif operation=='*':
            opy.multiply(num2)
        elif operation =='/':
            opy.division(num2)

        play_on=input('Would you like to continue ')

        if play_on != 'Y':
            play = False
        
    print(opy.score)


if __name__ == "__main__":
    main()
