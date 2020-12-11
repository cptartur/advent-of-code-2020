import copy

def check(grid, seat_pos):
    seat_x, seat_y = seat_pos
    directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    count = 0
    for x, y in directions:
        xx, yy = seat_x + x, seat_y + y
        while xx in range(len(grid)) and yy in range(len(grid[0])):
            if grid[xx][yy] == '#':
                count += 1
                break
            elif grid[xx][yy] == 'L':
                break
            xx += x
            yy += y
    return count

def evolve(grid):
    while True:
        old_grid = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if old_grid[i][j] == 'L' and check(old_grid, (i, j)) == 0:
                    grid[i][j] = '#'
                elif old_grid[i][j] == '#' and check(old_grid, (i, j)) >= 5:
                    grid[i][j] = 'L'
        if grid == old_grid:
            return


with open(r'days\11\input.txt', 'r') as f:
    grid = [list(i.strip()) for i in f]
    evolve(grid)
    c = sum(row.count('#') for row in grid)
    print(c)