#Python Dictionary

#key  :  value
'''
{"bug": "bug value"}
'''

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.", 
                          "Loop": "The action of doing something over and over again.",}
#list and index 0 = Important thing that most student fail to do is use the correct data type when calling for the item in the dictionary
'''
print(programming_dictionary["Loop"])

#make new dictionary
new_dictionary = {}

#wipe existing dictionary
programming_dictionary = {}

#adding to existing dictionary
programming_dictionary["Poop"] = "The action of unburdening your bowels."
        #               ^key          ^the value



#Edit dictionary
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)
#Tried printing out "Bug" from the programming dictionary but kept getting an error. 
# After trying around for a couple of minutes i realized It was not a bug, it was the value of bug and i did everything right...

'''
#looping through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
    
#nesting list and dictionary


'''
list1 = {key1: [list],
         key2: {dict},
         }
'''
#Example + Each key can only have 1 value BUT you can use a list!

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#nesting
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
}
