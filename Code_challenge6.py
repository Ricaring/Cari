prelim = float(input("Enter your prelim grade: "))
midterm = float(input("Enter your midterm grade: "))
semifinals = float(input("Enter your semifinals grade: "))
finals = float(input("Enter your finals grade: "))
quiz = float(input("Enter your quiz grade: "))
project = float(input("Enter your project grade: "))

if (65 <= prelim <= 100) and (65 <= midterm <= 100) and (65 <= semifinals <= 100) and (65 <= finals <= 100) and (65 <= quiz <= 100) and (65 <= project <= 100):
	final_grade = (prelim * 0.15) + (midterm * 0.15) + (semifinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.25)
	if final_grade >= 75:
		print("You nailed it, you have passed the exam!")
	else:
		print("Apologies, you have failed the exam.")