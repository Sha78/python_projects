#Ch5 pe15
#Description: This program asks a user to enter 5 test scores and returns the letter grade for each score entered.
#The program uses two functions one that determines the grade for each score and one that returns the average of allthe scores entered.
NUMBER_OF_TESTS = 5 #number of tests to calculate

def main(): #defines main funciton
    
    all_scores = 0 #initializes counting total
    each_score = 0
    for score in range(NUMBER_OF_TESTS):#counting loop collects all the scores entered by the user
        each_score = int(input("Enter a test score: "))#user inputs each test score 
        all_scores += each_score#each score is placed in a counting total variable 
        each_score = determine_grade(each_score,)#calls the determine_grade function to be performed.
        total_scores = calc_average(all_scores)#calls the calc_average function to be performed and passes all_scores into the function calc_average to compute average.

    print("The average of all test scores is: ", format(total_scores, '.2F'))#prints the average of all the scores entered by user. 

def calc_average(all_scores): #This function calculates the average scores of a the test scores the user entered.
    average = (all_scores)/NUMBER_OF_TESTS#formula that calculates the average of all the scores.

    return average#returns average from where it was called which is total_scoresin the main function 

def determine_grade(each_score): #This function determines a grade for each score entered.
    if each_score >=90 or each_score ==100:#Checks to see if each_score is within the required scope to print letter grade A 
        print("score",each_score,"Earned a grade letter A")
    elif each_score >=80 or each_score == 89:#Checks to see if each_score is within the required scope to print letter grade B
        print("score",each_score,"Earned a grade letter B")
    elif each_score >=70 or each_score == 79:#Checks to see if each_score is within the required scope to print letter grade C
        print("score",each_score,"Earned a grade letter C")
    elif each_score >=60 or each_score == 69:#Checks to see if each_score is within the required scope to print letter grade D
        print("score",each_score,"Earned a grade letter D")
    elif each_score<60:#Checks to see if each_score is within the required scope to print letter grade F
        print("score",each_score,"Earned a grade letter F")
    else:#If anotehr input is entered that does not meet any requirements for a letter grade user is propted to try again. 
        print("Try again")

    return determine_grade#returns determine_grade from where it was called. Which is in the main function. 

main()
#******************************fotter for CH5 pe15**************************************************************************
# [shaycraf@hills Ch05]$ python3 pe15.py
# Enter a test score: 100
# score 100 Earned a grade letter A
# Enter a test score: 80
# score 80 Earned a grade letter B
# Enter a test score: 70
# score 70 Earned a grade letter C
# Enter a test score: 60
# score 60 Earned a grade letter D
# Enter a test score: 59
# score 59 Earned a grade letter F
# The average of all test scores is:  73.80
# [shaycraf@hills Ch05]$ cat pe15.py
# #Ch5 pe15
# #Description: This program asks a user to enter 5 test scores and returns the letter grade for each score entered.
# #The program uses two functions one that determines the grade for each score and one that returns the average of allthe scores entered.
# NUMBER_OF_TESTS = 5 #number of tests to calculate
# def main(): #defines main funciton

#     all_scores = 0 #initializes counting total
#     each_score = 0
#     for score in range(NUMBER_OF_TESTS):#counting loop collects all the scores entered by the user
#         each_score = int(input("Enter a test score: "))
#         all_scores += each_score
#         each_score = determine_grade(each_score,)#calls the determine_grade function to be performed.
#         total_scores = calc_average(all_scores)#calls the calc_average function to be performed.

#     print("The average of all test scores is: ", format(total_scores, '.2F'))

# def calc_average(all_scores): #This function calculates the average scoer of a the test scores the user entered.
#     average = (all_scores)/NUMBER_OF_TESTS#calculates the average of all the scores.

#     return average#returns average from where it was called

# def determine_grade(each_score): #This function determines a grade for each score entered.
#     if each_score >=90 or each_score ==100:
#         print("score",each_score,"Earned a grade letter A")
#     elif each_score >=80 or each_score == 89:
#         print("score",each_score,"Earned a grade letter B")
#     elif each_score >=70 or each_score == 79:
#         print("score",each_score,"Earned a grade letter C")
#     elif each_score >=60 or each_score == 69:
#         print("score",each_score,"Earned a grade letter D")
#     elif each_score<60:
#         print("score",each_score,"Earned a grade letter F")
#     else:
#         print("Try again")

#     return determine_grade#returns determine_grade from where it was called.

# main()
# [shaycraf@hills Ch05]$