import copy

def check(grid, seat_pos):
    seat_x, seat_y = seat_pos
    directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    count = 0
    for x, y in directions:
        if seat_x + x in range(len(grid)) and seat_y + y in range(len(grid[0])):
            if grid[seat_x + x][seat_y + y] == '#':
                count += 1
    return count

def evolve(grid):
    while True:
        old_grid = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if old_grid[i][j] == 'L' and check(old_grid, (i, j)) == 0:
                    grid[i][j] = '#'
                elif old_grid[i][j] == '#' and check(old_grid, (i, j)) >= 4:
                    grid[i][j] = 'L'
        if grid == old_grid:
            return


with open(r'days\11\input.txt', 'r') as f:
    grid = [list(i.strip()) for i in f]
    evolve(grid)
    for i in grid:
        print(i)
    c = sum(row.count('#') for row in grid)
    print(c)