a = input("enter a string:")
b = input("enter a string:")
c = 0

if len(a) == len(b):
    for i in a:
        if a.count(i) == b.count(i):
            c += 1

    if c == len(a):
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram")

        
