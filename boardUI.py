def print_grid(grid):
    for line in grid:
        for cell in line:
            if cell == 0:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print(" ", end="\n")