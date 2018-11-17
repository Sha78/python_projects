NUMBER_OF_TESTS = 2 #number of tests to calculate
def main(): #defines main funciton 
    
    all_scores = 0 #initializes counting total
    each_score = 0
    for score in range(NUMBER_OF_TESTS):#counting loop collects all the scores entered by the user
       
        each_score = int(input("Enter a test score: "))\
        all_scores += each_score
        each_score += score
        
        
    total_scores = calc_average(all_scores) #this function is placed in a varible to be used to deterine the grade with the determine_grade function. 
    
    print("The average of all test scores is: ", format(total_scores, '.2F'))#prints the average
    determine_grade(each_score)#calls the determine_grade function to be performed
def calc_average(all_scores): #defines calc_average function. this function has an argument of all scores entered from line 10
    average = (all_scores)/NUMBER_OF_TESTS#calculates the average of all scores entered
    return average #returns the average to where is was called
    
def determine_grade(each_score):#defines determine grade. This fucntion has an argument of total_scores which links the calc_average function to it. 
    if each_score >90 or each_score ==100:#reads through conditional statements and does what it is told to do. 
        print("You earned an A")
    elif each_score >80 or each_score == 89:
        print("You earned a B")
    elif each_score >70 or each_score == 79:
        print("You earned a C")
    elif each_score >60 or each_score == 69:
        print("You earned a D")
    elif each_score<60:
        print("You earned a F")
    else:
        print("Try again")
            
        
    return determine_grade#returns determine_grade back to the place it was called. 
    
main()