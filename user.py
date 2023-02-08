class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a member")

    def spend_points(self,amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("You do not have sufficient points to spend")

user_jorge = User("Jorge","Leon","jorge2751@gmail.com",26)

user_jorge.display_info()
user_jorge.enroll()

user_alex = User("Alex","Tran","idk@gmail.com",24)
user_jane = User("Jane","Tran","idk@gmail.com",3)

user_jorge.spend_points(50)
user_alex.enroll()
user_alex.spend_points(80)
user_jorge.display_info()
user_alex.display_info()
user_jane.display_info()
user_jorge.enroll()
user_jane.spend_points(40)