# hub_test.py

import sys
sys.path.insert(1, './state_machines/')
sys.path.insert(1, './state_machines/lasers')
sys.path.insert(1, './state_machines/rooms')
sys.path.insert(1, './state_machines/devices')

from house import House
import lasers
import rooms

'''
HUB
 - Recieves input from laser packages
 - Processes inputs and manages events sent to rooms/lasers/house
'''

# initialize house/rooms
house = House()
bt1 = rooms.Bt1()
bt2 = rooms.Bt2()
bd1 = rooms.Bd1()
bd2 = rooms.Bd2()
hal = rooms.Hal()
kit = rooms.Kit()
liv = rooms.Liv()
utl = rooms.Utl()

# initialize lasers
bt1_hal = lasers.Bt1Hal()
bt2_bd2 = lasers.Bt2Bd2()
bd1_bd2 = lasers.Bd1Bd2()
bd1_hal = lasers.Bd1Hal()
bd2_hal = lasers.Bd2Hal()
hal_liv = lasers.HalLiv()
hal_utl = lasers.HalUtl()
kit_liv = lasers.KitLiv()
kit_utl = lasers.KitUtl()

out_bd1 = lasers.OutBd1()
out_liv = lasers.OutLiv()
out_utl = lasers.OutUtl()    

module_list = ['bt1_hal', 'bt2_bd2', 'bd1_bd2', 'bd1_hal', 'bd2_hal', 'hal_liv', 'hal_utl', 'kit_liv', 'kit_utl', 'out_bd1', 'out_liv', 'out_utl']

def update_lasers():
    for module in module_list:
        rooms = eval(module).name.split('_')
        if rooms[0] == 'out':
            if eval(rooms[1]).count == 0:
                eval(module).on_event('single')
            else:
                eval(module).on_event('dual')
        else:
            if (eval(rooms[0]).count + eval(rooms[1]).count) == 0:
                eval(module).on_event('off')
            elif (eval(rooms[0]).count + eval(rooms[1]).count) == 1:
                eval(module).on_event('single')
            elif eval(rooms[0]).count == 0 or eval(rooms[1]).count == 0:
                eval(module).on_event('single')
            else:
                eval(module).on_event('dual')

def laser_input(module, signal):
    module_state = str(module.state)
    module_name = module.name.split('_')
    
    if module_name[0] == 'out':
        if signal == 'in':
            eval(module_name[1]).on_event('entry')
            house.on_event('entry')
        elif signal == 'out':
            eval(module_name[1]).on_event('exit')
            house.on_event('exit')
    else:
        if module_state == 'SingleState':           
            if signal == 'in' or signal == 'out':
                if  eval(module_name[0]).count == 0:
                    eval(module_name[0]).on_event('entry')
                    eval(module_name[1]).on_event('exit')
                elif eval(module_name[0]).count == 1:
                    eval(module_name[0]).on_event('exit')
                    eval(module_name[1]).on_event('entry')
            else:
                print(f'BAD SIGNAL - signal = {signal}. Module state = {module_state}. Module name = {module_name}')
                
        elif module_state == 'DualState':
            if signal == 'in':
                eval(module_name[0]).on_event('exit')
                eval(module_name[1]).on_event('entry')
            elif signal == 'out':
                eval(module_name[0]).on_event('entry')
                eval(module_name[1]).on_event('exit')
            else:
                print(f'BAD SIGNAL - signal = {signal}. Module state = {module_state}. Module name = {module_name}')
    
    update_lasers()
    
def print_status():
    print(f'   House counter: {house.count} | State: {house.state}')
    print(f'      Bathroom1 counter: {bt1.count} | State: {bt1.state}')
    print(f'      Bathroom2 counter: {bt2.count} | State: {bt2.state}')
    print(f'      Bedroom1 counter: {bd1.count} | State: {bd1.state}')
    print(f'      Bedroom2 counter: {bd2.count} | State: {bd2.state}')
    print(f'      Hallway counter: {hal.count} | State: {hal.state}')
    print(f'      Kitchen counter: {kit.count} | State: {kit.state}')
    print(f'      Living room counter: {liv.count} | State: {liv.state}')
    print(f'      Utility room counter: {utl.count} | State: {utl.state}')
    
    print('   Lasers:')
    print(f'      Bathroom1/Hallway state: {bt1_hal.state}')
    print(f'      Bathroom2/Bedroom2 state: {bt2_bd2.state}')
    print(f'      Bedroom1/Bedroom2 state: {bd1_bd2.state}')
    print(f'      Bedroom1/Hallway state: {bd1_hal.state}')
    print(f'      Bedroom2/Hallway state: {bd2_hal.state}')
    print(f'      Hallway/Living state: {hal_liv.state}')
    print(f'      Hallway/Uitility state: {hal_utl.state}')
    print(f'      Kitchen/Living state: {kit_liv.state}')
    print(f'      Kitchen/Utility state: {kit_utl.state}')
    print(f'      Outside/Bedroom1 state: {out_bd1.state}')
    print(f'      Outside/Living state: {out_liv.state}')
    print(f'      Outside/Utility state: {out_utl.state}')
    print()
if __name__ == '__main__':
    print('Initial Counters and States:')
    print_status()
    laser_input(out_liv, 'in')
    print('Counters and States:')
    print_status()
    laser_input(out_liv, 'in')
    print('Counters and States:')
    print_status()
    laser_input(out_liv, 'out')
    print('Counters and States:')
    print_status()
    laser_input(kit_liv, 'out')
    print('Counters and States:')
    print_status()
    
    
