"""# Creating a dictionary with emoji mappings
emojis = {"happy": "😊", "sad": "😢"}

# Safely getting the 'happy' emoji
print(emojis.get("happy"))  # Prints 😊

# Looping through the dictionary items
for key, value in emojis.items():
    print(f"{key}: {value}")  # Prints each key-value pair

# Adding a new key-value pair
emojis["angry"] = "😠"

# Checking if a key exists
if "sad" in emojis:
    print("Sad emoji is present.")

# Removing a key-value pair
removed = emojis.pop("angry")
print(f"Removed: {removed}")

# Getting all keys and values separately
keys = list(emojis.keys())
values = list(emojis.values())
print("All keys:", keys)
print("All values:", values)

# Clearing the dictionary
emojis.clear()
print("After clearing:", emojis)


"""


"""
a={"dog":"bark","cat":"meow","cow":"moo","lion":"roar","horse":"neigh"}

#foundation task
print("Animal Sounds")
for i,j in a.items():
    print(f"{i} says {j} ")
   

#stretch task
print(a)
a["duck"]="quack"
print(a)
a["cow"]="moomoooo"
print(a)

"""
#chsllenge task
print("Grade Tracker")
b={"ann":80,"john":75,"Peter":95}
print(b)
average=sum(b.values())/len(b)
print(f"Average Grades :{average}" )

highest=max(b,key=b.get)
lowest=min(b,key=b.get)

print("Highest scorer:",highest, "(",b[highest],")")
print("Lowest scorer:",lowest, "(",b[lowest],")")

b["David"] = 90  

print("\nUpdated Students:",b)

