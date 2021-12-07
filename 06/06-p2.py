# --- Part Two ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

# After 256 days in the example above, there would be a total of 26984457539 lanternfish!

# How many lanternfish would there be after 256 days?

# Your puzzle answer was 1738377086345.

########################################################################################################################################################################################################################################################

import pathlib


def calc_num_offspring(starting_age, days_left):
    if not '{}:{}'.format(starting_age, days_left) in fish_memo:

        # Not enough days to have any offspring
        if days_left - (starting_age + 1) < 0:
            return 0

        else:
            offspring = 0

            # Will have an offspring every 7 days after the first time age gets to 0 then resets
            for day in range(days_left - (starting_age + 1), -1, -7):
                offspring += 1
                offspring += calc_num_offspring(8, day)

            fish_memo['{}:{}'.format(starting_age, days_left)] = offspring

    return fish_memo['{}:{}'.format(starting_age, days_left)]


fish_list = open(pathlib.Path(__file__).parent /
                 'input.txt', "r").read().split(',')

# get rid of /n at the end of the array
fish_list[-1] = fish_list[-1].strip()
fish_memo = {}

total_fish = 0
num_days = 256

# The weird string formatting here for dict keys isn't necessary to get the right answer,
# but just keeps the fish_memo keys consistent
for fish in fish_list:
    if not '{}:{}'.format(fish, num_days) in fish_memo:
        fish_memo['{}:{}'.format(fish, num_days)] = calc_num_offspring(
            int(fish), num_days) + 1

    total_fish += fish_memo['{}:{}'.format(fish, num_days)]

print(total_fish)
