#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
#Any code taken from other sources is referenced within my code solution.

#Student ID : w1953980
#IIT ID : 20210741
 
#Date: 13.12.2022

#-----------------------------PART 1----------------------------------

#Declaring variables
user = 0
PASS = 0
DEFER = 0
FAIL = 0
TOTAL = 0
pro = 0
mod_t = 0
mod_r = 0
excld = 0
contOption = ""
prog_data_list = []


#Displaying the menu heading 
print("*"*50)
print("*"*5,"WELCOME! TRACK THE PROGRESSION OUTCOME!","*"*4)
print("*"*50)

#Selecting the user (Student or Staff)
while True:
    try:
        print("\nYou are,\n\t1 - Student\n\t2 - Staff")
        user = int(input("\nPlease enter the number to proceed:"))
        if user != 1 and user != 2:
            print ("Invalid integer.Try again.")
            continue
    except ValueError:
        print("Invalid input. Try again.")
        continue
    else:
        break
     
#User defined function for getting credits as inputs
def input_credit():
    #Making global variables
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
    global pro
    global mod_t
    global mod_r
    global excld

    #Checking credits and displaying "Progress"
    if PASS == 120:
        print("Progress\n")
        pro = pro + 1
        
        #Adding the inputted progression data into a list
        prog_data_list.append(["Progress - ", PASS, DEFER, FAIL])

    #Checking credits and displaying "Progress (Module Trailer)"
    elif PASS == 100 and DEFER == 20 or PASS == 100 and FAIL == 20:
        print("Progress (Module Trailer)\n")
        mod_t = mod_t + 1

        #Adding the inputted progression data into a list
        prog_data_list.append(["Progress (Module Trailer) - ", PASS, DEFER, FAIL])

    #Checking credits and displaying "Exclude"
    elif FAIL == 80 or FAIL == 100 or FAIL == 120:
        print("Exclude\n")
        excld = excld + 1

        #Adding the inputted progression data into a list
        prog_data_list.append(["Exclude - ", PASS, DEFER, FAIL])

    #Checking credits and displaying "Module retriever"     
    else :
        print("Module retriever\n")
        mod_r = mod_r + 1

        #Adding the inputted progression data into a list
        prog_data_list.append(["Module retriever - ", PASS, DEFER, FAIL])


#User defined function for printing histogram
def histogram():
    #Making global variables
    global pro 
    global mod_t
    global mod_r 
    global excld

    #Printing the heading
    print("-"*50)
    print("Histogram")

    #Printing the histogram
    print("Progress",(pro)," :",end="")
    for i in range (pro):
        print ("*",end="")

    print("\nTrailer",(mod_t),"  :",end="")
    for i in range (mod_t):
        print ("*",end="")

    print("\nRetriever",(mod_r),":",end="")
    for i in range (mod_r):
        print ("*",end="")

    print("\nExcluded",(excld)," :",end="")
    for i in range (excld):
        print ("*",end="")
        
    print("\n", end="")
    print(pro + mod_t + mod_r + excld,"outcomes in total.")

    print("-"*50)



#---------------------------PART 2 - List-----------------------------

#User defined function for displaying outputs in a list
def display_output():
    #Making global variables
    global prog_data_list

    #Printing the values stored in the list
    print("Part 2:")
    for i in (prog_data_list):
        print(i[0],end="")
        #temporarily storing elements in string format
        prog_data_list2=str(i[1:4])[1:-1]
        print (prog_data_list2)


#-------------------------PART 3 - Text file-----------------------------
        
#User defined function for saving progression data to a text file
def text_file():
    global prog_data_list
    f = 0
    f = open("prog_data_text.txt","w")

    #Writing the progression data into a text file
    for i in prog_data_list:
        f.write(i[0])
        #temporarily storing elements in string format
        prog_data_list2=str(i[1:4])[1:-1]
        f.write(prog_data_list2)
        f.write("\n")
    f.close()

    #Reading the progression data from file and printing
    print("\nPart 3:")
    f=open("prog_data_text.txt","r")
    for j in f:
        print(j,end='')
    f.close()



#-----------------------------MAIN PROGRAM-------------------------------
        
#Student's version
if user == 1:
    #Calling the functions
    input_credit()
    prog_outcome()
    display_output()
    text_file()

    #Ending the program
    print("\nThank you for using our system.Good luck with your studies!")
        
#Staff version
if user == 2:
    #Asking the user to continue or quit the program
    while not contOption =='q' or contOption =='Q':
        input_credit()
        prog_outcome()
        contOption=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results\n")
        if contOption =='q' or contOption =='Q':
            histogram()
            display_output()
            text_file()
            
            
            #Ending the program
            print("\nThank you for using our system. Goodbye!")











    
   
