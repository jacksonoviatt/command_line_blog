import dbcreds
import mariadb
import traceback

def insertBlogPost(username):
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, database=dbcreds.database, port=dbcreds.port)
        cursor = conn.cursor()

        post_content = input("Write your post: ")
        cursor.execute(f"INSERT INTO blog_post(username, content) VALUES('{username}', '{post_content}')")
        conn.commit()

    except:
        print("Error in the DB")
        traceback.print_exc()

    try:
        cursor.close()
    except:
        print("error in the closing cursor")
        traceback.print_exc()

    try:
        conn.close()
    except:
        print("error in the connection closing")
        traceback.print_exc()

def view_blog_posts():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, database=dbcreds.database, port=dbcreds.port)
        cursor = conn.cursor()

        cursor.execute("SELECT username, content FROM blog_post")
        posts = cursor.fetchall()

        for post in posts:
            print(post)

    except:
        print("Error in the DB")
        traceback.print_exc()

    try:
        cursor.close()
    except:
        print("error in the closing cursor")
        traceback.print_exc()

    try:
        conn.close()
    except:
        print("error in the connection closing")
        traceback.print_exc()

