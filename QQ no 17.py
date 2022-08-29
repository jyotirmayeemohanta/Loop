# n=int(input("enter a no"))
# i=0
# while i<len(n):
#     if n[i]=="0":
#         print("zero")
#     elif n[i]=="1":
#         print("one")
#     elif n[i]=="2":
#         print("two")
#     elif n[i]=="3":
#         print("three")
#     elif n[i]=="4":
#         print("four")
#     elif n[i]=="5":
#         print("five")
#     elif n[i]=="6":
#         print("six")
#     elif n[i]=="7":
#         print("seven")
#     elif n[i]=="8":
#         print("eight")
#     elif n[i]=="9":
#         print("nine")
#     i=i+1
# from instabot import Bot
# bot=Bot()
# bot.login(username="",password="")

# bot.upload_photo("image.jpg",
# caption="type your caption here")

# bot.follow("elonrmuskk")

# bot.send_message("Hello from codehub",['user1','user2'])

# my_followers=bot.get_user_followers("codehub.py")
# for follower in my_followers:
#     print(follower)
# bot.unfollow_everyone()
from random import *
user_pass=input("Enter your password")
password=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess=""
while(guess !=user_pass):
    guess=""
    for letter in range(len(user_pass)):
        guess_letter=password[randint(0,25)]
        guess=str(guess_letter)+str(guess)
    print(guess)
print("your password is",guess)