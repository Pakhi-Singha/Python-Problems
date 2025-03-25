#max sum of 2 integers in array
n= int(input('Size of array?'))
arr1=input('Enter array where numbers are separated by space')
arr2=arr1.split(' ')
arr=[]
for num in arr2:
    arr.append(int(num))
max=0
i=0
j=0
while(i<n):
    while(j<n):
        if((arr[i]+arr[j])>max):
            max=arr[i]+arr[j]
        j=j+1
    j=0
    i=i+1
print(max-1)

