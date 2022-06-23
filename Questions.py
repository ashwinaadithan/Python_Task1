#Question 1
a = "Hello World"
char = input("Enter the character:")
print(f'Character entered: {char}')
b = a.replace(char,'')
print(b)

#Question 2
a = "Hello world"
char = input("Enter the character: ")
count = 0
for i in a:
    if(i == char):
        count += 1
print(count)

#Question 3
a = "cat"
b = "act"
if(sorted(a)==sorted(b)):
    print("anagram")
else:
    print("anagram")

#Question 4
a = "malayalam"
if(a == a[::-1]):
    print("palindrome")
else:
    print("not a palindrome")

#Question 5
char = input("Enter the character :")
vowels=['a','e','i','o','u']
if char in vowels:
    print("Vowel")
else:
    print("Consonant")

#Question 6 
char = input("Enter the character : ")
if(char >= '0' and char <= '9'):
    print("Its a Digit")
else:
    print("Its not a digit")

#Question 7
a = input("Enter the value: ")
if a.isdigit():
    print("Digit")
else:
    print("Not a digit")

#Question 8 
a = "I am Groot"
char = '-'
b = list(a)
for i in range(len(b)):
    if(b[i] == ' '):
        b[i] = char
print(''.join(b))

#Question 9
a = "I am Groot";  
char = '-';    
b = a.replace(' ', char); 
print(b); 

#Question 10
a = input("Enter the string : ")
b = ""
for i in a:
    b+=i.upper()
print(b)

#Question 11
a = input("Enter the string : ")
vowels = "aeiou"
for i in a:
    if i in vowels:
        a = a.replace(i,i.upper())
print(a)

#Question 12
a = [i for i in range(1,100)]
a.remove(int(input("")))
b = sum(a)
c = len(a)+1
missing_num=(c*(c+1))//2-b 
print("The missing number is :",missing_num)

#Question 13
a = [4,834,248742,136842,21,3211111,834,11,248742]
b = set(a)
for i in b:
    if a.count(i)>1:
        print("{} has {} duplicates in given list".format(i,a.count(i)))
        
#Question 14
a = [4,834,248742,136842,21,3211111,834,11,248742]
dict={}
for i in a:
    try:
        dict[i]+=1
    except:
        dict[i]=1
for i,j in dict.items():
    print(f'{i} repeat {j} times')
    
#Question 15
a = [1,2]
b = [3,4,5]
if len(a)==len(b):
    print("Yes")
else:
    print("NO")

#Question 16
a = [4,834,248742,136842,21,3211111]
print("The smallest number :",min(a))
print("The largest number :",max(a))

#Question 17
a = [4,834,248742,136842,21,3211111]
a.sort()
b = list(set(a))
b.sort()
print("The second largest number is:",b[-2])

#Question 18 & 20
a = [4,834,248742,136842,21,3211111]
a.sort()
b = list(set(a))
b.sort()
print("The top 2 maximum numbers:",b[len(b)-2:])

#Question 19
a = [4,834,248742,136842,21,3211111,834,11,248742]
b=set(a)
print(list(b))

#Question 21
a = [4,834,248742,136842,21,3211111]
print(a[::-1])

#Question 22
a = [4,834,248742,136842,21,3211111]
b = []
for i in range (len(a)-1,-1,-1):
    b.append(a[i])
print(b)
print(a[::-1])

#Question 23
a = [4,834,248742,136842,21,3211111]
print(len(a))

#Questions 24
a = [4,834,248742,136842,21,3211111]
a.append(10)
print(a)

