number = input("Enter a number: ") # take input from user 

number = int(number) #convert string into int

print("The numbered entered was", number)#print the entered number 

if (number % 2==0 and number%10==0):#condtion to check either even or odd
	print("That is an even number and divided by 10 ")
else:
	print("That is an odd numberand not divisible by 10")
