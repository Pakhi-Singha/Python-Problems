#reverse array 
n= int(input('Size of array?'))
arr1=input('Enter array where numbers are separated by space')
arr2=arr1.split(' ')
arr=[]
for num in arr2:
    arr.append(int(num))
rev=arr[::-1]
print(rev)