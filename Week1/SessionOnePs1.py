def welcome():
	print("Welcome to The Hundred Acre Wood!")

def greeting(name):
    ans = f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin."
    print(ans)

def print_catchphrase(character):
    if character == "Pooh": 
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":	
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
         print("Sorry! I don't know <character>'s catchphrase!")

def get_item(items, x):
    if (x >= len(items)):
        return None
    return items[x]

def sum_honey(hunny_jars):
    sum = 0
    for jar in hunny_jars:
        sum += jar
    return sum

def doubled(hunny_jars):
    ret = []
    for jar in hunny_jars:
        ret.append(jar * 2)
        # print(jar)
    return ret

def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count+=1
    return count

def print_todo_list(tasks):
    count = 1
    print("Pooh's To Dos:")
    for task in tasks:
        print(f"{count}. " + task)

def can_pair(item_quantities):
    for quantity in item_quantities:
        if (quantity % 2 != 0):
            return False
    return True

def split_haycorns(quantity):
    ret = []
    for i in range(1, quantity+1):
        if (quantity % i == 0):
            ret.append(i)
    return ret

def tiggerfy(s):
    ans = ""
    s = s.lower()
    letters = ["t","i","g","e","r"]
    for c in s:
        if c not in letters:
            ans += c
    return ans
    


if (__name__ == "__main__"):
    s = "suspicerous"
    print(tiggerfy(s))

    s = "Trigger"
    print(tiggerfy(s))

    s = "Hunny"
    print(tiggerfy(s))

    print(sum_honey([12, 7, 31, 5]))

    # quantity = 6
    # print(split_haycorns(quantity))

    # quantity = 1
    # print(split_haycorns(quantity))

    # item_quantities = [2, 4, 6, 8]
    # print(can_pair(item_quantities))

    # item_quantities = [1, 2, 3, 4]
    # print(can_pair(item_quantities))

    # item_quantities = []
    # print(can_pair(item_quantities))

    # tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    # print_todo_list(tasks)

    # tasks = []
    # print_todo_list(tasks)

    # welcome()
    # greeting("Winnie the Pooh")
    # print_catchphrase("Pooh")

    # items = ["piglet", "pooh", "roo", "rabbit"]
    # x = 2
    # print(get_item(items, x))
    # x = 5
    # print(get_item(items, x))

    # hunny_jars = [2, 3, 4, 5]
    # print(sum_honey(hunny_jars))
    # hunny_jars = []
    # print(sum_honey(hunny_jars))

    # hunny_jars = [1, 2, 3]
    # print(doubled(hunny_jars))

    # race_times = [1, 2, 3, 4, 5, 6]
    # threshold = 4
    # print(count_less_than(race_times, threshold))

    # race_times = []
    # threshold = 4
    # print(count_less_than(race_times, threshold))

