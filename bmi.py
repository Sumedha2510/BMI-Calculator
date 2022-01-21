Height=float(input("Enter your Height in Centimeters(cm): "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=18.5):
		print("You are Underweight")
	elif(BMI<=24.9):
		print("You are Fit")
	elif(BMI<=30):
		print("You are Overweight")
	else: 
    print("You are Obese")
else:("Invalid Entry, Enter Valid Details")
