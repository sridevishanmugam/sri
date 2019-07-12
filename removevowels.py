def remove(string):
    vowels=('a','e','i','o','u')
    for x in string.lower():
        if x in vowels:
            string=string.replace(x, "")
    string=string[::-1]
    print(string)
s=input()
remove(s)
