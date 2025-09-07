all_users = []

while True:
    name1 = input ("Name: ")
    age1 = int(input ("Age: "))
    languages_yes = input ("Do you speak any other languages? ")
    languages_list = []
    if languages_yes.lower() == "yes":
        how_many_languages = int(input ("How many other languages do you speak? "))
        for i in range(how_many_languages):
            language1 = input ("What other language do you speak? ")
            languages_list.append(language1)
            print("Wow! " + language1 + " is a great language!")
    else:
        languages_list.append("None")

    user1 = {
        "name1": name1,
        "age1": age1,
        "languages1": languages_list
    }
    print("Hi. Welcome to this program," + user1["name1"] + ".")
    print("Languages you speak:", ", ".join(user1["languages1"]))
    if user1["languages1"] == ["None"]:
        learn_language = input("Would you like to learn a new language? ")
        if learn_language.lower() == "yes":
            new_language = input("Which language would you like to learn? ")
            print(f"Great! {new_language} is a wonderful language to learn.")

    if user1["age1"] < 13:
        print("Unfortunately, you are not old enough to sit in the front seat of a car, vote, or rent a car")
    elif user1["age1"] >= 13 and user1["age1"] < 18:
        print("You can sit in the front seat of a car, but you cannot vote.")
    elif user1["age1"] >= 18 and user1["age1"] < 25:
        print("You can vote, but you cannot rent a car.")
    elif user1["age1"] >= 25 and user1["age1"] < 35:
        print("You can do whatever you want.")
    elif user1["age1"] >= 35:
        print("Old")
    else:
        print("Error")

    all_users.append(user1)
    another = input("Would another user like to enter their information? (yes/no): ")
    if another.lower() != "yes":
        break

print("\nAll user data:")
for user in all_users:
    print(user)
