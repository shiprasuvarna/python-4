#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function
#that multiplies argument x with argument y and prints the result.
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))




#Write a Python program to sort a list of tuples using Lambda.
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)




#Write a Python program to check whether a given string is a number or not using Lambda.
is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))
