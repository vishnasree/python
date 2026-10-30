
a = input("Enter a string: ")
for i in a:
    if i.lower() in "aeiou":
        print("*", end="")
    else:
        print(i, end="")
    
        
