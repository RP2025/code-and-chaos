def winningpatterns(grid):
    positions = [[i * grid + j for j in range(grid)] for i in range(grid)]
    return (
        positions +                                            # rows
        [[positions[j][i] for j in range(grid)] for i in range(grid)] +  # columns
        [[positions[i][i] for i in range(grid)],             # diagonal top-left → bottom-right
         [positions[grid-i-1][i] for i in range(grid)]]     # diagonal top-right → bottom-left
    )

print(winningpatterns(3))

def check_win(winning_patterns, player_moves):
    player_moves = set(player_moves)

    for pattern in winning_patterns:
        if set(pattern).issubset(player_moves):
            return True

    return False




# METHOD ONE 
# def tictactoe(grid):
#     wp = winningpatterns(grid)

#     one_inp = []
#     cross_inp = []

    
#     for i in range(0,9):
#         position = int(input("Enter position (0-8): "))
#         userinp = int(input("enter symbol"))
#         if userinp == 1:
#             one_inp.append(position)
#             if is_subarray(wp,one_inp):
#                 return "one wins"

#         else:
#             cross_inp.append(position)
#             if is_subarray(wp,cross_inp):
#                 return "Cross wins"
        
#     return "DRAW"


# print(tictactoe(3))

# METHOD TWO
def tictactoe(grid):
    wp = winningpatterns(grid)
    cross_inp = []
    one_inp = []
    Startuser = int(input("Enter who starts first (1 for one and 2 for cross): "))
    currUser = Startuser
    for i in range(0,9):
        position = int(input("Enter position (0-8): "))
        if currUser == 1:
            if position in one_inp or position in cross_inp:
                print("Position already taken. Try again.")
                continue
            one_inp.append(position)
            if check_win(wp, one_inp):
                return "one wins"
            currUser = 2
        else:
            if position in one_inp or position in cross_inp:
                print("Position already taken. Try again.")
                continue
            cross_inp.append(position)
            if check_win(wp, cross_inp):
                return "Cross wins"
            currUser = 1
    return "DRAW"

print(tictactoe(3))