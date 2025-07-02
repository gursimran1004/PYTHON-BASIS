n=int(input("list"))
num=[]
for i in range (n):
    number=int(input("enter numbers"))
    num.append(number)
max_value=max(num)
min_value=min(num)
sum_value=sum(num)
print("the maximum number",max_value)
print("the minimum  number",min_value)
print("the sum of the mumbers is ",sum_value)
    
