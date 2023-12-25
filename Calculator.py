## Mohsen Pourdehghan


#-----Define functions-----
def addition(x):
        result = 0
        for nums in x:
                result += nums
        return result

def minus(x):
        if len(x) == 1 :
                result = x
                return result
        elif len(x) >= 2:
                result = x[0] - x[1]
                for nums in range(2,len(x)):
                        result -= x[nums]
                return result

def multiply(x):
        result = 1
        for nums in x:
                result *= nums
        return result

def division(x):
        result_list=[]
        operand_number = x[1]
        if len(x) == 2 and x[1] != 0:
                result_list.append(x[0] / x[1])
                return result_list, operand_number
        
        elif len(x) == 2 and x[1] == 0:
                return result_list, operand_number
        
        else:
                operand_number = input('What number do you want to divide the numbers by? ')
                while (operand_number.isdigit() == False) or operand_number.count('0') == len(operand_number) :
                        operand_number = input('AGAIN!!! What number do you want to divide the numbers by? ')
                operand_number = int(operand_number)
                for nums in x:
                        result_list.append(nums / operand_number)
                return result_list, operand_number
#-----

numbers_list = []

#-----1st number Validation-----       
number_1 = input('enter your first number: ')
while number_1.isdigit() == False :
        number_1 = input('AGAIN!!! enter your first number: ')
number_1 = int(number_1)
numbers_list.append(number_1)
#-----

#-----2nd number Validation-----
number_2 = input('enter your second number: ')
while number_2.isdigit() == False :
        number_1 = input('AGAIN!!! enter your second number: ')
number_2 = int(number_2)
numbers_list.append(number_2)
#-----

#-----Request more number-----
more_number = True
while more_number == True :
    more_number = input('need to write more number? (yes/no) ')
    while more_number != 'yes' and more_number != 'no' :
        more_number = input('AGAIN!!! need to write more number? (yes/no) ')
        
    if more_number == 'yes':
        more_number = True
        new_number = input('enter your number: ')
        while new_number.isdigit() == False :
            new_number = input('AGAIN!!! enter your number: ')
        new_number = int(new_number)
        numbers_list.append(new_number)
    else :
        more_number = False
#----- 

#-----Select operator-----
operator = input('which operator you want? (* _ / _ + _ -) ')

while operator != '*' and operator != '/' and operator != '+' and operator != '-':
        operator = input('AGAIN!!! which operator you want? (* _ / _ + _ -) ')

if operator == '*':
        print(multiply(numbers_list))

elif operator == '/':
        div_result, div_operand = division(numbers_list)
        if len(div_result) == 1:
                print(f'\nthe results for division of {numbers_list[0]} by {div_operand} : {div_result[0]}')

        elif len(div_result) == 0 :
                print('Can not divide by zero!')
        else:
                print('\n')
                for index in range(len(div_result)):
                        print(f'\nthe results for division of {numbers_list[index]} by {div_operand} : {div_result[index]}')
    
elif operator == '+':
        print(addition(numbers_list))

elif operator == '-':
        print(minus(numbers_list))
#----- 
