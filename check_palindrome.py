# Check if a string is palindrome
# s=input("Enter any sting or name or number or word= ")

#>>>>>>>>>>> using build in sliceing operator --> [star:end:jump] <<<<<<<<<<<<<

# if s==s[::-1]:
#     print(s,"=",s[::-1],"--> Yes it is a palindrome")
# else:
#     print(s,"=",s[::-1],"--> No it is not a palindrome")


#>>>>>>>>>>>>>>>>>>>>>> my won Algorithm <<<<<<<<<<<<<<<<<<<<

# b=""
# for i in s:
#     b=i+b
# if b==s:
#     print(s,"=",b,"--> Yes it is a palindrome")
# else:
#     print(s,"=",b,"--> No it is not a palindrome")


#>>>>>>>>>>>>>>>>>> my won palindrom function palid() <<<<<<<<<<<<<<

def palid(value):
    b=""
    for i in value:
        b=i+b
    if b==value:
        return f"{value} = {b} --> Yes it is a plindrome"
    else:
        return f"{value} = {b} --> No it is not a plindrome"

s=input("Enter any sting or name or number or word= ")
print(palid(s))
