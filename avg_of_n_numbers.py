n = int(input())
sum=0
for i in range(n):
    num=float(input())
    sum+=num
average=sum/n
print("The average is: {:.2f}".format(average))
