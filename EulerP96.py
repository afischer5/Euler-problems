#Euler P96
#Reads sudolu puzzles from a text file, solves them, then sums the top left 3 digit numbers for all puzzles

#define the solve a puzzle function that returns the first 3 digit number
def solve(puzzle):
    for y in puzzle:
        for x in y:
            possible numbers = [1,2,3,4,5,6,7,8,9]
            


with open ("C:\\Users\\Andrew\\Desktop\\p096_sudoku.txt") as file:
    lines = file.readlines()

#sperate the lines into puzzles
    puzzles = []
    puzzle = []
    for i in range(len(lines)):
        row = []
        
        if "Grid" in str(lines[i]):
            puzzles.append(puzzle)
            puzzle = []
            continue
    
        for num in lines[i].strip():
            row.append(int(num))
            
        puzzle.append(row)

    total = 0

    #go through each puzzle solve it and add the first three digit number to total
   """for n in puzzles:

        total += solve(puzzle[n])
    """
    file.close()
