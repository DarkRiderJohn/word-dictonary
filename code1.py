import json
# this json contain 49,537 words

with open("data.json") as f:
    data = json.load(f)


user_input = str.lower(input("Enter the word:"))

if user_input in data:
    for meaning in data[user_input]:
        print(meaning)
else:
    print("Not found")
