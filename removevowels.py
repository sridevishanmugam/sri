def remove(n):
    string=input()
    string=string[0:n]
    vowels=('a','e','i','o','u')
    for x in string.lower():
        if x in vowels:
            string=string.replace(x, "")
    string=string[::-1]
    print(string)
    
n=int(input())

remove(n)
