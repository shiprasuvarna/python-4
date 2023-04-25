'''16) Write a function division() that accepts two arguments. The function should be able to catch an
exception such as ZeroDivisionError, ValueError, or any unknown error you might come across when
you are doing a division operation. Modify the earlier “perfect division function” task in such a way
that the function division() has a clean-up action.'''
def division(x,y):
    try:
        div = x/y
        print(f"{x}/{y} = {div}")
    except ZeroDivisionError as e:
        print("Exception occurred!:", e)
    except Exception as e:
        print("Exception occurred!:", e)
    finally:
        print("Working on division function.")
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
division(a,b)
