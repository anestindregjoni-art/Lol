# Exercise 1
name = input("Enter the student's name: ")
score = int(input("Enter the test score (0-100):"))

if score >= 90:
    grade = "A"
    result = "Pass"

elif score >= 80:
    grade = "B"
    result = "Pass"

elif score >= 70:
    grade = "C"
    result = "Pass"

elif score >= 60:
    grade = "D"
    result = "Pass"

else:
    grade = "F"
    result = "Fail"

print (name, "has", result, "with grade", grade)


# Exercise 2

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Exercise 3

salary = float(input("Enter your salary:"))

if salary <= 1000:
    tax_rate = 0.20
elif salary <= 2500:
    tax_rate = 0.15
else:
    tax_rate = 0.10

tax = salary * tax_rate
take_home = salary - tax

print("Your salary is", salary,", of which", tax,"is tax and you take home", take_home)

#Exercise 4

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter the third number: "))

largest=num1

if num2 > num1:
    largest = num2
if num3 > largest:
    largest = num3
print("Between", num1, "," , num2, "and" , num3 , largest, "is the largest number")

