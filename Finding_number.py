# Returns the largest of the three given numbers    

def find_largest(num1, num2, num3):

  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = find_largest(num1, num2, num3)

print("The largest number is", largest)
