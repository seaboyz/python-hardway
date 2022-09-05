def cheese_and_crachers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man ths's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crachers(20, 30)

print("OR, we can use vriables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crachers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crachers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crachers(amount_of_cheese + 100, amount_of_crackers + 1000)
