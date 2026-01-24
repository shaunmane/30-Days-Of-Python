## 💻 Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = ['Thirty', 'Days', 'Of', 'Python']
con_string = ' '.join(string)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string = ['Coding', 'For' , 'All']
con_string = ' '.join(string)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string = "Coding For All"
print(string.capitalize())
print(string.title())
print(string.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
string = "Coding For All"
print(string[:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
string = "Coding For All"
print(string.index("Coding"))

# 11. Replace the word coding in the string 'Coding For All' to Python.
string = "Coding For All"
print(string.replace("Coding", "Python"))

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods. 
string = "Python for Everyone"
print(string.replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
string = "Coding For All"
print(string.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))

# 15. What is the character at index 0 in the string Coding For All.
string = "Coding For All"
print(string[0])

# 16. What is the last index of the string Coding For All.
string = "Coding For All"
print(string[-1])       

# 17. What character is at index 10 in "Coding For All" string.
string = "Coding For All"
print(string[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python For Everyone'
print(string.split(" ")[0][0] + string.split(" ")[1][0] + string.split(" ")[2][0])

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
string = "Coding For All"
words = string.split(" ")
print(words[0][0] + words[1][0] + words[2][0])

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
string = "Coding For All"
print(string.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
string = "Coding For All"
print(string.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = "Coding For All People"
print(string.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = "You cannot end a sentence with because because because is a conjunction"
print(string.index("because"))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = "You cannot end a sentence with because because because is a conjunction"
print(string.rindex("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = "You cannot end a sentence with because because because is a conjunction"
print(string[31:54])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = "You cannot end a sentence with because because because is a conjunction"
print(string.find("because"))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = "You cannot end a sentence with because because because is a conjunction"
print(string[31:54])

# 28. Does 'Coding For All' start with a substring Coding?
string = "Coding For All"
print(string.startswith("Coding"))

# 29. Does 'Coding For All' end with a substring coding?
string = "Coding For All"
print(string.endswith("Coding"))

# 30. '   Coding For All      ' , remove the left and right trailing spaces in the given string.
string = "   Coding For All      "
print(string[3:-3])

# 31. Which one of the following variables return True when we use the method isidentifier():
string1 = "30DaysOfPython"
string2 = "thirty_days_of_python"
print(string1.isidentifier())       # False
print(string2.isidentifier())       # True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(libraries))

# 33. Use the new line escape sequence to separate the following sentences.
string = "I am enjoying this challenge. \nI just wonder what is next."
print(string)

# 34. Use a tab escape sequence to write the following lines.
print("Name\t\tAge\tCountry\t City")
print("Asabeneh\t250\tFinland\t Helsinki")

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# 36. Make the following using string formatting methods:
a = 8
b = 6
print(f" {a} + {b} = {a + b}")
print(f" {a} - {b} = {a - b}")
print(f" {a} * {b} = {a * b}")
print(f" {a} / {b} = {a / b:.2f}")
print(f" {a} % {b} = {a % b}")
print(f" {a} // {b} = {a // b}")
print(f" {a} ** {b} = {a ** b}")