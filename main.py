
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
"""
   This function greets to
   the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"



"""

from ast import Num
from os import name
from typing import Dict


def greet(name, msg='good morning ! <name>'):

    msg = msg.replace('<name>', name)
    return msg


print(greet('doc'))
print(greet('Bob', "What's up, <name>!"))


dict = {
    'sun': 274,
    'jupiter': 24.9,
    'neptune': 11.2,
    'earth': 9.82598,
    'saturn': 2.44,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.6,
    'pluto': 0.6

}


def force(mass, body='earth'):
    body_afgerond = ()
    body_afgerond = round(dict[body], 1)

    force = body_afgerond * mass
    return force


l = force(2, 'saturn')
print('de zwaartekracht= ', l)


def pull(m1, m2, d):
    g = 6.674*10**-11
    pull = g * ((m1*m2)/(d**2))
    return pull


print('de kracht in newton is ', pull(800, 1500, 3))
