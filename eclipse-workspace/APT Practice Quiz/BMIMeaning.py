'''
Created on Jan 31, 2018

@author: lavonnehoang
'''

def interpret(weight,height):
    BMI = 703.0695 * (weight/(height**2))
    if BMI >= 40:
        return ("obese")
    elif 25<BMI<40:
        return ("overweight")
    elif BMI<16:
        return ("underweight")
    elif 16<BMI<24:
        return ("normal")



if __name__ == '__main__':

    print (interpret(200,60))