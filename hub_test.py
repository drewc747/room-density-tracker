# hub_test.py

import sys
sys.path.insert(1, './state_machines/')
sys.path.insert(1, './state_machines/lasers')
sys.path.insert(1, './state_machines/rooms')
sys.path.insert(1, './state_machines/devices')

from house import House
import lasers
import rooms

# initialize room counters
house_cnt = 1
bat1_cnt = 0
bat2_cnt = 0
bed1_cnt = 0
bed2_cnt = 0
hal_cnt = 0
kit_cnt = 0
liv_cnt = 1
utl_cnt = 0

# initialize house/rooms
house = House()
bat1 = rooms.Bat1()
bat2 = rooms.Bat2()
bed1 = rooms.Bed1()
bed2 = rooms.Bed2()
hal = rooms.Hal()
kit = rooms.Kit()
liv = rooms.Liv()
utl = rooms.Utl()

# initialize lasers


def print_status():
    print(f'   House counter: {house_cnt} | State: {house.state}')
    print(f'      Bathroom1 counter: {bat1_cnt} | State: {bat1.state}')
    print(f'      Bathroom2 counter: {bat2_cnt} | State: {bat2.state}')
    print(f'      Bedroom1 counter: {bed1_cnt} | State: {bed1.state}')
    print(f'      Bedroom2 counter: {bed2_cnt} | State: {bed2.state}')
    print(f'      Hallway counter: {hal_cnt} | State: {hal.state}')
    print(f'      Kitchen counter: {kit_cnt} | State: {kit.state}')
    print(f'      Living room counter: {liv_cnt} | State: {liv.state}')
    print(f'      Utility room counter: {utl_cnt} | State: {utl.state}')
    print()

if __name__ == '__main__':
    print(f'Initial Counters and States:')
    print_status()
    
    
