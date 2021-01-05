str1=input("enter the first string:")
str2=input("enter the sec string:")
print(str1[::-1])
def compare(str1,str2):
    if len(str1)==len(str2):
        if str1 == str2:
            print("string are equal")
        else:
            print ("print string are not equal")
    else:
        print("string are not equal")
def palendrme(str1):
    str3=""
    str3=str1[::-1]
    print("**************************************")
    if str1==str3:
        print("palendrome")
    else:
        print("not a palendrome")

str=compare(str1,str2)
st=palendrme(str1)