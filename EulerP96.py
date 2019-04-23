#Euler P96
#Reads sudolu puzzles from a text file, solves them, then sums the top left 3 digit numbers for all puzzles



#refactor whole thing for a list[][] rather than list [[],[],[],...]????
#define the solve a puzzle function that returns the first 3 digit number
def solve(puzzle):
    for row in puzzle:
        for x in row:
            if x == 0:
                possibleNumbers = [1,2,3,4,5,6,7,8,9]

                #check the same row
                for i in row:
                    if i in possibleNumbers:
                        possibleNumbers.remove(i)

                #check the same collumn
                for i in puzzle:
                    if i[x] in possibleNumbers:
                        possibleNumbers.remove(i[x])

                #check in the 3x3 tiles
                for 


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
    #for n in puzzles:

        #total += solve(puzzle[n])

    solve(puzzles[1])
    file.close()
