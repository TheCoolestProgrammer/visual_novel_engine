import pygame, random, copy
from linked_list import linked_list
from levels import test

pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
process_running = True
fps = 200

choise_buttons = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]

stages = []

def adapter(level):
    # making objects from dictionary
    for i in level:
        for j in i.keys():
            stage = linked_list(i[j][0])
            stage.image = i[j][1]
            stage.conditions = i[j][2]
            stage.links = i[j][3]
            stages.append(stage)
    # changing links names on objects
    for i in range(len(stages)):
        for j in range(len(stages[i].links)):
            for k in range(len(stages)):
                if stages[i].links[j] == stages[k].name:
                    stages[i].links[j] = stages[k]
                    break
    #changing conditions

    for i in range(len(stages)):
        changes = dict()
        for j in stages[i].conditions.keys():
            for k in range(len(stages)):
                if stages[k].name ==j:
                    # stages[i].conditions[stages[k]] = stages[i].conditions[j]
                    # changes[stages[k]] = stages[i].conditions[j]
                    # changes.append([stages[i],{}])
                    changes[stages[k]] = stages[i].conditions[j]
        stages[i].conditions = changes
    print("file loading is done!")
def change_stage(parent,choise=0):
    return parent.links[choise]

def drawing(now_frame):
    screen.fill((0, 0, 0))
    background = pygame.image.load(now_frame.image)
    pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(background,(0,0))
    pygame.display.update()

def events_check():
    global process_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False

def is_active_key_pressed():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                return True
    return False

def choose():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            return event.key
def choise_check(choise, now_stage):
    if choise > len(now_stage)-1:
        return len(now_stage)-1
    else:
        conditions = now_stage.conditions
        cond_keys = conditions.keys()
        if choise == pygame.K_1:
            if 0 in cond_keys:
                return conditions[0]
        elif choise == pygame.K_2:
            if 1 in cond_keys:
                return conditions[1]
        elif choise == pygame.K_3:
            if 2 in cond_keys:
                return conditions[2]
        elif choise == pygame.K_4:
            if 3 in cond_keys:
                return conditions[3]
        elif choise == pygame.K_5:
            if 4 in cond_keys:
                return conditions[4]
        elif choise == pygame.K_6:
            if 5 in cond_keys:
                return conditions[5]
        elif choise == pygame.K_7:
            if 6 in cond_keys:
                return conditions[6]
        elif choise == pygame.K_8:
            if 7 in cond_keys:
                return conditions[7]
        elif choise == pygame.K_9:
            if 8 in cond_keys:
                return conditions[8]
def mainloop():
    level = test.level
    adapter(level)
    now_stage = stages[0]
    while process_running:
        events_check()
        # if there is choise
        if len(now_stage.links)>1:
            choise = choose()
            if choise:
                if choise in choise_buttons:
                    choise = choise_check(choise,now_stage)
                    change_stage(now_stage,choise)
                else:
                    if is_active_key_pressed():
                        change_stage(now_stage)
        # if there isn`t choise
        else:
            if is_active_key_pressed():
                change_stage(now_stage)
        drawing(now_stage)
        print(now_stage)
        pygame.time.delay(fps)


if __name__ == '__main__':
    mainloop()