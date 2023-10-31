from ultralytics import YOLO
from time import sleep
import win32gui
import mss
import numpy as np
import cv2
import random
import csv
from datetime import datetime, timedelta
import os
import subprocess
from random import uniform

import utility_modules.move_ctype as cici
from utility_modules.resets import reset_dung, sell_loot, change_action, logout, grp_creation
from utility_modules.calculus import calculate_vector_magnitude, calculate_angle_north
from utility_modules.capture import capture_mode, crop


fhd_route_dict = {
'first_pull': [[[727, 141], 8, None, None],# left
 [[706, 149], 8, None, None], #right
 [[708, 167], 8, None, None], #align to big
 [[677, 203], 20, None, None], #big
 [[692, 245], 8, None, None], #left
 [[649, 242], 8, None, None], #right1
 [[647, 272], 8, None, None], #right2
 [[671, 287], 10, None, None], #left2
 [[656, 328], 6, None, None], #stairs
 [[667, 341], 8, None, None], #behind
 [[655, 333], 8, None, 1], #behind
 [[662, 315], 8, None, None]
 ], 

'boss1_pull': [[[658, 305], 4, None, None],#align stairs
 [[662, 325], 2, None, None],
 [[677, 340], 4, 135, None],
 [[689, 329], 8, 40, None],
 [[715, 305], 8, None, None],
 [[768, 261], 8, None, None],
 [[778, 217], 10, None, None],
 [[762, 187], 8, None, None],
 #[[743, 221], 8, None, None],
 [[718, 233], 6, None, None], #shooter
 [[721, 268], 8, None, None], #align pillar
 [[702, 278], 5, None, None], #behind
 
 ],

'boss1_TO_rp':[ #[[479, 301], 5, None, None], #uppper repos
 #[[714, 205], 10, None, None], #close to jump
 #[[690, 212], 10, None, None], #jumped off
 [[706, 289], 6, None, None], # up repos
 [[679, 262], 8, None, None], # jump

 #[[670, 262], 6, None, None], # align with brdge
 [[648, 279], 2, None, None], #enter brige
 [[610, 308], 10, 225, None], #1 bridge
 [[560, 346], 10, None, None], #2 bridge
 [[494, 397], 8, None, None], #end of bridge #################
 [[480, 407], 5, None, None], #out of bridge
 [[444, 412], 8, None, None], #right drunk
 #[[457, 443], 10, None, None], #left drunk1
 [[444, 460], 10, None, None], #left drunk2
 [[400, 477], 8, None, None], #left drunk3
 [[375, 439], 8, None, None], #center 
 [[337, 439], 5, None, None], #lefty
 [[315, 427], 6, None, None], #pack to right
 [[302, 434], 4, None, None], #stairs ###
 #[[280, 432], 7, None, None], #center to last
 [[248, 427], 5, None, None],# last

 [[247, 420], 3, None, None], ##align jump
 [[262, 396], 8, None, None], # jump
 [[285, 397], 12, None, None], # 1patrol
 [[310, 367], 8, None, None], # patrol
 [[297, 357], 4, None, None], #align harpoon
 [[235, 339], 12, None, None] #run harpoon
 ],

'boss2_TO_boss3':[ 
 [[251, 348], 8, None, None], #close to jump
 [[177, 362], 8, None, None], #biqmmboi
 [[170, 396], 6, None, None], # right caster
 [[208, 395], 5, None, None], #left caster
 ],

'RETURN': [
 [[204, 400], 6, None, None], #center
 #[[216, 378], 8, None, None], #align to road
 [[235, 356], 10, None, None], #jumpoff to road

 [[346, 356], 8, None, None], #2boss
 [[402, 435], 8, None, None], #rp
 [[470, 415], 3, None, None], #bridge align
 [[489, 401], 3, None, None], #onbridge
 [[534, 366], 10, None, None], #br1
 [[593, 320], 10, None, None], #br2
 [[654, 274], 10, None, None], #brout
 [[676, 216], 8, None, None], #prewoods
 [[703, 172], 5, None, None], #woods
 [[720, 108], 4, None, None], #portal align
 [[743, 81], 6, None, None],
 [[750, 72], 4, None, None],
 ]
}


ID = "Habibati_WORKER666"




def loginer(creds):

    def start_game(shortcut_name):

        script_path = os.path.abspath(__file__)
        shortcut_path = os.path.join(os.path.dirname(script_path), f"{shortcut_name}.lnk")

        # Get the target file path from the shortcut
        target_file_path = subprocess.check_output(['powershell', '(New-Object -ComObject WScript.Shell).CreateShortcut("{}").TargetPath'.format(shortcut_path)]).decode().strip()

        # Check if the target file exists
        if os.path.exists(target_file_path):
            # Execute the target file
            subprocess.Popen([target_file_path])
        else:
            print("Target file does not exist.")

    def login(creds):
        login = creds[0]
        password = creds[1]
        sleep(1)


        start_game("game")
        sleep(20)
        
        try:
            # Find the window by its title
            window_title = "World of Warcraft"
            hwnd = win32gui.FindWindow(None, window_title)

            # Set the window focus
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print(f'during login happened: {e} ')
            while True:
                sleep(600)


        print('started game')

        cici.type_string(login)

        uniform(0.4,2)
        cici.press_key('tab')
        uniform(0.2,1)

        cici.type_string(password)

        uniform(0.7,2)
        cici.press_key('enter')

        sleep(15)
        cici.press_key('enter')

    def checker():

        while True:
            infobox = capture_mode('infobox')
            if sum(infobox[195,390]) == 0:
                print('we logged in')
                break
            else:
                print('not logged in atm')
                sleep(5)

    

    login(creds)
    checker()

def freehold_farmer(to_run):
    model_LOCATION = YOLO('instruments\\LOCATION_FHD_NORESIZE_3.pt')
    model_LOCATION.to('cuda')
    model_MARROW = YOLO('instruments\\ARROW_MAP_SMALL3.pt')
    model_MARROW.to('cuda')

    model_TARGET = YOLO('instruments\\TARGET_RADAR5.pt')
    model_TARGET.to('cuda')
    model_RARROW = YOLO('instruments\\RARROW_SMALL5.pt')
    model_RARROW.to('cuda')

    def write_to_csv(data, csv_name):
        with open(csv_name, 'a', newline='') as file:
            file.write(f'{data}\n')

    def clear_file(csv_name):
        with open(csv_name, 'w') as file:
            pass
            
    def travel(key, cp_list,model_LOCATION, model_MARROW):
        def actions(state_input):
            match state_input:
                case 0 | 1:
                    if abs(player_angle - cp_angle) > 6:
                        mouse_moves = cici.calculate_rotation_direction(player_angle, cp_angle)
                        for index, move in enumerate(mouse_moves):
                            cici.move_mouse_steps(960 + move, 540)
                            sleep(0.04)

                        cici.gas(distance, 22.5)
                    else:
                        cici.gas(distance, 22.5)

                case 1:
                    if abs(player_angle - cp_angle) > 6:
                        mouse_moves = cici.calculate_rotation_direction(player_angle, cp_angle)
                        for index, move in enumerate(mouse_moves):
                            cici.move_mouse_steps(960 + move, 540)
                            sleep(0.04)
                        cici.press_key('a',0.2)
                        cici.gas(distance, 22.5)
                    else:
                        cici.press_key('a',0.2)
                        cici.gas(distance, 22.5)
                case 2:
                    print("debug1")
                    if abs(player_angle - cp_angle) > 6:

                        mouse_moves = cici.calculate_rotation_direction(player_angle, cp_angle)

                        for index, move in enumerate(mouse_moves):
                            cici.move_mouse_steps(960 + move, 540)
                            sleep(0.04)

                        cici.keybd_down('w')
                        cici.press_key('space')
                        sleep(distance / 22.5)
                        cici.keybd_up('w')

                    else:
                        cici.keybd_down('w')
                        cici.press_key('space')
                        sleep(distance / 22.5)
                        cici.keybd_up('w')

                case 3:
                    print("debug2")
                    cici.press_key(random.choice(['a', 'd']), random.uniform(0.6, 0.9))
                    cici.press_key('w ', random.uniform(0.4, 0.6))

                    debug = 0

        n_checkpoints = 0
        distance_old = 0
        timeouter = 0
        debug = 0


        cici.press_key('c')
        
        cici.press_key('m')
        sleep(0.4)
        cici.press_key('m')
        sleep(0.4)

        infobox = capture_mode('infobox')
        combat_B, _, _ = infobox[50, 350]
        dung_B, dung_G, dung_R = infobox[150,350]
        
        if dung_B == 255:
            print('we arent in dung')
            return
        else:
            print("we in dung")

        need_new_SCT = True

        change_action('runner')

        while True:
            cici.press_key('c')
            cici.move_cursor_steps(960, 540)

            infobox = capture_mode('infobox')
            death_B, death_G, _ = infobox[150, 50]

            if death_G == 255:
                cici.press_key('9')
            if death_B == 255:
                cici.move_cursor_steps(900, 150)
                cici.press_left_button()
                cici.release_left_button()

                raise ValueError('dead')

            checkpoint = cp_list[n_checkpoints]
            required_distance = checkpoint[1]

            if timeouter == 0:
                required_timeout = checkpoint[3]
            else:
                required_timeout = 0

            if required_timeout:
                print('sslleeeeppin')
                sleep(required_timeout)
                timeouter += 1

            if need_new_SCT:
                MAP_SCT = False
                checkpoint_coords = checkpoint[0]
                required_distance = checkpoint[1]
                required_angle = checkpoint[2]
                print(f"predicting for cp{checkpoint_coords, required_distance, required_angle}")
                
                try:
                    while not MAP_SCT:
                        MAP = capture_mode('map')
                        MAP_B, MAP_G, MAP_R = MAP[200, 370]
                        if (MAP_B, MAP_G, MAP_R) == (85, 120, 77):
                            print('we in map we good')
                            MAP_SCT = True
                        elif (MAP_B, MAP_G, MAP_R) == (123, 22, 66):
                            print('we not in map, extra M press')
                            cici.press_key('m')

                    results_LOCATION = model_LOCATION.predict(MAP)
                    boxes = results_LOCATION[0].boxes

                    if boxes:
                        box = boxes.xyxy[0].tolist()
                        location = [round((box[0] + box[2]) / 2), round((box[1] + box[3]) / 2)]
                        print(f'HERE {location}')

                        MARROW = crop(MAP, 'marrow', location)

                        results_ARROW = model_MARROW.predict(MARROW)
                        boxes, keypoints = results_ARROW[0].boxes, results_ARROW[0].keypoints


                        if boxes:
                            box = boxes.xyxy[0].tolist()
                            position = [((box[0] + box[2]) / 2), (box[1] + box[3]) / 2]
                            pointer = keypoints.xy.tolist()[0][0]
                            vector_player = [pointer[0] - position[0], pointer[1] - position[1]]
                            magnitude_player = calculate_vector_magnitude(vector_player)
                            vector_north = [0, vector_player[1] - magnitude_player]
                            player_angle = round(calculate_angle_north(vector_player, vector_north))

                            vector_cp = [checkpoint_coords[0] - location[0], checkpoint_coords[1] - location[1]]
                            cp_angle = round(calculate_angle_north(vector_cp, vector_north))

                            distance = round(abs(checkpoint_coords[0] - location[0]) + abs(checkpoint_coords[1] - location[1]))
                            if distance > 200:
                                print(f"wrong pred, {distance}")
                                cici.press_key('w', 0.2)
                                cici.press_key('d', 0.2)
                                
                                continue

                        else:

                            print('ahd to use else1')
                            distance = 10
                            cp_angle = 20
                            player_angle = 10
                    else:
      
                        print('ahd to use else2')
                        distance = 10
                        cp_angle = 20
                        player_angle = 10

                except Exception as e:
                    #sleep(10)
                    print(f'failed in pred map: {e}')
                    distance = 10
                    cp_angle = 20
                    player_angle = 10
                
            else:
                checkpoint_coords = checkpoint[0]
                required_angle = checkpoint[2]
                print(f"using old predict for new cp{checkpoint_coords, required_distance, required_angle}")

                location, vector_player,vector_north, player_angle = player_data_old[0], player_data_old[1], player_data_old[2], player_data_old[3]
                
                vector_cp = [checkpoint_coords[0] - location[0], checkpoint_coords[1] - location[1]]
                cp_angle = round(calculate_angle_north(vector_cp, vector_north))
                distance = round(abs(checkpoint_coords[0] - location[0]) + abs(checkpoint_coords[1] - location[1]))




            if distance < required_distance:
                n_checkpoints += 1
                timeouter = 0
                need_new_SCT = False
                debug = 0
                player_data_old = (location, vector_player,vector_north, player_angle)

                if n_checkpoints == len(cp_list):
                    print('finished')
                    break
                continue

            if abs(distance - distance_old) < 2:
                debug += 1
                if debug == 3:
                    n_checkpoints -= 1

            else:
                debug = 0

            actions(debug)
            distance_old = distance
            need_new_SCT = True

            if n_checkpoints < 0:

                print("entered n_cps")
                match key:
                    case 'boss1_TO_rp':

                        n_checkpoints = 2
                        key = 'tried_force'
                        continue

                    case 'tried_force':
                        print(f'failed force key:{key}')
                        raise IndexError('checkps')

                    case _:
                        print(f'idk watudu, key: {key}')
                        raise IndexError('checkps')
                           
    def damage(model_TARGET, model_RARROW):
        def do_damage(damage_color):
            damage_code = sum(damage_color)
            damage_key_map = {
                0: '6',    # buff
                50: '8',    # bear
                100: 'g',    # burst
                150: 'r',    # thrash
                200: 'q',    # raze
                250: '1',    # mangle
                300: '2',    # trash
            }

            if damage_code in damage_key_map:
                cici.press_key(damage_key_map[damage_code])

        print('fighting')

        combat_ticker = 0
        rotate = 0
        fallback = 0
        jumpy = 0
        infobox = capture_mode('infobox')
        combat_B, _ , _ = infobox[50,350]
        nomove = 0
        
        if combat_B == 255:
            return
        else:
            sleep(0.2)
            cici.press_key('8')
            sleep(0.2)

        while True:
            infobox = capture_mode('infobox')
            combat_B, _ , _ = infobox[50,350]

            if combat_B == 255:
                combat_ticker += 1

                if combat_ticker == 6:
                    print('no combat')
                    cici.press_key('n')
                    break

            else:
                combat_ticker = 0
                _, _ , target_R = infobox[150,150]
                
                if target_R == 255:
                    print('no target')
                    cici.press_key('n')
                    cici.press_key('3')
                    sleep(0.1)

                    rotate +=1

                    if rotate == 5:
                        cici.press_key('n')
                        cici.press_key(random.choice(['a', 'd']),random.uniform(0.3, 0.7))
                        cici.press_key('w', random.uniform(0.2, 0.4))
                        cici.press_key('3')
                        sleep(0.1)

                        rotate = 0
                    continue

                else:
                    range_B, _ , range_R = infobox[50,50]
                    _, _ , facing_R = infobox[50, 150]
                    RADAR = capture_mode('radar')
                    
                    if nomove > 2:
                        nomove = 0
                        try:
                            RARROW = crop(RADAR, 'rarrow', (133, 133))

                            predict_target = model_TARGET.predict(RADAR)
                            boxes_target = predict_target[0].boxes

                            box = boxes_target.xyxy[0].tolist()

                            target_position = [(box[0] + box[2]) / 2, (box[1] + box[3]) / 2]

                            location = (133, 133)

                            results_rarrow = model_RARROW.predict(RARROW)
                            boxes_rarrow, keypoints = results_rarrow[0].boxes, results_rarrow[0].keypoints
                            box = boxes_rarrow.xyxy[0].tolist()

                            position = [(box[0] + box[2]) / 2, (box[1] + box[3]) / 2]
                            pointer = keypoints.xy.tolist()[0][0]

                            vector_player = [pointer[0] - position[0], pointer[1] - position[1]]

                            magnitude_player = calculate_vector_magnitude(vector_player)
                            vector_north = [0, vector_player[1] - magnitude_player]

                            player_angle = round(calculate_angle_north(vector_player, vector_north))

                            target_vector = [target_position[0] - location[0], target_position[1] - location[1]]

                            distance = round(calculate_vector_magnitude(target_vector))

                            target_angle = round(calculate_angle_north(target_vector, vector_north))
                            print(f"P:{player_angle}, T:{target_angle}, D:{distance}")

                        except Exception as e:
                            cici.press_key('w', 0.5)

                            continue


                        if abs(target_angle - player_angle) > 15:
                            cici.press_key('n')

                            mouse_moves = cici.calculate_rotation_direction(player_angle, target_angle)
                            for index, move in enumerate(mouse_moves):

                                cici.move_mouse_steps(960 + move, 540)
                                sleep(0.04)

                        elif distance > 12:
                            cici.press_key('n')

                            cici.press_key('w', distance/25)
                            jumpy += 1
                            if jumpy == 2:
                                cici.press_key('space')
                                cici.press_key('w', distance/20)
                                jumpy = 0

                        elif range_B == 255:
                            fallback +=1
                            if fallback == 2:
                                cici.press_key('n')
                                cici.press_key('s', 0.3)
                                fallback = 0

                        

                    nomove += 1
                    cici.press_key('n')
                    damage_color = infobox[50, 250]

                    do_damage(damage_color)
                    cici.press_key('n')
                    sleep(0.2)

    def check_reset(start_time, run_time = 360):  
        current_time = datetime.now()

        delta = current_time - start_time

        if delta < timedelta(minutes = 6):
            sleep_time = (timedelta(minutes = 6) - delta).seconds
            print(f'we need to sleep {sleep_time}, cuz we runnin to fast')
            sleep(sleep_time)
            cici.press_key('w', 0.1)
        else:
            print(f"we aight, run took {delta}")

    def force_move(model_LOCATION, model_MARROW, mode):
        match mode:
            case 'pos_understairs':
                force_list = [(674, 337),[679, 326]]
                f = 0
                succ_killer = 0
                print(f'force changing pos for force_coords{force_list[f]}')

                while f < len(force_list) and succ_killer < 5:
                    force_coords = force_list[f]
                    
                    MAP = capture_mode('map')
                    try:
                        results_LOCATION = model_LOCATION.predict(MAP)
                        boxes = results_LOCATION[0].boxes

                        if boxes:
                            box = boxes.xyxy[0].tolist()
                            location = [round((box[0] + box[2]) / 2), round((box[1] + box[3]) / 2)]

                            MARROW = crop(MAP, 'marrow', location)

                            results_ARROW = model_MARROW.predict(MARROW)
                            boxes, keypoints = results_ARROW[0].boxes, results_ARROW[0].keypoints

                            if boxes:
                                box = boxes.xyxy[0].tolist()
                                position = [((box[0] + box[2]) / 2), (box[1] + box[3]) / 2]
                                pointer = keypoints.xy.tolist()[0][0]
                                vector_player = [pointer[0] - position[0], pointer[1] - position[1]]
                                magnitude_player = calculate_vector_magnitude(vector_player)
                                vector_north = [0, vector_player[1] - magnitude_player]
                                player_angle = round(calculate_angle_north(vector_player, vector_north))
                                
                                vector_force = [force_coords[0] - location[0], force_coords[1] - location[1]]
                                force_angle = round(calculate_angle_north(vector_force, vector_north))

                                distance = round(abs(force_coords[0] - location[0]) + abs(force_coords[1] - location[1]))
                    except Exception as e:
                        print(f"failed because {e}")
                        success = False
                        return success
                    

                    
                    cici.move_cursor_steps(960,540)
                    mouse_moves = cici.calculate_rotation_direction(player_angle, force_angle)
                    for index, move in enumerate(mouse_moves):
                        cici.move_mouse_steps(960 + move, 540)
                        sleep(0.04)

                    cici.gas(distance, 22.5)

                    MAP = capture_mode('map')
                    try:
                        results_LOCATION = model_LOCATION.predict(MAP)
                        boxes = results_LOCATION[0].boxes

                        if boxes:
                            box = boxes.xyxy[0].tolist()
                            location = [round((box[0] + box[2]) / 2), round((box[1] + box[3]) / 2)]

                            MARROW = crop(MAP, 'marrow', location)

                            results_ARROW = model_MARROW.predict(MARROW)
                            boxes, keypoints = results_ARROW[0].boxes, results_ARROW[0].keypoints

                            if boxes:
                                box = boxes.xyxy[0].tolist()
                                position = [((box[0] + box[2]) / 2), (box[1] + box[3]) / 2]
                                pointer = keypoints.xy.tolist()[0][0]
                                vector_player = [pointer[0] - position[0], pointer[1] - position[1]]
                                magnitude_player = calculate_vector_magnitude(vector_player)
                                vector_north = [0, vector_player[1] - magnitude_player]
                                player_angle = round(calculate_angle_north(vector_player, vector_north))
                                
                                vector_force = [force_coords[0] - location[0], force_coords[1] - location[1]]
                                force_angle = round(calculate_angle_north(vector_force, vector_north))

                                distance_new = (abs(force_coords[0] - location[0]) + abs(force_coords[1] - location[1]))
                    except Exception as e:
                        print(f"failed because {e}")
                        success = False
                        return success
                    
                    if distance_new < 4:
                        f += 1
                        
                    else:
                        cici.move_cursor_steps(960,540)
                        mouse_moves = cici.calculate_rotation_direction(player_angle, force_angle)
                        for index, move in enumerate(mouse_moves):
                            cici.move_mouse_steps(960 + move, 540)
                            sleep(0.04)

                        cici.press_key('a', 0.2)
                        cici.gas(distance, 22.5)                            

                    succ_killer += 1
                    print(succ_killer)

                if succ_killer == 5:
                    success = False
                    return success

                success = True
                
                return success

            case 'angle_reset':
                force_angle = 17
                    
                MAP = capture_mode('map')
                try:
                    results_LOCATION = model_LOCATION.predict(MAP)
                    boxes = results_LOCATION[0].boxes

                    if boxes:
                        box = boxes.xyxy[0].tolist()
                        location = [round((box[0] + box[2]) / 2), round((box[1] + box[3]) / 2)]

                        MARROW = crop(MAP, 'marrow', location)

                        results_ARROW = model_MARROW.predict(MARROW)
                        boxes, keypoints = results_ARROW[0].boxes, results_ARROW[0].keypoints
                        
                        if boxes:
                            box = boxes.xyxy[0].tolist()
                            position = [((box[0] + box[2]) / 2), (box[1] + box[3]) / 2]
                            pointer = keypoints.xy.tolist()[0][0]
                            vector_player = [pointer[0] - position[0], pointer[1] - position[1]]
                            magnitude_player = calculate_vector_magnitude(vector_player)
                            vector_north = [0, vector_player[1] - magnitude_player]
                            
                            player_angle = round(calculate_angle_north(vector_player, vector_north))
                except Exception as e:
                    print(f"failed because {e}")
                    success = False
                    return success

                print(player_angle)
                if abs(player_angle-force_angle) > 4:
                    cici.move_cursor_steps(960,540)
                    mouse_moves = cici.calculate_rotation_direction(player_angle, force_angle)
                    for index, move in enumerate(mouse_moves):
                        cici.move_mouse_steps(960 + move, 540)
                        sleep(0.04)
                else:
                    print(f'angle is aight, P:{player_angle}, F:{force_angle}')


    start_time = datetime.now().strftime("%d.%m_%H:%M")
    csv_name = f"logs\\{ID}_latest.csv"
    clear_file(csv_name)

    #write_to_csv(f"ID/{ID}/ started script at TIME/{start_time}/\n", csv_name)
    
    runs_did = 0
    death_count = 0
    cp_failures = 0

    while runs_did < to_run:
        runs_did += 1
        run_start = datetime.now()
        rt_pasta = run_start.strftime("%H:%M")
        #write_to_csv(f"RUN/{r}/ started at TIME/{rt_pasta}/", csv_name)
        failure = "no"
        
        for key, cp_list in fhd_route_dict.items():
            if key == 'RETURN':

                damage(model_TARGET, model_RARROW)
                sleep(1)
                sell_loot()
                try:
                    travel(key, cp_list,model_LOCATION, model_MARROW)
                except IndexError:
                    print('niiigggger')
                    damage(model_TARGET, model_RARROW)
                    sleep(2)
                    cici.press_key('4')
                    print('pressed 4')
                    sleep(1)
                    cici.press_key('5')
                    print('sslleeeeppin')
                    sleep(90)

                    check_reset(run_start)
                    reset_dung()
                    break
                except Exception as e:
                    print(f'failed cuz {e}')
                    cici.press_key('w', 0.3)

                check_reset(run_start)
                force_move(model_LOCATION, model_MARROW, 'angle_reset')
                reset_dung()

            else:
                try:
                    travel(key, cp_list,model_LOCATION, model_MARROW)
                    damage(model_TARGET, model_RARROW)
                except IndexError:
                    #cp failure
                    print('niiigggger')
                    damage(model_TARGET, model_RARROW)
                    sleep(1)
                    cici.press_key('4')
                    print('pressed 4')
                    sleep(1)
                    cici.press_key('5')
                    print('sslleeeeppin')
                    sleep(90)
                    
                    check_reset(run_start)
                    reset_dung()
                    failure = f"CP at {key}"
                    cp_failures += 0
                    break


                except ValueError:
                    #death
                    cici.press_key('a',1)
                    cici.press_key('w',0.5)

                    check_reset(run_start)
                    force_move(model_LOCATION, model_MARROW, 'angle_reset')
                    reset_dung()

                    failure = f"DEATH at {key}"
                    death_count += 1
                    break

                except Exception as e:
                    print(f'failed cuz {e}')
                    cici.press_key('w', 0.3)

        run_finish = datetime.now()
        rf_pasta = run_finish.strftime("%H:%M")

        time_took = '{:02}:{:02}'.format(*divmod((run_finish - run_start).seconds, 60))
        
        #write_to_csv(f"RUN/{r}/ finished at {rf_pasta} FAIL/{failure}/, SPENT/{time_took}", csv_name)



if __name__ == "__main__":
    creds = "sergeynegej5@gmail.com", "csoYWBHzI92VPY27dn"
    
    wake_hrs = random.randint(6, 8)
    sleep_hrs = random.randint(19, 23)
    print(f"wakin {wake_hrs}, sslleeeeppin: {sleep_hrs}")
    full_cycle = 0
    total_ran = 0
    
    while full_cycle < 5:

        runs_amount = random.randint(14, 67)
        
        current_hour = 10 #datetime.now().hour
        
        print(f"currently: {current_hour}, WILL RUN {runs_amount}")

        if current_hour > sleep_hrs or current_hour < wake_hrs:
            left_sleeping = wake_hrs - current_hour + uniform(0,2)
            if current_hour > sleep_hrs:
                left_sleeping = 24 - current_hour + wake_hrs + uniform(0,1)
            
            print(f'currently sleep for for {left_sleeping}')
            sleep(left_sleeping*60*60)
        
        else:
            
            print('redy to go')

            loginer(creds)
        
            grp_creation()

            

            freehold_farmer(runs_amount)

            print('finished all runs')

            logout()
            

            afterwork_nap = 1 + uniform(0,3)
            
            total_ran += runs_amount
            
            print(f'after work will sleep for {afterwork_nap}, already did: {total_ran} runs')
            sleep(afterwork_nap*60*60)

            full_cycle +=1 

    




        
        




