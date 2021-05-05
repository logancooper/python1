##VARIABLES
welcome_message = "Please fill in the blanks below: "
name_question = "What is your name? "
subject_quesiton = "What is you favorite subject? "

##FUNCTIONS
def madlib():
    name = input(name_question)
    subject = input(subject_quesiton)
    print("%s's favorite subject in school is %s" %(name,subject))

##UPDATE/RUN/LOGIC
madlib()