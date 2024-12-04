from sys import modules

from main import give_toefl_voca, guess_meaning_of_voca
from modules.db import connect_db
from modules.db import register_user

if __name__ == "__main__":
    # voca = give_toefl_voca()
    # guess_meaning_of_voca(voca)
    register_user()