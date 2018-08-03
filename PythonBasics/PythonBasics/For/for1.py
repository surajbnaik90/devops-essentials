#Simple for loop in python to find out the sum of the series

series = "1,2,3,4,5,6,7,8,9"
sum = 0

for i in range(0,len(series)):
   if(series[i] in '0123456789'):
        print(series[i],end='')