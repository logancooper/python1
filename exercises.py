##VARIABLES##
welcome_message = "What is your name? "
greeting_message = "Hello,"
letters_message = "Number of letters in your name: "

##GREETING FUNCTION##
def greeting():
    name = input(welcome_message.upper())
    print(greeting_message.upper() + name.upper())
    print(letters_message.upper() + str(len(name)))

##UPDATE/RUN/LOGIC##
greeting()
