
def get_answers(filename):


  def mian():
#   student_answers = []
#   test_answers= []
    total_correct_answers = 0
    total_incrrect_answers = 0 
    incorect_question_numbers = [] 
    solutions_input =  open('test_solution.txt', 'r')
    stud
    ent_input = open('test_student.txt', 'r')

    solution_answers = get_answers('test_solution.txt', 'r')
    student_answers = get_answers('test_student.txt', 'r')

    print(student_answers)
    print(student_solution)
  
  
  try:
    for answer in solution_input:
      solution_answers.append(answer.rstrip('\n'))
    for answer in  stident_input:
      student_answers.append(answer.rstrip('\n'))
      solution_input.close()
      
    except FileNotFound as err:
      print('file not found.')
    return anser_list
      
      
  
  
  main()