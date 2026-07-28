a={"x":1,"y":2}
print(a)

b=dict(name="Sam",age=20)
print(b)

#Accessing dictionary items
d=dict(name="Kat",age=21)
print(d["name"])    #Accessing using key
print(d.get("age")) #Access using get() method

#Adding and updating dictionary items
d={"name":"Sam"}
d["age"] = "20"
d["name"]="Alex"
print(d)

#Removing Dictrionary items
d = {"a":1,"b":2,"c":3,"d":4,"e":5}
del d["a"]  #remove an item using its key
print(d)

val=d.pop("b") #removes the item with the given key and returns its value
print(val)
print(d)

print(d.popitem()) #removes and return the last inserted key-value pair

d.clear() #removes all item from the dictionary
print(d)

#iterating through a dictionary
d={"a":1,"b":2,"c":3}
for key in d: #return all keys from dictionaries
    print (key)
    
for value in d.values():#returns all values from the dictionary
    print(value)
    
for key, value in d.items():# return all key-value pair as tuple
    print(key,value)
    
#Nested dictionaries
f={
    "student":{
        "name":"Sam",
        "age":20
    }
}

print(f["student"]["name"])