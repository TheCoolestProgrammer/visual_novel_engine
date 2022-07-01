from linked_list import linked_list

stages = []
def adding_child(index):
    names = [i.name for i in stages]
    del(names[index])
    while True:
        print("what kind of stages you wanna add to", names[index],"?")
        for i in range(len(names)):
            print(i, names[i])
        print(len(names), "exit")
        choise = input()
        if choise == str(len(names)) or choise == "exit":
            break
        if 0 <= int(choise) < len(names):
            index2 = int(choise)
        elif choise in names:
            index2 = names.index(choise)
        else:
            print("there is no such name/index")
            continue
        if index2 in names[index]:
            print("this stage already connected")
        else:
            names[index].links.append(names[index2])
            print(f"you`ve successfully connect {names[index].name} as a parent and {names[index2].name} as a child")

def customizing(index):
    while True:
        print("what`s you wanna do?")
        print("1. add child(add chd)")
        print("2. delete child(del chd)")
        print("3. remove child(rm chd)")
        print("4. add condition(add con)")
        print("5. delete condition(del con)")
        print("6. exit")
        choise = input()
        if choise == "1" or choise == "add chd":
            adding_child(index)
def customize_menu():
    names = [i.name for i in stages]
    while True:
        if len(names) ==0:
            print("there is no stages")
            break
        print("what kind of stage you wanna customize?")
        for i in range(len(names)):
            print(i, names[i])
        print(len(names), "exit")
        choise = input().lower()
        if choise == str(len(names)) or choise == "exit":
            break
        if choise in names :
            index = names.index(choise)
        elif choise.isdigit() and 0 <= int(choise) < len(names):
            index = int(choise)
        else:
            print("there is no such name/index")
            continue
        customizing(index)
def add_stage():
    print("print name of stage: ", end="")
    name = input()
    stage = linked_list(name)
    stages.append(stage)
while True:
    print("what`s you wanna do?")
    print("1. add stage")
    print("2. customize stage")
    print("3. delete stage")
    print("4. save game")
    choise = input()
    if choise == "1":
        add_stage()
    elif choise == "2":
        customize_menu()
