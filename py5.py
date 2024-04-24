def get_usernames(emails):
    usernames = []
    for email in emails:
        if "@" in email:
            username = email.split("@")[0]
            usernames.append(username)
    return usernames

# Test the function
email_list = ["nakomegi@gmail.com", "john.doe@example.com", "jane_smith@yahoo.com", "bob123@outlook.com"]
usernames = get_usernames(email_list)
print("List of email addresses:", email_list)
print("List of usernames:", usernames)

