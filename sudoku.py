import time
class Sudoku:
  
  def __init__(self):
    self.puzzle = []
    for i in range(9):
        self.puzzle.append([])
        for j in range(9):
            self.puzzle[i].append(0)
            
  def print(self):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in self.puzzle]))
    
  def set_puzzle(self, string):
    if len(string)==81:
      idx=0
      for i in range(9):
        for j in range(9):
          if string[idx]!= '.':
            self.puzzle[i][j] = int(string[idx])
          idx+=1
    else:
      return
  
  def is_conflict_assign(self, x, y, val):
    #same row
    for i in range(9):
      if self.puzzle[x][i]==val:
        return True
    #same col
    for i in range(9):
      if self.puzzle[i][y]==val:
        return True
    #same subset
    for i in range(3):
      for j in range(3):
        if(self.puzzle[i+(x-x%3)][j+(y-y%3)]==val):
          return True
    return False
  
  def find_unassigned(self):
    for i in range(9):
      for j in range(9):
        if self.puzzle[i][j]==0:
          return (i,j)
    return None
  
  def solve(self):
    pos = self.find_unassigned()
    if(pos==None):
      return True
    for k in range(1,10):
      if self.is_conflict_assign(pos[0],pos[1],k)==False:
        self.puzzle[pos[0]][pos[1]] = k
        if self.solve():
          return True
        self.puzzle[pos[0]][pos[1]] = 0
    return False
  
###############################################################    
hard = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
p = Sudoku()
p.set_puzzle(hard)
p.print()
print()
before = time.time()
p.solve()
after = time.time();
p.print()
print('Demorou',after-before,'segundos')

