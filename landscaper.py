## Array of Tools
tools = [
    {"name": "Teeth", "income":1, "price": 0},
    {"name": "Rusty Scissors", "income":5, "price": 5},
    {"name": "Push Mower", "income":50, "price": 25},
    {"name": "Fancy Mower", "income":100, "price": 250},
    {"name": "Starving Students", "income":250, "price": 500},
]

## Game State
tools_used = []
current_tool = "Teeth"
money = 0


## start function should
# - print a message introducing the game and options
# - take input from the user (1 = mow 2 = buy)
# - return that input
# This function does NOT have a test
print("Welcome to Landscaper.")
def start():
    
    user_Answer = input("Would you like to mow or buy?. Enter 1 for mow, enter 2 for buy : ")
    if user_Answer.isalpha():
            print("You must use numbers 1 or 2")
    else:
        if int(user_Answer) == 1:
            return "mow"
        elif int(user_Answer) == 2:
            return "buy"
        else:
            return "improper input"
 
## selection function should
# - if user input is 1, run the mow function
# def mow():

## upgrade function
# - check to see if money is enough to buy the next tool
# - if so upgrades tool by incrementing current_tool
# - if not, print message saying money isn't enough
def upgrade():
    global current_tool
    global money
    if money > 0:
        answer = int(input("""What would you like to buy?:
        1. Rusty Scissors:
        2. Push Mower:
        3. Fancy Mower:
        4. Starving Students:
        Input: """))
        # Testing
        print(current_tool)
        # ///////
        if answer == 1 and money >= tools[1]["price"]:
            if tools[1]['name'] in tools_used:
                print("""
                You have this tool already
                """)
            elif current_tool == "Teeth":
                current_tool = tools[1]['name']
                tools_used.append(current_tool)
                money -= tools[1]["price"]
            else:
                print(""" 
                You can't skip a step when it comes to the tools you buy.
                You must buy the tools in order according to price.
                """)
        elif answer == 2 and money >= tools[2]["price"]:
            if tools[2]['name'] in tools_used:
                print("You have this tool already")
            elif current_tool == "Rusty Scissors":
                current_tool = tools[2]['name']
                tools_used.append(current_tool)
                print(tools_used)
                money -= tools[2]["price"]
                current_tool = tools[2]["name"]
            else:
                print(""" 
                You can't skip a step when it comes to the tools you buy.
                You must buy the tools in order according to price.
                """)
        elif answer == 3 and money >= tools[3]["price"]:
            if tools[3]['name'] in tools_used:
                print("You have this tool already")
            elif current_tool == "Push Mower":
                current_tool = tools[3]['name']
                tools_used.append(current_tool)
                print(tools_used)
                money -= tools[3]["price"]
            else:
                print(""" 
                You can't skip a step when it comes to the tools you buy.
                You must buy the tools in order according to price.
                """)
        elif answer == 4 and money >= tools[4]["price"]:
            if tools[4]['name'] in tools_used:
                print("You have this tool already")
            elif current_tool == "Fancy Mower":
                current_tool = tools[4]['name']
                tools_used.append(current_tool)
                print(tools_used)
                money -= tools[4]["price"]
            else:
                print(""" 
                You can't skip a step when it comes to the tools you buy.
                You must buy the tools in order according to price.
                """)
        else:
            print("""
            You dont have the funds for that tool.
            
            """)
    else:
        print("Your short on funds")
    # Testing
    print(current_tool)
    # ///////////
    return 0

# - if user input is 2, run the upgrade function
# - if anything else, text warning
def selection(select):
    if select == "mow":
        mow()
    elif select == "buy":
        upgrade()
    else:
        print("""
        wrong input.
        """)
    return select


## mow function
# to refer to global variables look up global keyword
# - should up income based on current_tool & tools list
# - print message
def mow():
    global money
    if current_tool == "Teeth":
        money += 1
    elif current_tool == "Rusty Scissors":
        money += 5
    elif current_tool == "Push Mower":
        money += 50
    elif current_tool == "Fancy Mower":
        money += 100
    elif current_tool == "Starving Students":
        money += 250
    return 0


## the win_conditions functionss
# check if the current tool is the team and money is 1000
# If true, print a win message then return true
# If false, print the players money total and tool and run game_loop()
def win_conditions():
    if current_tool == "Starving Students" and money >= 1000:
        print("You won!")
        return True

    else:
        print(f"""
        You have {money} dollars and are currently using your {current_tool}
        """)
        game_loop()

    return 0



## GAME LOOP

def game_loop():
    ## get users input
    select = start()
    ## run a particular action
    selection(select)
    ## check win conditions and start again
    win_conditions()

game_loop()