weight = 86
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
print (bmi)

if bmi < 18.5:
    print("underweight")
    
elif bmi >= 18.5 and bmi < 25:
        print("normal weight")
    
elif bmi >= 25:
        print("overweight")
        
else:
    print("wrong input")
    