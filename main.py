import random
grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
def printGrid(n):
  for i in range(len(n)):
    print(""+n[i][0]+"  |"+n[i][1]+"  |"+n[i][2])
    
    if i < 2:
      print("---+---+---")
printGrid(grid)
q = random.randint(1,2)
if q == 1:
  print("You start!")
if q == 2:
  print("Computer starts!")

def forkChecker(n,typ,chtyp,opp):
  
  for i in range(3):
    for j in range(3):
      if n[i][j] == " ":
        newGrid = copygrid(n)
        newGrid[i][j] = typ
        
        winningmove(newGrid,typ,opp)
        if winningmove(newGrid,typ,opp) == True:
          n[i][j] = chtyp
          return True
  return False



def wincheck(n,typ):
  if n[0][0] == typ and n[0][1] == typ and n[0][2] == typ:
    return True
  if n[1][0] == typ and n[1][1] == typ and n[1][2] == typ:
    return True
  if n[2][0] == typ and n[2][1] == typ and n[2][2] == typ:
    return True
  if n[0][0] == typ and n[1][0] == typ and n[2][0] == typ:
    return True
  if n[0][1] == typ and n[1][1] == typ and n[2][1] == typ:
    return True
  if n[0][2] == typ and n[1][2] == typ and n[2][2] == typ:
    return True
  if n[0][0] == typ and n[0][1] == typ and n[0][2] == typ:
    return True
  if n[0][0] == typ and n[1][1] == typ and n[2][2] == typ:
    return True
  if n[0][2] == typ and n[1][1] == typ and n[2][0] == typ:
    return True
  return False
def copygrid(n):
  copy = []
  for i in range(3):
    row = []
    for j in range(3):
      row.append(n[i][j])
    copy.append(row)
  return copy
  
  
def winningmove(n,typ,opp):
  for i in range(3):
    for j in range(3):
      if n[i][j] == " ":
        newGrid = copygrid(n)
        newGrid[i][j] = typ
        if wincheck(newGrid,typ) == True:
          n[i][j] = opp
          return True
  return False
        
      
while True:
  
  if " " not in grid[0] and " " not in grid[1] and " " not in grid[2]:
    printGrid(grid)
    print("Tie")
    break
#player turn
  if q == 1:
    printGrid(grid)
    j = int(input("Pick a row to play (0,2) "))
    f = int(input("Pick a column to play (0,2) "))
    if grid[j][f] == " " and (j < 3 and f < 3):
      grid[j][f] = "x"
      q = 2
    else:
      print("invalid tile")
      q = 1
  
    if wincheck(grid,"x") == True:
      printGrid(grid)
      print("You win")
      break
#Computer turn
  else:
    winmov = False
    # check for computer winning move
    if winmov == False:
      winmov = winningmove(grid,"o","o")
    if winmov == True:
      q =1
      
    #check for player winning move
    if winmov == False:
      winmov =winningmove(grid,"x","o")
    if winmov == True:
      q =1
      
    #check for fork
    if winmov == False:
      winmov = forkChecker(grid,"o","o","x")
    if winmov == True:
      q =1

    
    #check for opponent fork
    if winmov == False:
      winmov = forkChecker(grid,"x","o","o")
    if winmov == True:
      q =1
    #check for center
    if  winmov == False and grid[1][1] == " " :
      grid[1][1] = "o"
      q = 1
      winmov = True
    if winmov == False and grid[0][0] == " ":
      grid[0][0] = "o"
      q = 1
      winmov = True  
    if winmov == False and grid[0][2] == " ":
      grid[0][2] == "o"
      q=1
      winmov == True
    if winmov == False and grid[2][0] == " ":
      grid[2][0] == "o"
      q=1
      winmov == True
    if winmov == False and grid[2][2] == " ":
      grid[2][2] == "o"
      q=1
      winmov == True
    #random
    if winmov == False:
      x = random.randint(0,2)
      y = random.randint(0,2)
      if grid[x][y] == " ":
        grid[x][y] = "o"
        q = 1
      else:
        q = 2

    if wincheck(grid,"o") == True:
      printGrid(grid)
      print("Computer wins")
      break
  
