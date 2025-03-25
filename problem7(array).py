#given array of n size find max and min element with min comparisons
n= int(input('Size of array?'))
arr1=input('Enter array where numbers are separated by space')
arr2=arr1.split(' ')
arr=[]
for num in arr2:
    arr.append(int(num))
min=9999999999
max=0
i=0
#while(i<n):
#    if(min>arr[i]):
#        min=arr[i]
#    i=i+1
#i=0
#while(i<n):
#    if(max<arr[i]):
#        max=arr[i]
#    i=i+1
for num in arr:
    if(num<min):
        min=num
    elif(num>max):
        max=num
print('Max:',max)
print('Min:', min)
