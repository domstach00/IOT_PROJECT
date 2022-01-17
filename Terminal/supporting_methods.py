from constants import *
import random


def read_rfid() -> str:
    for card in RFID_CARDS:
        if card not in USED_CARDS:
            USED_CARDS.append(card)
            print(f"ENTER {card}")
            return card


def find_used_card() -> str:
    card = random.choice(USED_CARDS)
    USED_CARDS.remove(card)
    print(f"ESCAPE: {card}")
    return card
