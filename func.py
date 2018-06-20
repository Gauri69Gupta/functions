print("QUESTION-1")
def area(radius):
    ar=3.14*radius*radius
    return ar
radi=float(input("Input radius of the circle"))
area_circle=area(radi)
print(area_circle)
print("\n")
print("Question2")
def perfect(n):
    sum=1
    i=2
    while i*i<=n:
        if n%i ==0:
            sum=sum+i+n/i
        i=i+1
    if(sum==n and n!=1):
        return True
    else:
        return False
print("Perfect Number")
n=2
for n in range(1000):
    if perfect(n):
        print(n,"is a perfect number")
print('*'*10)
print('\n')

print("Question3")
def table(n,time=1):
 if time<=10:
  print("%d*%d="%(n,time),n*time)
  time=time+1
  table(n,time)
num=int(input("Enter the value"))
table(num)

print("Quesion-4")
def power(a,b):
   if(b==1):
       return(a)   
   else:
       return(a*power(a,b-1))
            
a1=int(input("Enter the base value"))
b1=int(input("Enter the exponential value"))
cal=power(a1,b1)
print(cal)

print("QUESTION-5")
print("Question5")
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
list1=[]
dict1={}
n = int(input("Enter number of elemets:"))
for i in range(n):
    num = int(input("Enter number:"))
    list1.append(num)
for j in list1:
    t=factorial(j)
    dict1[j]=t
print("Dictionary:")
for k,v in dict1.items():
    print(k,":",v)
