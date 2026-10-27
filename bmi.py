#bm1 calc
# • Underweight: Below 18.5
#
# • Healthy Weight: 18.5 to 24.9
#
# • Overweight: 25.0 to 29.9
#
# • Obesity (Class I): 30.0 to 34.9
#
# • Obesity (Class II): 35.0 to 39.9
#
# • Severe Obesity (Class III): 40.0 or higher
weight= input("Please enter your weight in kgs:")
height= input("please enter your height in m:")

w= float(weight)
h= float(height)

bmi= w/h**2

if bmi<18.5:
    print("you are underweight")

elif bmi>=18.5 and bmi<=24.9:
    print("you are Healthy")
elif bmi>=25.0 and bmi<=29.9:
    print("you are overweight")
elif bmi>=30.0 and bmi<=34.9:
    print("you are obese class1")
elif bmi>=35.0 and bmi<=39.9:
    print("you are obese class2")
else:
    print("you are obese class3")


