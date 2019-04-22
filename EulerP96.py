#Euler P96
#Reads sudolu puzzles from a text file, solves them, then sums the top left 3 digit numbers for all puzzles
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
        
    #print(puzzles)
    print(puzzles[1])

    file.close()
