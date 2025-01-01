class User:
    def __init__(self, first_name, last_name, address, email, phone, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.hobby = hobby

    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}. I live in {self.address}. My email address is {self.email}. My phone number is {self.phone}. My hobby is {self.hobby}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Welcome to Aspire Leader Program 2025. God bless you a lot in the new year of 2025.")

user1 = User("Laraib", "Fatima", "Karachi", "laraib@gmail.com", "+9298473732", "gardening")
user2 = User("Leena", "Foladi", "Kabul", "leena@gmail.com", "+77939383839", "travelling")
user3 = User("Hanisha", "Potluri", "Andhra Pradesh", "hanisha@gmail.com", "+82747737478", "coding")

# short description of user
user1.describe_user()
user2.describe_user()
user3.describe_user()

print()  # print a blank line

# greetings to the users
user1.greet_user()
user2.greet_user()
user3.greet_user()