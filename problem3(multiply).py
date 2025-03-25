#if user give number, give multiplication table
n=int(input('Enter number'))
i=1
while(i<=10):
    s=n*i
    print(n,'*',i,'=',s)
    i=i+1