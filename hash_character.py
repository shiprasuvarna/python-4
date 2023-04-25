#Write a Python program to replace each character of a word of length five and more with a hash character (#).
#Sample Output: Original string: Count the lowercase letters in the said list of words:
#Replace words (length five or more) with hash characters in the said string:
#riginal string: Python - Remove punctuations from a string:
#Replace words (length five or more) with hash characters in the said string:
#- ###### ############ from a
#the ######### ####### in the said list of
def test(text):
  for i in text.split():
   if len(i) >= 5:
     text = text.replace(i, "#" * len(i))
  return text
text ="Count the lowercase letters in the said list of words:"
print("Original string:", text)
print("Replace words (length five or more) with hash characters in the said string:")
print(test(text))
text = "Python - Remove punctuations from a string:"
print("\nOriginal string:", text)
print("Replace words (length five or more) with hash characters in the said string:")
print(test(text))
