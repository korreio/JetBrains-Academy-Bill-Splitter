import random

num_friends: str = input("Enter the number of friends joining (including you):\n")

if not num_friends.isnumeric() or int(num_friends) < 1:
    print("No one is joining for the party")
else:
    # Get Friend Names
    print("Enter the name of every friend (including you), each on a new line:")
    friends_list = [input() for _ in range(int(num_friends))]

    # Get bill value and divide by number of friends
    the_bill = input("Enter the total bill value:\n")

    # Use the Who's Lucky feature?
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n') == "Yes"

    pay_per_friend = round(float(the_bill) / (float(num_friends) - float(lucky)), 2)
    friends_dict = dict.fromkeys(friends_list, pay_per_friend)

    if lucky:  # Select the lucky one and set his bill to zero
        lucky_one = random.choice(friends_list)
        friends_dict[lucky_one] = 0.0
        print(f"{lucky_one} is the lucky one!\n")
    else:
        print("No one is going to be lucky\n")

    print(friends_dict)
