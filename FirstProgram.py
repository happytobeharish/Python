#a=int(input("Enter first value :"))
#b=int(input("Enter second value :"))
#print(a>=b)

#name = input("(str)Enter Your Name :")
#print("Length of your name is :", len(name))


#str = "hi i am $ symbol $99.99 102$ 100k usd$" 
#print(str.count("$"))



marks = int(input(" Enter The Marks :"))

if (marks  >= 90) :
    grade ="A"
elif (marks >=80 and marks <90):
    grade ="B"
elif (marks >=70 and marks <80):
    grade ="C"
elif (marks >=60 and marks <70):
    grade ="D"
else : 
    grade="Fail"            

print("grade of the student ->", grade)