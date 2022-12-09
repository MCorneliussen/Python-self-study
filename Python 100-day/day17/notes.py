# making a class

class NewUserExample: 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #print("New user being created...")
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = NewUserExample("001", "angela")
user_2 = NewUserExample("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
class Car: 
    def __init__(self, seats):
        #initialise attributes
        self.seats = seats
        #Sets the attribute of the object

my_car = Car(5)

#my_car.seats = 5




# PascalCase > Used in making classes 
# camelCase > 
# snake_case > used for pretty much everything else
