#################################################
#-------------- Exercises - Day 3 --------------#
#################################################

# 1. Declare your age as integer variable
age = int(30)

# 2. Declare your height as a float variable
height = float(178.33)

# 3. Declare a variable that store a complex number
c_num = 3j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input("Base: "))
h = float(input("Height: "))
area = 0.5 * b * h

# 5. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width  
perimeter = 2 * (length + width)
print("Area: ", area)
print("Perimeter: ", perimeter)

# 6. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input("Radius: "))
pi = 3.14
area = pi * r ** 2  
c = 2 * pi * r

# 7. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = input("x-intercept: ")
y = 2*x - 2

# 8. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10

m = (y2 - y1)/(x2 - x1)

# 9. Compare the slopes in tasks 8 and 9.
euclidean_a = (2 ** 2 + 2 ** 2) ** 0.5
euclidean_b = (6 ** 2 + 10 ** 2) ** 0.5

# 10. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y = x**2 + 6*x + 9

# 11. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# 12. Use and operator to check if 'on' is found in both 'python' and 'dragon'
# 13. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# 14. There is no 'on' in both dragon and python
# 15. Find the length of the text python and convert the value to float and convert it to string
# 16. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# 17. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# 18. Check if type of '10' is equal to type of 10
# 19. Check if int('9.8') is equal to 10
# 20. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?