import random

def create_number(lengh=4,unique_digits=True) ->str:
    secret = ''.join(random.sample('0123456789',lengh))
    return secret

def prompt_number(lentgh=4):
    a = input(f"Enter a {lentgh}-digit number : ")
    return a

def is_valis_guess(guess:str,lenght:int,) -> tuple[bool,str]:
    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == len(guess):
        return True,'Valid number.'
    return False,'Enter valid number'

def is_new_guess(guess:str,state:dict) ->bool:
    return guess not in state['guess']