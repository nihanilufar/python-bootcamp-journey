string = input("Enter a string: ")

count = 0
for char in string:
    if char in "a,e,i,o,u":
        count += 1
        
print("number of vowels:  ",count)
