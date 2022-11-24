

n = int(input("enther the number: "))
temp = n 
rev = 0
while temp>0:
    rem=temp%10
    rev = rev * 10 + rem
    temp//= 10
if n == rev:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")