from ultralytics import YOLO
from pyautogui import press 
import keyboard
import time

from capture_fhd import screenshot_mode

def coords():
    model_LOCATION = YOLO('C:\\piton\\git\\plateenum\\7ver_wow\\instruments\\LOCATION_FHD_NORESIZE_3.pt')
    model_LOCATION.to('cuda')

    print('loaded')
    

    while True:
        if keyboard.is_pressed('q'):
            MAP = screenshot_mode('map')
            results_LOCATION = model_LOCATION.predict(MAP)

            boxes = results_LOCATION[0].boxes

            if boxes:
                box = boxes.xyxy[0].tolist()
                location = [round((box[0]+box[2])/2),round((box[1]+box[3])/2)]
                print(location)

        time.sleep(0.01)
        
        if keyboard.is_pressed('z'):
            break

coords()

[726, 139] 
[705, 147] 
[713, 164] 
[677, 203] 
[693, 247] 
 #right1
 #right2 
 #left2
 #stairs
 #test


fhd_route_dict = {
'first_pull': [[[726, 139], 3, None, None],# left
 [[705, 147], 4, None, None], #right
 [[713, 164], 5, None, None], #align to big
 [[677, 203], 8, None, None], #big
 [[693, 247], 4, None, None], #left
 [[649, 244], 4, None, None], #right1
 [[647, 276], 5, None, None], #right2
 [[675, 294], 6, None, None], #left2
 [[666, 316], 5, None, None], #stairs
 [[676, 276], 3, None, 4]], #test,

}

newroutefullhd_dict = {
'first_pull': [[[575, 174], 3, None, None],
 [[554, 180], 4, None, None],
 [[560, 203], 5, None, None],
 [[534, 244], 8, None, None],
 [[546, 300], 4, None, None],
 [[512, 294], 4, None, None], #right1
 [[509, 335], 5, None, None], #right2
 [[533, 356], 6, None, None], #left
 [[520, 408], 5, None, None], #align stairs
 [[527, 421], 3, None, 4],
 [[518, 404], 5, None, None]],
 
'boss1_pull': [[[427, 361], 2, None, None],#align stairs
 [[432, 372], 2, None, None],
 [[442, 384], 5, 135, None],
 [[453, 368], 2, 40, None],
 [[471, 355], 8, None, None],
 [[490, 335], 8, None, None],
 [[494, 309], 8, None, None],
 [[487, 293], 4, None, None],
 [[480, 310], 6, None, None]],
'boss1_TO_rp':[ #[[479, 301], 5, None, None], #uppper repos
 [[460, 302], 8, None, None], #close to jump
 [[443, 303], 10, None, None], #jumped off
 [[438, 334], 6, None, None], # align with brdge
 [[421, 349], 2, None, None], #enter brige
 [[400, 367], 10, 225, None], #1 bridge
 [[365, 396], 10, None, None], #2 bridge
 [[338, 420], 3, None, None], #end of bridge
 [[333, 424], 8, None, None], #out of bridgei
 [[315, 426], 4, None, None], #right drunk
 [[324, 443], 4, None, None], #left drunk1
 [[316, 453], 3, None, None], #left drunk2
 [[292, 462], 4, None, None], #left drunk3
 [[275, 439], 4, None, None], #center 
 [[259, 440], 5, None, None], #lefty
 [[247, 432], 5, None, None], #pack to right
 [[242, 436], 2, None, None], #stairs ###
 [[207, 433], 7, None, None],##center to last

 [[211, 429], 3, None, None], ##align jump
 [[219, 420], 7, None, None], # jump
 [[232, 417], 5, None, None], # 1patrol
 [[247, 399], 7, None, None], # patrol
 [[240, 394], 4, None, None], #align harpoon
 [[203, 382], 9, None, None], #run harpoon
 [[215, 381], 9, None, None] #last harpywmm
 
 ],


'boss2_TO_boss3':[ 
 [[212, 387], 5, None, None], #close to jump
 [[173, 395], 8, None, None], #biqmmboi
 [[171, 415], 6, None, None], # right caster
 [[190, 415], 4, None, None], #left caster
 ],

'RETURN': [

 [[188, 421], 6, None, None], #center
 [[195, 408], 3, None, None], #align to road
 [[208, 394], 6, None, None], #jumpoff to road

 [[269, 393], 5, None, None], #2boss
 [[296, 437], 10, None, None], #rp
 [[330, 426], 2, None, None], #bridge align
 [[340, 418], 3, None, None], #onbridge
 [[366, 396], 10, None, None], #br1
 [[394, 372], 10, None, None], #br2
 [[424, 347], 3, None, None], #brout
 [[453, 284], 3, None, None], #woods
 [[462, 247], 3, None, None], #portal align
 [[477, 227], 6, None, None],
 [[480, 223], 6, None, None],

 ]
 
}







slower_way_dict = {
'first_pull': [[[467, 264], 3, None, None],
 [[456, 269], 4, None, None],
 [[459, 279], 5, None, None],
 [[441, 300], 8, None, None],
 [[449, 327], 4, None, None],
 [[426, 324], 4, None, None], #right1
 [[424, 342], 5, None, None], #right2
 [[438, 353], 8, None, None], #left
 [[429, 375], 5, None, None], #align stairs
 [[435, 383], 3, None, 4],
 [[428, 372], 5, None, None]],
'boss1_pull': [[[427, 361], 2, None, None],#align stairs
 [[432, 372], 2, None, None],
 [[440, 382], 5, 135, None],
 [[453, 368], 7, 40, None],
 [[471, 355], 8, None, None],
 [[490, 335], 8, None, None],
 [[494, 309], 8, None, None],
 [[487, 293], 4, None, None],
 [[480, 310], 6, None, None]],
'boss1_TO_rp':[ [[479, 301], 5, None, None], #uppper repos
 [[460, 302], 8, None, None], #close to jump
 [[443, 303], 10, None, None], #jumped off
 [[438, 334], 6, None, None], # align with brdge
 [[421, 349], 2, None, None], #enter brige
 [[400, 367], 10, 225, None], #1 bridge
 [[365, 396], 10, None, None], #2 bridge
 [[338, 420], 3, None, None], #end of bridge
 [[333, 424], 8, None, None], #out of bridgei
 [[315, 426], 4, None, None], #right drunk
 [[324, 441], 4, None, None], #left drunk1
 [[315, 446], 3, None, None], #left drunk2
 [[292, 463], 4, None, None], #left drunk3
 [[275, 439], 4, None, None], #center 
 [[259, 440], 5, None, None], #lefty
 [[247, 432], 5, None, None], #pack to right
 [[242, 436], 2, None, None], #stairs #####center to last
 [[207, 433], 7, None, None] ],

'boss3_first':[[[205, 433], 3, None, None],
 [[203, 434], 6, None, None], 
 [[192, 430], 6, None, None], #dropdown
 [[170, 416], 6, None, None], #1pack 
 [[189, 415], 3, None, None]],  #mid
'boss3_second':[[[183, 419], 5, None, None], #reset
 [[177, 395], 4, None, None], #bigboi
 [[201, 393], 3, None, None], #center between packs
 [[217, 373], 6, None, None], #bridge pack+beckpack
 [[225, 391], 8, None, None]], #lastone
'boss3_third':[[[220, 376], 3, None, None], #reset
 [[212, 357], 2, None, None], #align with road
 [[199, 357], 3, None, None], #last prepare
 [[199, 357], 6, None, None], #to bigboi
 [[174, 358], 5, None, None]], #back to road

'boss3_TO_boss2': 
[[[174, 362], 3, None, None], #align
 [[191, 389], 8, None, None], #dropdown
 [[245, 400], 5, None, None], #patrol end
 [[234, 415], 6, None, None], #patrol mid
 [[215, 414], 6, None, None]], #LAST
'RETURN':
[[[243, 406], 6, None, None], #patrol
 [[263, 398], 6, None, None], #2boss
 [[296, 437], 10, None, None], #rp
 [[330, 426], 2, None, None], #bridge align
 [[340, 418], 3, None, None], #onbridge
 [[366, 396], 10, None, None], #br1
 [[394, 372], 10, None, None], #br2
 [[424, 347], 3, None, None], #brout
 [[453, 284], 3, None, None], #woods
 [[462, 247], 3, None, None], #portal align
 [[477, 227], 6, None, None],
 [[480, 223], 6, None, None],
 
 ]
}