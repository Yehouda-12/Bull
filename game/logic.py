from validate import is_valis_guess,is_new_guess
from secret import create_number
def score_guess(secret: str, guess: str) -> tuple[int, int]:
    is_valid,message = is_valis_guess(guess)
    bulls = 0
    cows = 0
    if is_valid :
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                for j in range(len(secret)):
                    if secret[i] == guess[j]:
                        cows +=1
    return bulls ,cows

def is_won(bulls:int,length=4):

    return bulls == length

def init_state(secret: str, length= 4, max_tries= None, unique_digits=True,
allow_leading_zero= True) -> dict:
    game_dict = { "secret": secret,
                  "length": length,
                  "max_tries": max_tries,
                  "tries_used": 0,
                  "unique_digits": True,
                  "allow_leading_zero": True,
                  "history": list[tuple[str, int, int]],
                  "seen": set[str] }
    return game_dict
def apply_guess(state:dict,guess:str):
    pass
print(init_state(create_number(),))