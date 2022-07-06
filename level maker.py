from linked_list import linked_list
import pygame
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

def add_condition(index):
    names = [i.name for i in stages]
    while True:
        if len(stages[index].conditions) == len(stages[index].links):
            print("every conditions to childrens already was added")
            break
        print("print name of child stage you need to connect")
        for i in range(len(names)):
            if names[i] in stages[index].conditions:
                print(i,names[i],"--connected--")
            else:
                print(i,names[i])
        print(len(names), "exit")
        stage_child = input()
        if int(stage_child) ==len(names) or stage_child == "exit":
            break
        if stage_child in names or (stage_child.isdigit() and 0<=int(stage_child) <len(names)):
            if stage_child in stages[index].conditions or (stage_child.isdigit() and  names[int(stage_child)] in stages[index].conditions):
                print("already connected")
                continue
            while True:
                print("print text for condition")
                text = input()
                print("print number of keyboard(1-9) for condition")
                button = input()
                if button.isdigit() and 0< int(button) <=9:
                    if button == "1":
                        button = pygame.K_1
                    elif button == "2":
                        button = pygame.K_2
                    elif button == "3":
                        button = pygame.K_3
                    elif button == "4":
                        button = pygame.K_4
                    elif button == "5":
                        button = pygame.K_5
                    elif button == "6":
                        button = pygame.K_6
                    elif button == "7":
                        button = pygame.K_7
                    elif button == "8":
                        button = pygame.K_8
                    elif button == "9":
                        button = pygame.K_9
                    if stage_child.isdigit():
                        stages[index].conditions[names[int(stage_child)]] = [text,button]
                    else:
                        stages[index].conditions[stage_child] = [text,button]
                    break
                else:
                    print("this key connot be use for choosing condition")
        else:
            break

def delete_conditions(index):
    while True:
        conditions = [i for i in stages[index].conditions.keys()]
        if len(stages[index].conditions) == 0:
            print("nothing to delete")
            break
        print("print name of child stage you need to delete")
        for i in range(len(conditions)):
            print(i, conditions[i])
        print(len(conditions), "exit")
        stage_child = input()
        if int(stage_child) == len(conditions) or stage_child == "exit":
            break
        if stage_child in conditions or (stage_child.isdigit() and 0 <= int(stage_child) < len(conditions)):
            if stage_child.isdigit():
                del(stages[index].conditions[conditions[int(stage_child)]])
            else:
                del(stages[index].conditions[stage_child])
        else:
            print("wrong stage")

def add_background(index):
    print("print name and path to image or exit")
    print("*note: path must be from folder where is level_maker.py !")
    path = input()
    if path == exit:
        return 0
    stages[index].image = path
def customizing(index):
    while True:
        print("what`s you wanna do?")
        print("1. add child(add chd)") #done
        print("2. delete child(del chd)") #done
        print("3. remove child(rm chd)") #done
        print("4. add condition(add con)") #done
        print("5. delete condition(del con)") #done
        print("6. add background(add bg)") #done
        print("7. exit") #done
        choise = input()
        if choise == "1" or choise == "add chd":
            adding_child(index)
        elif choise == "2" or choise == "del chd":
            delete_child(index)
        elif choise == "3" or choise == "rm chd":
            remove_child(index)
        elif choise == "4" or choise == "add con":
            add_condition(index)
        elif choise == "5" or choise == "del con":
            delete_conditions(index)
        elif choise == "6" or choise == "add bg":
            add_background(index)
        elif choise == "7" or choise == "exit":
            break
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
        index = right_input_check(names,choise)
        if index:
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
