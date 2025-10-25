# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = "Hey harry, how are you doing today?everything good?"
if ("Harry".lower() in post.lower()):
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")