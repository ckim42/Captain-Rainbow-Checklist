# Thanks to Drake Vorndran and Victoria Murray for their help

checklist = list()
# checklist.append("Hello")
# print(checklist)
# checklist.append("World")
# print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])
# checklist = ["Hello", "World"]
# checklist[1] = "Cats"
# print(checklist)

def update(index, item):
    checklist[index] = item
# checklist = ["Hello", "World"]
# checklist.pop(1)
# print(checklist)

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        # new print function - twas upgraded
        print("{}{}".format(index, list_item))
        index += 1

def mark_completed(index):
    item = "√" + str(checklist[index])
    update(index, item)

def mark_incomplete(index):
    item = str((checklist[index])[2:])
    update(index, item)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):

    # Create item
    if function_code == "C":
        #Create item in checklist here
        input_item = user_input("Add item: ")
        create(input_item)
        print(str(input_item) + " was added to the list")

    # Read item
    elif function_code == "R":
        #Read item in checklist
        item_index = int(user_input("Index to read: "))
        if item_index > len(checklist) - 1:
            print("Index out of range")
        else:
            read(item_index)

    elif function_code == "U":
        item_index = int(user_input("Index to update: "))
        if item_index > len(checklist) - 1:
            print("Index out of range")
        else:
            item = user_input("Update " + checklist[item_index] + " to: ")
            update(item_index, item)

    elif function_code == "D":
        item_index = int(user_input("Index to destroy: "))
        if item_index > len(checklist) - 1:
            print("Index out of range")
        else:
            checklist.pop(item_index)

    elif function_code == "P":
        #Print all items here
        list_all_items()

    elif function_code == "Q":
        #This is where we want to stop our loop
        running = False
        return running

    else:
        #Catch all
        print("Unknown Option")
    return True

def test():

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    # print(read(1)) problematic because we destroy this same
    list_all_items()

    select("C")
    list_all_items()
    # call fxn w new value
    select("R")
    # view results
    list_all_items()
    #continue until all code is run

# test()

running = True
# selection = 0
while running == True:
    selection = user_input("Press C to add to list, R to read from list, U to update an item, D to destroy an item, P to display list, and Q to quit: ").upper()
    select(selection)
