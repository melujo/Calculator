import sys
import functions
import types

'''
The entry-point of our application.
'''
def main():
    
    # Indicates whether or not our application should quit
    quit = False



    # Implement basic functionality
  
if __name__== "__main__":
    main()
ans = "0"
run = True
while run:
    command = input()
    if command == "version":
        print("calculator version 0.1")
    elif command == "help":
        functions.print_functions()
    elif command == "quit":
        run = False
    else:
        if "ans" in command:
            command = command.replace("ans",str(ans))
        ans = functions.process_line(command)
        print(ans)