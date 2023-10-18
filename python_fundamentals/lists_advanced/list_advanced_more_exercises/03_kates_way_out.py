def starting_pos(some_maze: list):
    starting_row = 0
    starting_spot = 0

    for row in some_maze:
        for pos in row:
            if pos == 'k':
                starting_row = int(maze.index(row))
                starting_spot = int(maze.index(pos))
    starting_position = some_maze[starting_row][starting_spot]
    return starting_position


def end_pos(some_other_maze: list):
    ending_row = 0
    ending_spot = 0

    for row in some_other_maze:
        for pos in row:
            if pos == 'x':
                ending_row = int(maze.index(row))
                ending_spot = int(maze.index(pos))
    starting_position = some_other_maze[ending_row][ending_spot]
    return starting_position

rows = int(input())

maze = []

for line in range(rows):
    maze.append(list(input()))



