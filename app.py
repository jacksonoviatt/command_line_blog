import dbcreds
import mariadb
import traceback
import sqlfunctions as sql


current_user = input("Please enter your username: ")
print(f"Welcome {current_user}")
while(True):
    print("Would you like to: 1 - Make a post, 2 - View posts, 3 - Exit") 

    user_choice = int(input("1 or 2 or 3: "))
    if(user_choice == 1):
        sql.insertBlogPost(current_user)
    elif(user_choice == 2):
        sql.view_blog_posts()
    elif(user_choice == 3):
        print(f"See you next time {current_user}")
        break
    else:
        print("please enter a valid key")
