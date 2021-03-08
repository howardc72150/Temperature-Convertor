# Get data from user and store it in a list, then
# display the most recent three entires nicely.

# Initialise variables
all_calculations = []

# Get five items of data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")
    if get_item == "xxx":
        break
    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("THe list is empty!")
else:
    print()
    print("Full list")
    print(all_calculations)

    # Print items starting at the end of the list
    if len(all_calculations) >= 3:
        print("Most recent 3")
        for item in range(0,3):
            print(all_calculations[len(all_calculations)-item-1])
    else:
        print("Item from newest to oldest")
        for item in all_calculations:
            print(all_calculations[len(all_calculations)-all_calculations.index(item)])