"""
File: weather_master.py
Name:Ray
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100


def main():
	"""
	find the highest temperature
	find the lowest temperature
	find the Average of temperature
	how many days we need to issued the temperature alert
	"""
	print('StanCode "Weather Master 4.0"!')
	data = int(input("Next Temperature: (or -100 to quit)? "))
	if data == EXIT:
		print('No data')
	else:
		maximum = data
		minimum = data
		if data >= 16:
			coldest = 0
		else:
			coldest = 1
		total = data
		d = 1
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data != EXIT:
				total += data
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			if data < 16 != EXIT:
				coldest = coldest + 1
			if data != EXIT:
				d = d + 1
		average = total / d
		print('Highest: ' + str(maximum))
		print('lowest: ' + str(minimum))
		print("Average = " + str(average))
		print(str(coldest) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
