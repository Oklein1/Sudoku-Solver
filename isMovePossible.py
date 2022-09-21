def isPossibleXMove(grid,x,n):
    if len(list(filter(lambda x: x == n, grid[x]))) == 0:
        return True
    else:
        return False
    

def isPossibleYMove(grid,y,n):
    data = [grid[i][y] for i in range(len(grid[0]))]
    if len(list(filter(lambda y: y == n, data))) == 0:
        return True
    else:
        return False
    
def isPossibleinDomain(grid,x,y,n):
    centroidX = (x//3)*3
    centroidY = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[centroidX+i][centroidY+j] == n:
                return False
    return True


def isPossibleMove(grid,x,y,n):
    if isPossibleXMove(grid,x,n) and isPossibleYMove(grid,y,n) and isPossibleinDomain(grid,x,y,n):
        return True
    else:
        return False