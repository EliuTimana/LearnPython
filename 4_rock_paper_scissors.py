import random

def play():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors:\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or \
        (player == 'p' and opponent == 'r') or \
        (player == 's' and opponent == 'p'):
        return True
    else:
        return False

print(play())