# Import statements
import unittest
import sqlite3
import twitter_info # still need this in the same directory, filled out
import matplotlib.pyplot as plt

## [PART 1]
def getDayDict(cur):
	cur.execute('SELECT time_posted FROM Tweets')
	data = cur.fetchall()
	dayDict = {}
	sun = 0
	mon = 0
	tue = 0
	wed = 0
	thu = 0
	fri = 0
	sat = 0
	for row in data:
		day = row[0][0:3]
		if day == "Sun":
			sun += 1
		elif day == "Mon":
			mon += 1
		elif day == "Tue":
			tue += 1
		elif day == "Wed":
			wed += 1
		elif day == "Thu":
			thu += 1
		elif day == "Fri":
			fri += 1
		elif day == "Sat":
			sat += 1

	dayDict["Sun"] = sun
	dayDict["Mon"] = mon
	dayDict["Tue"] = tue
	dayDict["Wed"] = wed
	dayDict["Thu"] = thu
	dayDict["Fri"] = fri
	dayDict["Sat"] = sat

	retun(dayDict)
  
## [Part 2]
def drawBarChart(dayDict):
	def drawBarChart(dayDict):
	day_list = dayDict.keys()
	tweet_list = dayDict.values()

	plt.bar(day_list,tweet_list)
	plt.title("Number of Tweets Per Week Day")
	plt.xlabel("Week Day")
	plt.ylabel("Number of Tweets")
	plt.savefig('bar.png')

## [Part 3]
## Create unittests to test the function
# Finish writing the unittests.  Write the setUp function which will create the database connection 
# to 'tweets.sqlite' and the cursor.  Write the tearDown function which closes the database connection.  
# Write the test_getDayDict function to test getDayDict by comparing the returned dictionary to the 
# expected value.  Also call drawBarChart in test_getDayDict. 
class TestHW10(unittest.TestCase):

# run the main method
if __name__ == "__main__":
    unittest.main(verbosity=2)
