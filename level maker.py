import codecs

from linked_list import linked_list
import pygame
stages = []

def right_input_check(names,choise):
    if (type(choise) == int or(type(choise)== str and choise.isdigit())) and 0 <= int(choise) < len(names):
        index2 = str(choise)
    elif choise in names:
        index2 = str(names.index(choise))
    else:
        print("there is no such name/index")
        return False
    return index2

def adding_child(index):
    names = [i.name for i in stages]
    while True:
        print("what kind of stages you wanna add to", names[index],"?")
        for i in range(len(names)):
            if stages[i] in stages[index].links:
                print(i, names[i],"---connected---")
            else:
                print(i, names[i])
        print(len(names), "exit")
        choise = input()
        if choise.isdigit() and choise == str(len(names)) or choise == "exit":
            break
        index2 = right_input_check(names, choise)
        if index2:
            index2 = int(index2)
            if names[index2] in stages[index].links:
                print("this stage already connected")
            elif names[index2] == stages[index].name:
                print("cannot connet self")
            else:
                stages[index].links.append(stages[index2])
                print(f"you`ve successfully connect {names[index]} as a parent and {names[index2]} as a child")
def delete_child(index):
    while True:
        children = stages[index].links
        if len(children)==0:
            print("stage hasn`t children")
            break
        names = [i.name for i in children]
        print("what kind of child you wanna delete?")
        for i in range(len(names)):
            print(i, names[i])
        print(len(names), "exit")
        choise = input()
        if choise == str(len(names)) or choise == "exit":
            break
        index2 = right_input_check(names, choise)
        if index2:
            index2 = int(index2)
            if children[index2] in stages[index].links:
                to_del = stages[index].links[index2]
                del (stages[index].links[index2])
                print(f"you`ve sucessfully disconnected {to_del.name} from {stages[index].name}")
            else:
                print("wrong data")
def remove_child(index):
    while True:
        names = [i for i in stages[index].links]
        if len(names)<2:
            print("too low children")
            break
        print("choose child")
        for i in range(len(names)):
            print(i, names[i].name)
        print(len(names),"exit")
        choise = input()
        if choise == str(len(names)) or choise == "exit":
            break
        index2 = right_input_check(names,choise)
        if index2:
            index2 = int(index2)
            while True:
                print("print position or exit")
                pos = input()
                if pos.isdigit():
                    pos = int(pos)
                    if 0<= pos < len(stages[index].links):
                        stages[index].links.insert(pos,stages[index].links[index2])
                        if pos > index2:
                            del(stages[index].links[index2])
                        else:
                            del(stages[index].links[index2+1])
                        print(f"you`ve sucessfully remove child on pos {pos}")
                        break
                    else:
                        print("wrong position")
                else:
                    if pos == "exit":
                        break
                    print("wrong position")

def add_condition(index):
    names = [i.name for i in stages[index].links]
    while True:
        if len(stages[index].conditions) == len(stages[index].links):
            print("every conditions to childrens already was added")
            break
        print("print name of child stage you need to connect")
        for i in range(len(names)):
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
                        print("you`ve sucessfully added condition")
                    else:
                        stages[index].conditions[stage_child] = [text,button]
                        print("you`ve sucessfully added condition")
                    print(stages[index].conditions)
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
                print("you`ve sucessfully deleted condition")
            else:
                print("you`ve sucessfully deleted condition")
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
            customizing(int(index))
def add_stage():
    while True:
        print("print name of stage or exit")
        name = input()
        if name == "exit":
            break
        stage = linked_list(name)
        stages.append(stage)
def delete_stage():
    while True:
        names = [i.name for i in stages]
        if len(names) == 0:
            print("nothing to delete")
            break
        print("what kind of stages you wanna delete?")
        for i in range(len(names)):
            print(i, names[i])
        print(len(names),"exit")
        stage = input()
        if stage == "exit" or int(stage) ==len(names):
            break
        if stage in names or (stage.isdigit() and 0 <= int(stage) < len(names)):
            if stage.isdigit():
                del(stages[int(stage)])
            else:
                del(stages[stages.index(stage)])
        else:
            print("wrong data")

def save_project():
    print("print path with name of your project")
    print("(.py in the end)")
    filename = input()
    while True:
        print("print name of start stage")
        stage = input()
        stage2 = ""
        for i in stages:
            if i.name == stage:
                stage2 = stage
                break
        if stage2:
            print("success")
            break
        else:
            print("print right name")

    with codecs.open(filename,"w") as file:
        file.write("level = [")
        for i in stages:
            # links =[j.name for j in i.links]
            # special_links ="["+  ", ".join(links)+"]"
            name = i.name
            image = i.image
            # conditions ="["+ ", ".join(i.conditions)+"]"
            file.write("{")
            file.write(f"'{name}': ['{name}', '{image}', ")
            file.write("{")
            for j in i.conditions.keys():
                # file.write("{")
                file.write(f"'{j}': [")
                print(i.conditions[j][0])
                file.write(f"'{i.conditions[j][0]}', {i.conditions[j][1]}")
                file.write("], ")
            file.write("}, ")

            file.write("[")
            for j in i.links:
                file.write(f"'{j.name}', ")
            file.write("]")
            file.write("]},\n")
        file.write("]")
    print(f"project saved as {filename}")
while True:
    print("what`s you wanna do?")
    print("1. add stage")
    print("2. customize stage")
    print("3. delete stage")
    print("4. save project")
    choise = input()
    if choise == "1":
        add_stage()
    elif choise == "2":
        customize_menu()
    elif choise == "3":
        delete_stage()
    elif choise == "4":
        save_project()