#programme to get a secured password 
# in this programme the commonly used alphabets are replaced with there corresponding partner according to their shape 
def passgene(password):
    secure = (('s', '$'), ('and', '&'), ('i', '|'), ('1', '!'), ('v', '^'), ('a', '@'),
              ('o', '0'), ('c', '('), ('h', '#'), ('f', '£'), ('e', '€'), ('8', '∞'), ('r', '®'))

    for i, j in secure:
        password = password.replace(i, j)

    return password
password = input("Enter the password: ")
secpass = passgene(password)
print("Secure password:", secpass)
