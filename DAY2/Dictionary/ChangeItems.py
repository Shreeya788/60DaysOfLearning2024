thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)     #before updating

# can be done by referring to its key name

thisdict["year"] = 2024
print(thisdict)     #after updating

# values can be updated using update() function

thisdict.update({"year" : 2023})
print(thisdict)

#Items can be added by:

#Method 1:
thisdict["color"] = "red"
print(thisdict)

#Method 2: Using update() method
thisdict.update({"modelNo": "mxy65"})
print(thisdict)