def main():
    # Prompt user to enter filenames
    boy_file = input("Open the Boy name file: ")
    girl_file = input("Open the Girl name file: ")

    try:
        # Opens both files
        inputFile = open(boy_file, 'r')
        inputFile2 = open(girl_file, 'r')

        # Read contents of both files into separate lists
        boy_names = inputFile.readlines()
        girl_names = inputFile2.readlines()

        # Remove newline characters from both lists
        boy_names = [name.rstrip() for name in boy_names]
        girl_names = [name.rstrip() for name in girl_names]

        # Close both files
        inputFile.close()
        inputFile2.close()

        # Ask user to search for a boy's name
        BoyName = input("What boy name do you want to look up? ")
        if BoyName in boy_names:
            print(f"{BoyName} made the list of popular boy names.")
        else:
            print(f"{BoyName} did not make the list of popular boy names.")

        # Ask user to search for a girl's name
        GirlName = input("What girl name do you want to look up? ")
        if GirlName in girl_names:
            print(f"{GirlName} made the list of popular girl names.")
        else:
            print(f"{GirlName} did not make the list of popular girl names.")

    except:
        print("wrong file")

main()
   





                                     
                        
        
            
                                    
                                    
        
