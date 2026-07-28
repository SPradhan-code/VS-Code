s ={10,50,20}
print(s)
print(type(s))

#Typecasting a set to list
s = set(["a", "b", "c"])
print(s)

#Values of set cannot be changed
#sets cannot have duplicate elements
s=set(["a", "b", "c", "a", "b"])
print(s)
s[1]="F"
print(s)

#Frozen Set
s=set(["a", "b", "c"])
print(s)
fs=frozenset(["a", "b", "c"])
print("Frozen Set:", fs)

#Adding elements to a set
s=set(["a", "b", "c"])
print(s)
s.add("d")
print(s)

#Union of two sets
s1=set(["a", "b", "c"]) 
s2=set(["c", "d", "e"])
u= s1.union(s2)
print(u)

#Intersection of two sets
s1=set(["a", "b", "c"]) 
s2=set(["c", "d", "e"]) 
i=s1.intersection(s2)
print(i)

#difference of two sets
s1=set(["a", "b", "c"]) 
s2=set(["c", "d", "e"]) 
d=s1.difference(s2)
print(d)

#Clearing a set
s=set(["a", "b", "c"])
print(s)
s.clear()
print(s)