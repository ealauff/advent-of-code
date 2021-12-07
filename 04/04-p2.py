# --- Part Two ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, 
# so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. 
# That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, 
# which happens after 13 is eventually called and its middle column is completely marked. 
# If you were to keep playing until this point, 
# the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

# Your puzzle answer was XXXXX.

###########################################################################################################################################################################

import pathlib


def find_last_winning_board(numbers, data, num_boards):
    c = 0
    winners = []
    for n in numbers:
        board_num = 0
        row_num = 0
        for entry in data:
            if entry == '':
                board_num += 1
                row_num = 0
                continue
            row = entry.split()
            if n in row:
                sums[board_num][0][row_num] += 1
                sums[board_num][1][row.index(n)] += 1
                if 5 in sums[board_num][0] or 5 in sums[board_num][1]:
                    if not(board_num in winners):
                        winners.append(board_num)
                        if len(winners) == num_boards:
                            return board_num, c
            row_num += 1
        c += 1


def get_sum_unmarked(board, numbers, c):
    unmarked = board.copy()
    for n in range(0, c+1):
        number = numbers[n]
        if number in unmarked:
            unmarked.remove(number)
    return sum(map(int, unmarked))*int(number)


f = open(pathlib.Path(__file__).parent / 'input.txt', "r").read().splitlines()

boards = []
board_num = 0
board_list = []

for entry in f[2:]:
    if entry == '':
        boards.append(board_list)
        board_num += 1
        board_list = []
        row_list = []
        continue
    board_list += entry.split()

boards.append(board_list)

numbers = f[0].split(',')
sums = []
for i in range(100):
    sums.append([[0]*5, [0]*5])

board, c = find_last_winning_board(numbers, f[2:], len(boards))

print(get_sum_unmarked(boards[board], numbers, c))

# IMPROVEMENTS:
# - change so that we are only doing this many iterations: numbers*total numbers on boards
# - looping over numbers and boards many times
# - shouldnt have to create the boards array
