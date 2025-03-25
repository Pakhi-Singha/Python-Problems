#target given with array, if 2 numbers of array added, we get target, output the 2 numbers
n= int(input('Size of array?'))
arr1=input('Enter array where numbers are separated by space')
arr2=arr1.split(' ')
arr=[]
for num in arr2:
    arr.append(int(num))
target=int(input('Target?'))
i=0
j=0
while(i<n):
    while(j<n):
        if(arr[i]+arr[j]==target):
            print('Position of 1st number:',i+1)
            print('Position of 2nd number',j+1)
        j=j+1
    i=i+1