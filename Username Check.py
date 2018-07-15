# -*- coding: utf-8 -*-
# Answer to CHALLENGE (description after the code)
# Proposed by George Victor

user1 = "Goubi3#"
user2 = "troubi#4"
user3 = "Fou fobi@5"
user4 = "Bi4*"
users = [user1, user2, user3, user4]

def check(user):
    if 4 < len(user) < 11 and any(c.isupper() for c in user) and any(c.isdigit() for c in user) and any(c in "@#*=" for c in user) and all(c != " " for c in user):
        return "PASS"
    else:
        return "FAIL"

n = 0
for u in users:
    n += 1
    print("user", u, ":", check(u))
    
    # Sam wants to select a username to register on a website. The rules for selecting username:
# 1. The minimum length of the username must be 5 characters and the maximum may be 10.
# 2. It should contain at least one letter from A-Z
# 3. It should have at least one digit from 0-9
# 4. It should have at least one character from amongst @#*=
# 5. It should not have any spaces

# Write a program which accepts 4 usernames (one username per line)
# as input and checks whether each of them satisfy the above mentioned conditions.
# If it does, the program should print PASS (in uppercase)  else print FAIL
