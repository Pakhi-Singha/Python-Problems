#movie ticket pricing: 100 for kids <12, 150 for adults 12-60 years, 120 for seniors age>60, age as input and print ticket price
def checkAge(age):
    if(age < 12):
        print('Ticket price: 100')
    elif(age>=12 and age<=60):
        print('Ticket price: 150')
    elif(age>60):
        print('Ticket price: 120')
age=int(input('What is age?'))
checkAge(age)
