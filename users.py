class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("first name = ",self.first_name)
        print("last name = ",self.last_name)
        print("email = ",self.email)
        print("age = ",self.age)
        if self.is_rewards_member == True:
            print(f"{self.first_name} is a rewards member")
        else:
            print(f"{self.first_name} is not a rewards member")
        print("gold card points = ",self.gold_card_points)
    
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} is already a rewards member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points =+ 200
            return True
    
    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("insufficient points")


# didn't create 2 more instances and follow instructions exactly
print("A")
michael = User("Michael","DuWors","m@m.m","25")
michael.display_info()
print("B")
print(michael.enroll())
michael.display_info()
print("C")
michael.spend_points(75)
michael.display_info()
print("D")
print(michael.enroll())
print("E")
michael.spend_points(500)
michael.display_info()



