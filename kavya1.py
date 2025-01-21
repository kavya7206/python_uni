def stringinstring(str1, str2):
    if  str2 in str1:
         print("the string is present ")
    else:
        print("the string is not present")

str1= input("Enter a string:")
str2= input("Enter another string:")
stringinstring(str1, str2)
