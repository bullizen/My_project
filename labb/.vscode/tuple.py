# Create a sample collection
users = {"Éléonore": "inactive", "Hans": "active", "景太郎": "active"}

c = users.copy()

print("fore users", users, id(users))
print("fore c", c, id(c))

i = c.items()

print("i", i)

mintupel = ("Kent", "passive")

mintupel_namn, mintupel_status = mintupel


print(mintupel, type(mintupel))

for user, status in i:
    if status == "inactive":
        del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == "active":
#         active_users[user] = status