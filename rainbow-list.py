checklist = ["red", "orange", "yellow"]

print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

# lists all items in checklist with their indexes
def list_all_items():
    index = 0
    print("in my list I have:")
    for list_item in checklist:
        num = str(index)

        print(list_item, " : ", num)
        index += 1
    print("and that's it!")

def user_input(prompt):
    user_input = input(prompt)
    return user_input

# runs one of the above functions based on what function_code it gets
def select(function_code):
    # Create
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))
        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    # Update
    elif function_code == "U":
        input_index = int(user_input("Which index would you like to update? "))
        input_item = user_input("What would you like to update it with? ")
        update(input_index, input_item)

    # Destroy
    elif function_code == "D":
        index = int(user_input("At which index is the item you would like to delete? "))
        destroy(index)

    # List all items including indexes
    elif function_code == "P":
        list_all_items()

    # return false so it ultimately sets the running variable down in the while loop to false
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("INVALID INPUT. Your options are: \n- C to add to list\n- R to read in item from list\n- U to update an item\n- D to delete an item\n- P to display entire list\nWhat will you do? ")
        return True


# LOOP
# stops the instructions being shown every time
show_instructions = True
running = True
while running is not False:
    if show_instructions == True:
        show_instructions = False
        print(show_instructions)
        selection = user_input(
        "Options:\n- C to add to list\n- R to read in item from list\n- U to update an item\n- D to delete an item\n- P to display entire list\nWhat will you do?\n> ")
    else:
        selection = user_input("> ")
    running = select(selection)


# tests
def test():
    select("C")
    select("R")
    select("P")
    list_all_items()
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    print(read(1))

# create("blue")
# create("red")
#
# print(checklist)
# test()
