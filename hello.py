import datetime
import config

def say_hello(name):
   print(f"Hello, {name} from {config.APP_NAME}!")

def greet_user():
   name = input("Please enter your name: ")
   say_hello(name)

def say_hello(name):
   now = datetime.datetime.now() # เพิ่มบรรทัดนี้
   print(f"Hello, {name} from {config.APP_NAME}!")
   print(f"Today is {now.strftime('%Y-%m-%d')}.") # เพิ่มบรรทัดนี้


if __name__ == "__main__":
   greet_user()
