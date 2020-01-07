import webbrowser, requests,bs4
username = input("Username: ")

# check if user is on instagram
res = requests.get(f"https://www.instagram.com/{username}/")

if str(res) == "<Response [200]>":
    print("User is on instagram")

# check if user is on twitter
res = requests.get(f"https://www.twitter.com/{username}/")
if str(res) == "<Response [200]>":
    print("User is on twitter")

# check if user is on linkedin
res = requests.get(f"https://www.linkedin.com/in/{username}")
# print(res)
if str(res) == "<Response [999]>":
    print("User is on linkedin")
