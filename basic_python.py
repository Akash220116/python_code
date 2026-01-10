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

#list 
num = [1,2,3,5,6]
num2 = [7,9,10]
num.append(10)
print(num)
num.insert(3,13)
print(num)
num.extend(num2)
print(num)
num.remove(3)
print(num)
pop1 = num.pop(4)
in1 = num.index(7)
print(pop1,in1)
num.sort()
print(num)

l =[5,-1,6,3,-5,-3,-2,9]
pl = []
nl =[]
for i in l:
    if i>=0 :
        pl.append(i)
    else :
        nl.append(i)
print (f"positive number is {pl}")
print (f"negative number is {nl}") 


#dict
d={10:20,20:300,30:456}
print(type(d))
print(d[10])
d[20] = 700    #change
print(d[20])
d.update({50:430})  #add a new value in dict
print(d)            #full dict print
d[60] = 890  # it also add
del d[30]  #delete
print(d)
for i in d:
    print(i) #print keys
    print(d[i])  #print values
#merge two dict 
d1 ={1:10,2:20,3:30}
d2 ={4:40,5:50,6:60}
for i in d2:
    d1[i]=d2[i]
    print(d1)  

    print("akash")

#deep copy
#if we change the copy it changes the main
a =[1,2,3,4,5,6]
b = a
b[0] = 65
print (a)  

#shallow copy
#if we change the copy it changes only this copy
a =[1,2,3,4,5,6]
b = a.copy()
b[0] = 65
print (a)

#Exception handles
a = int(input("Enter a number "))
try:
    print(10/a)
except Exception as err:
    print(f"there are an error as {err}")  
 
# raise = create own error
age = int(input("Tell your age "))

try:
    if age<10 or age>18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("welcome to the club")
except Exception as err:
    print(f"An error occured as{err}")

    # class
    class Factory:
        k =16
    def hello(self):
        print("hello world")

Factory().hello()
print(Factory().k)

obj = Factory()
obj.hello()
obj2 = Factory()
print(obj2.k)
    