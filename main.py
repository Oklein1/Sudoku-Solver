from boardUI import print_grid
from isMovePossible import isPossibleMove

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,0,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [0,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,0,0,0,7,9]]





def solve():
    global grid
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    if isPossibleMove(grid,x,y,n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    print_grid(grid)
    input("Finished. Hit any button to exit.")




def main():
    solve()
    
if __name__ == '__main__':
    main()