from linked_list import linked_list

stages = []

def right_input_check(names,choise):
    if choise.isdigit() and 0 <= int(choise) < len(names):
        index2 = int(choise)
    elif choise in names:
        index2 = names.index(choise)
    else:
        print("there is no such name/index")
        return False
    return index2

def adding_child(index):
    names = [i.name for i in stages]
    while True:
        print("what kind of stages you wanna add to", names[index],"?")
        for i in range(len(names)):
            if i in names[index].links:
                print(i, names[i],"---connected---")
            else:
                print(i, names[i])
        print(len(names), "exit")
        choise = input()
        if choise.isdigit() and choise == str(len(names)) or choise == "exit":
            break
        index2 = right_input_check(names, index)
        if index2:
            if index2 in names[index]:
                print("this stage already connected")
            else:
                names[index].links.append(names[index2])
                print(f"you`ve successfully connect {names[index].name} as a parent and {names[index2].name} as a child")

def delete_child(index):
    while True:
        children = stages[index].links
        if len(children)==0:
            print("stage hasn`t children")
            break
        names = [i.name for i in children]
        print("what kind of child you wanna delete?")
        for i in range(len(names)):
            if i in names[index].links:
                print(i, names[i],"---connected---")
            else:
                print(i, names[i])
        print(len(names), "exit")
        choise = input()
        if choise == str(len(names)) or choise == "exit":
            break
        index2 = right_input_check(names, index)
        if index2:
            if index2 not in names[index]:
                print("this stage already disconnected")
            else:
                to_del =stages[index].links[index2]
                del (stages[index].links[index2])
                print(f"you`ve sucessfully disconnected {to_del.name} from {stages[index].name}")

def remove_child(index):
    while True:
        names = [i.name for i in stages]
        if len(names)<2:
            print("too low children")
            break
        print("choose firt child")
        for i in range(len(names)):
            print(i, names[i])
        print(len(names),"exit")
        choise = input()
        if choise == str(len(names)) or choise == "exit":
            break
        index2 = right_input_check(names,index)
        if index2:
            while True:
                print("print position or -1 to exit")
                pos = input()
                if pos.isdigit():
                    pos = int(pos)
                    if 0<= pos <=len(names)-1:
                        stages[index].links.insert(pos,stages[index].links[index2])
                        del(stages[index].links[index2+1])
                        print(f"you`ve sucessfully remove child {stages[index].links[pos].name} on pos {pos}")
                        break
                    else:
                        if pos == -1:
                            break
                        else:
                            print("wrong position")
                else:
                    print("wrong position")

def customizing(index):
    while True:
        print("what`s you wanna do?")
        print("1. add child(add chd)") #done
        print("2. delete child(del chd)") #done
        print("3. remove child(rm chd)") #done
        print("4. add condition(add con)")
        print("5. delete condition(del con)")
        print("6. add background(add bg)")
        print("7. exit")
        choise = input()
        if choise == "1" or choise == "add chd":
            adding_child(index)
        elif choise == "2" or choise == "del chd":
            delete_child(index)
        elif choise == "3" or choise == "rm chd":
            remove_child(index)
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
