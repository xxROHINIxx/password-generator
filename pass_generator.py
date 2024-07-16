import random
# import string

# letters=list(string.ascii_lowercase + string.ascii_uppercase)
# numbers=list(string.digits)
# symbols=list(string.punctuation) #instead typing the letters,numbers and symbols entirely u can also import string and use this method.

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A',
'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$',"%",'^','&','+']

print("Welcome to password generator")

n_letters=int(input("How many letters do you want to add in your password?"))
n_numbers=int(input("How many numbers do you want to add in your password?"))
n_symbols=int(input("How many symbols do you want to add in your password?"))

password=[]

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password += char

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char

for i in range(1,n_symbols):
    char=random.choice(symbols)
    password+=char

random.shuffle(password) #random shuffle cannot be used in string since they are immutable. so you have to convert the string to a list and use the join method.
shuffled_pass=''.join(password)
print(shuffled_pass)

print("Your password has been generated successfully!")