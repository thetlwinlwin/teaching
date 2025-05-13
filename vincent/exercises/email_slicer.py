email = input("Enter Your Email: ").strip()
email_list = email.split("@")
print("Your name is", email_list[0])
print("Your domain is", email_list[1])
