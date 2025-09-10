#Prompt the user for input: subject, course and schedule
subject = input('What subject do you study? ')
courseName = input('What is the name of the course?')
courseSchedule = input('When is your course?')

#Format a string using the input from the user, mixing literal characters with program variables
helloMsg = 'Hello %s world' % subject
courseMsg = '{0} with Python'.format(courseName)
seeYouMsg = f'See you on {courseSchedule}'

#Present the three messages to the user: hello, course message, see you message
print(helloMsg)
print(courseMsg)
print(seeYouMsg) 
 

