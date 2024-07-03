import getpass
username=input("Enter your username :-")
password=getpass.getpass("Enter your password")
if len(password)<=3:
    print("password is too short")
elif len(password)>8:
    print("Not accepted character exceeds ")
else:
    print(f"welcome\t{username}")
     