#Gets size of grid from the user and returns it to the caller
def get_grid_size():                                                        
    grid_size=int(input("Enter Grid size of your Tic-Tac-Toe game : "))
    return grid_size

#Prints the grid of given input grid_size     
def generate_grid(grid_size):       
    for i in range(grid_size):
        for j in range(grid_size-1):
           print("    |", end="") 
        print()   
        if i!=grid_size-1:
            for k in range(grid_size):   
                print(" -- ", end=" ") 
        print("")   

#Main function
def main(): 
    print("\n", "TIC-TAC-TOE GRID GENERATOR", "\n")
    grid_size=get_grid_size()
    print()
    generate_grid(grid_size)

main()    