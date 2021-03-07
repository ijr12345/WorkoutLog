#Author: Isabel Rodriguez
#date: 2/25/21
#description: final project. A program that generates a dumbell workout and keeps a workout log for the user.


#PEER REVIEW stuff: 
'''
Any feedback about how to maybe store and access the data more efficiently would be cool or anything that could make the program easier to 
interact with. Open to any and all suggestions.

I'm still trying to figure out how to create a new txt file if it doesn't exist already. So to run the 'view' workout log you're going
to have to create an empty workoutlog.txt file in the same folder as this (i couldn't upload a folder to the discussion post)----if you have any tips let me know!
'''


import random
import sys
import datetime

#dictionary of workout and reps
#specified reps are estimated to be equivalent to about 40 seconds of movement
movements = {
	'exercise1': 'Lunges' , 'reps1': 15 ,
	'exercise2':'Russian twists' , 'reps2': 20 ,
	'exercise3':'Hammer Curls' , 'reps3':12 ,
	'exercise4':'Bicep Curls' , 'reps4': 12 ,
	'exercise5':'Dumbell rows' , 'reps5': 8 ,
	'exercise6': 'Calf raises' , 'reps6': 15 ,
	'exercise7': 'Lying fly', 'reps7': 8 ,
	'exercise8': 'Shoulder shrugs', 'reps8': 15 ,
	'exercise9': 'Tricep extension', 'reps9':12 ,
	'exercise10':'Squats' , 'reps10': 12,
	'exercise11': 'Side Lunges', 'reps11': 10,
	'exercise12': 'Palsms-up wrist Curls', 'reps12': 10 ,
	'exercise13': 'Palsms-down wrist Curls', 'reps13': 10 ,
	'exercise14': 'Alternating bicep Curls', 'reps14': 12,
	'exercise15': 'Shoulder press', 'reps15': 12,
	}


def make_workout(time, exercises ):
	'''Creates a set of exercises based on desired duration of workout
		arguments: time is an integer, exercises is a dicitonary with movements and reps
		return: A list containing exercises and corresponding reps'''

	workout = []
	selected_workout_index = []

	#total workout duration determines number of exercises per set and time length of a set
	if time <=20:
		exercises_per_set = 5
		time_per_set = 5
	else:
		exercises_per_set = 6
		time_per_set = 6

	#add 5 random exercises to the set  
	for i in range(exercises_per_set):

		#generates random index to use within dictionary of exercises
		index = random.randint(1,15)

		#prevents duplicate exercises in the set
		while index in selected_workout_index:
			index = random.randint(1,15)
		selected_workout_index.append(index)

		#adds random exercise and corresponding reps to the set
		index_exercise = 'exercise' + str(index)
		index_exercise_reps = 'reps' + str(index)
		workout.append( [exercises[index_exercise], exercises[index_exercise_reps]] )


		#logic used to calculate number of repeat sets
			#each exercise = 40s, rest between each exercise = 20s
			#if 5 exercises per set, each set = 5min 
			#if 6 exercises per set, each set = 6min

		#number of times a set can be FULLY completed within the desired workout duration
		set_count = time // time_per_set

	#just general workout suggestion to user if their workout is super long
	if time > 60:
		print()
		print('This seems like a really long dumbell workout.......')
		print("I'd reccomend doing a shorter dumbell session and then doing some cardio, but if")
		print("you reallyyyyyy want to do it here's the", str(time), "minute dumbell workout")

	#diplays workout info to user
	print()
	print('Complete ' + str(set_count) + " sets with 20 seconds rest between each exercise and set!")
	for i in range(exercises_per_set):
		print ("	" + str(workout[i][0]) + " " + str(workout[i][1]))
	print()


	return workout




def validate_date(text):
	'''Checks if date is valid
		argument: string containing date in month-day-year format (##-##-####)
		return: true if valid, false if invalid
	'''
	try:
		datetime.datetime.strptime(text, '%m-%d-%Y')
		return True
	#if date isnt valid or doesnt match format datetime function raises error which then makes this function return false 
	except ValueError:
		return False


def log_workout(duration):
	''' writes the workout duration and date into a saved text file called workoutlog.txt
		arguments: duration should be an integer 
	'''

	#continuously asks user for date until they input a valid date one
	invalid_date = True
	while invalid_date:
		#prompts user for date
		date = input('Input workout date (##-##-####): ')

		#checks format was properly used (2 numbers to represent day and month even if the month is single digit) 
		if len(date) == 10:

			#checks if date is valid
			if validate_date(date) == True:
				invalid_date = False
			#tells user if date input is invalid
			else:
				print('Please enter a valid date in the given format')

		else:
			print('Please enter a valid date in the given format')



	#creates a string with date and workout duration to be put into the log
	workout_info = (str('\n')+ str(date) + str(' ---------- ') +str(duration) +str(' minutes'))

	#make a file or use existing file
	log = open('workoutlog.txt', 'a')

	#add date and duration to file
	log.writelines(workout_info)

	#close file
	log.close()


def display_log():
	''' Displays the workout information from saved textfile called workoutlog.txt
	'''
	#open file
	log = open('workoutlog.txt', 'r')

	#tells user there if they dont have any logged workouts 
	if not log.read(1):
		print ("\nYou don't have any saved workouts. Get working!\n")
	else:
		#display the dates and durations of saved workouts
		print('\nWORKOUTLOG')
		print ('Date ---------------- Workout Duration')
		print(log.read())
		print()

	#close file
	log.close()


def get_action(actions):
	""" prompts user with specified action options. checks that user chooses valid action from given options. returns the action the user selected
		arguments: a list containing user action options (W, S, V, Q)
	"""

	#viable user action prompts
	ask_user= 'Type '
	workout = '[W] to generate a workout, '
	save = '[S] to save your workout, '
	viewlog = '[V] to view your workout log, '
	quit = 'or [Q] to quit the program: '
	
	#adds the desired user action prompts based on what actions were specified in the argument
	if 'W' in actions:
		ask_user = ask_user + workout
	if 'S' in actions:
		ask_user = ask_user + save
	if 'V' in actions:
		ask_user = ask_user +viewlog
		
	#the user will always have the option to quit the program
	ask_user = ask_user + quit

	#continuously ask user for action input until valid entry is made
	while True:
		user_action = input(ask_user)

		if user_action.upper() in actions:
			return (user_action.upper())

		else:
			print('This is not a valid option')




#code to run whole workout program
def main():
	#welcomes user
	print('Lets Workout!')
	
	#tells user how they can interact with the program
	user_action = get_action(['W', 'V', 'Q'])


	#continuously allows user to interact with program
	while True: 
		#generates random workout
		if user_action == 'W':

			#asks user for workout specs and makes workout
			#duration = int(input('Enter your desired workout duration (minutes): '))

			invalid_duration = True
			while invalid_duration:
				duration = input('Enter your desired workout duration (minutes): ')
				
				if duration.isnumeric() == True:
					invalid_duration = False 
				else:
					print('Invalid duration\n')


			make_workout(int(duration), movements)

			#prompts user action including saving the workout 
			user_action = get_action(['W','S','V','Q'])

			#saves workout then prompts user for further action
			if user_action == 'S':
				log_workout(duration)
				user_action = get_action(['W', 'V', 'Q'])
				
		#will diplay workout log to user
		if user_action == 'V':
			display_log()
			user_action = get_action(['W', 'Q'])


		#will end program when Q is typed
		if user_action == 'Q':
			print('Goodbye:)')
			sys.exit(0)


#calls main function
if __name__ == "__main__":
	main()
