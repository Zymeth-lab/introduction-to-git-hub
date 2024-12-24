def main():

    filename = input("Enter the name of the file: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            print(f"The file contains {len(lines)} lines.")
            
            while True:
                line_number = int(input("Enter a line number to view (or 0 to quit): "))
                
                if line_number == 0:
                    break
                
                if 1 <= line_number <= len(lines):
                    print(lines[line_number - 1])
                else:
                    print("Invalid line number. Please enter a number between 1 and", len(lines), "or 0 to quit.")
    
    except FileNotFoundError:
        print("The file was not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
