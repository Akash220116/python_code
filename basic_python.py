print("Akash")
b =1+5
c =14/5
print(type(c))
print (b)
print(type(b))
a= "A"
print(ord(a))
d=65
print(chr(d))

e ="akash mony"
print(e[0:5:1])

name ="Mony"
age =23

print ("my name is",name,"and my age is",age) #process 1
print(f"my name is {name} and my age is {age}") #process 2

#input
num = int(input("Enter a number"))
age =int(input("Enter the age"))
print(num,age)

#if_else
if 13>10 :
    print("true")
else :
    print ("false")

#for loops

for i in range(1,21,1):
    print( i )

name = "Akash mony"
print(name[0:5:1]) 

for i in range (21):
   print (i)
 
n = int(input("enter the number ")) 

for i in range (1,n+1,1) :
   print (i)  

evensum = 0 
oddsum = 0
n = int(input("Enter the number "))
for i in range(n+1):
    if (i%2==0):
        evensum += i
    else :
        oddsum +=i 

print(f"even sum is {evensum}") 
print(f"odd sum is {oddsum}") 

# while loops
a = 5
while a < 10 :
    print ("akash")
    a += 1 

#funtion
def sum(name,surname):
    return (name+surname)

print(sum("akash ","mony")) 