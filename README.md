# Room Density Tracker
A smart home manager for room density. This software package is to be ported to a Rasbery Pi to manage
smart home functionality that relies on knowning how many people are in a given room. All communication will 
be wireless and work on the homes wifi. Some examples of functionality include:

- Automatic lights (Initial testing will focus on this application)
- Music sources
- Automatic locks
- Thermostat sleep mode

## Current Status:
Currently the state machines for each room, laser module, and the house are created. When an input from a laser module is counts for each room and the whole house are updated and laser power modes are updated. This is demonstrated by running hub_test.py. Next steps are to set up the hardware.

## Resources:
The room density tracker consists of the following submodules:

1.  The Hub
2.  Laser sender module
3.  Laser receiver module
4.  Light relay module

### The Hub:
The hub acts as the main manager for the system. It will recieve messages from the laser modules as inputs
and output messages to the laser modules and light relay.  The resources required for the hub consist of:

- Rasberry Pi
- Wifi transciever
- Power Source

Functionalities:

- Recieve and process messages from laser modules
  - Get ID of laser module to determine which beam has been broken
  - Get order of broken beams to determine direction of travel
- Keep counter for each room in house
  - Increment and decrement counter as people enter and leave rooms
  - Needs to be able to be manually reset
  - Needs to check for logic errors in case a beam breaker was accidently tripped or multiple go through door at once
and update accordingly
- Send messages to light relay modules to turn on or off
- Send messages to laser modules to turn on or off
  - To reduce power consumption, a laser should only be on if someone is occupying an adjacent room
  - If only one person is in entire house, only one laser is need per doorway since direction of travel is implied
  - Initiate sleep mode if no one is home where all lasers are turned off
  
### Laser sender module:
The laser sender consists of two lasers, a power source, a transciever, and logic gates. The laser sender module receives 
messages from the hub to determine which laser(s) should be turned on.

### Laser receiver module:
The laser receiver module consists of two photoresistors, two analog to digital converters, a power source, a 
transceiver and logic gates. The laser receiver module determines if a beam is broken and the order in which the 
beams are broken and sends a message to the hub. It also subscribes to the channel indicating which lasers are 
currently on.

### Light relay module:
The light relay recieves messages from the hub to turn a light on or off.  
