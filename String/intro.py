String1 = 'Welcome to my world'
print("String with single quotes: ")
print(String1)

String2 ="Welcome to my nation"
print("String with double quotes: ")
print(String2)

String3='''Welcome
           to 
           my  
           state'''
print("String with triple quotes: ")
print(String3)

#Length of String
S = 'Welcome to my world'
print("Length of string is: ")
print(len(S))
 
#Finding the character in the string
def findChar(s: str, ch: str) -> int:
    n = len(s)
    for i in range(n):
        if s[i] == ch:
            return i
    return -1
if __name__ == "__main__":
    s = "Welcome to my world"
    ch = 'o'
    print(findChar(s, ch))
    
#Finding the character in the string, using buil-in function
def findCharIndex(s: str, ch: str) -> int:
    idx = s.find(ch)
    return idx
s= "Welcome to my world"
ch='o'
index = findCharIndex(s,ch)
print(index)

#Inserting a character in the string
def insertChar(s: str, ch: str, pos: int) -> str:
    return s[:pos] + ch + s[pos:]
s="Welcome to my world"
print(insertChar(s, '!', 7))

#Deletion of a character in the string
str = "Welcome to my world"
pos = 7
modified_str=str[:pos]+str[pos+1:]
print("Modified string: ", modified_str)

#Checking same string or not
def areStringSame(s1: str, s2: str) -> bool:
    return s1 == s2
s1 = "Welcome to my world"
s2 = "Welcome to my world"    
if areStringSame(s1,s2):
    print("Yes, both strings are same")
    
#Concatenation of two strings
def main():
    s1="Welcome to my world"
    s2="You have the permission"
    res=s1+s2
    print(res)
if __name__ == "__main__":
    main()
    
#Reversing a string using two pointer
def reverseString(s):
    left =0
    right=len(s)-1
    s =list(s)
    while left<right:
        s[left],s[right]=s[right],s[left]`
        left+=1
        right-=1
    return "".join(s)
if __name__ == "__main__":
    s="Welcome to my world"
    print(reverseString(s))
    
#Reversing a string using backward traversal
def reverseString(s):
    res=[]
    for i in range(len(s)-1,-1,-1):
        res.append(s[i])
    return ''.join(res)
if __name__ == "__main__":
    s="Welcome to my world"
    print(reverseString(s))

