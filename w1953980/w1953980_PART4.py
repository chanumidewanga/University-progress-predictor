#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
#Any code taken from other sources is referenced within my code solution.

#Student ID : w1953980 
#IIT ID : 20210741
 
#Date: 13.12.2022


#--------------------------PART 4 - DICTIONARY------------------------------

#Declaring variables
ID = ""
PASS = 0
DEFER = 0
FAIL = 0
TOTAL = 0
ID_list = []
contOption = ""
prog_data_list = []
prog_data_dict = {}


#Printing the menu 
print("*"*50)
print("*"*5,"WELCOME! TRACK THE PROGRESSION OUTCOME!","*"*4)
print("*"*50)

#User defined function for getting student ID
def student_ID():
    global ID
    global ID_list
    ID = input("\nEnter the student ID :")
    ID_list.append(ID)
        
#User defined function for getting credits as inputs  
def input_credit():
    global PASS 
    global DEFER 
    global FAIL 
    global TOTAL
    
    #Validating all inputs by calculating the total - loop
    while True:
            
    #Getting pass credits and validating inputs
        while True:
            try:
                PASS = int(input("\nPlease enter the Pass credits : "))
                if PASS not in(0,20,40,60,80,100,120):
                    print("Out of range.\n")
                    continue
            except ValueError:
                print("Integer required.\n")
                continue
            else:
                break


        #Getting defer credits and validating inputs    
        while True:
            try:
                DEFER = int(input("Please enter the Defer credits : "))
                if DEFER not in(0,20,40,60,80,100,120):
                    print("Out of range.\n")
                    continue
            except ValueError:
                print("Integer required.\n")
                continue
            else:
                break
            

        #Getting fail credits and validating inputs
        while True:
            try:
                FAIL = int(input("Please enter the Fail credits : "))
                if FAIL not in(0,20,40,60,80,100,120):
                    print("Out of range.\n")
                    continue
            except ValueError:
                print("Integer required.\n")
                continue
            else:
                break

        #Validating all inputs by calculating the total    
        TOTAL = PASS + DEFER + FAIL
        if TOTAL != 120:
            print("Total incorrect.\n")
            continue
        else:
            break


#User defined function for displaying progression outcomes      
def prog_outcome():

    #Making global variables
    global PASS 
    global DEFER 
    global FAIL 
    global TOTAL
    global prog_data_list

    #Checking credits and displaying "Progress"
    if PASS == 120:
        print("Progress\n")
        
        #Adding the inputted progression data into a list
        prog_data_list=(["Progress - ", PASS, DEFER, FAIL])

    #Checking credits and displaying "Progress (Module Trailer)"
    elif PASS == 100 and DEFER == 20 or FAIL == 20:
        print("Progress (Module Trailer)\n")
        
        #Adding the inputted progression data into a list
        prog_data_list=(["Progress (Module Trailer) - ", PASS, DEFER, FAIL])

    #Checking credits and displaying "Exclude"
    elif FAIL == 80 or FAIL == 100 or FAIL == 120:
        print("Exclude\n")
        
        #Adding the inputted progression data into a list
        prog_data_list=(["Exclude - ", PASS, DEFER, FAIL])

    #Checking credits and displaying "Module retriever"             
    else :
        print("Module retriever\n")
        
        #Adding the inputted progression data into a list
        prog_data_list=(["Module retriever - ", PASS, DEFER, FAIL])


#User defined function for making the dictionary
def dictionary():

    #Making global variables
    global ID
    global ID_list
    global prog_data_list

    prog_data_dict[ID]=prog_data_list


#-----------------------------Main Program------------------------------------
    
#Asking the user to continue or quit the program - loop
while not contOption =='q' or contOption =='Q':
    
    #Calling the user defined functions
    student_ID()
    input_credit()
    prog_outcome()
    dictionary()

    #Asking the user to continue or quit the program
    contOption=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results\n")
    if contOption =='q' or contOption =='Q':
        dictionary()
        #Printing the dictionary
        print("\nPart 4:")
        for i in prog_data_dict.keys():
            print(i,end=' : ')
            marks=(prog_data_dict.get(i))
            print(marks[0],end='')
            marks_temp=str(marks[1:4])[1:-1]
            print(marks_temp)

        #Ending the program        
        print("\nThank you for using our system. Goodbye!")











    
   
