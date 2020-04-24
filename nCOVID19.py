import argparse
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates


def Q1(filename):

	data = pd.read_csv(filename, parse_dates = ["ObservationDate"])
	data.columns = ["SNo", "ObservationDate", "State", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
	data = data.set_index("ObservationDate")
	day_sum = data.resample("D").sum()

	# Plot
	plt.figure(dpi=128,figsize=(20,10))
	plt.title("nCOVID19-Number of confirmed / recovered / deaths worldwide")
	plt.xlabel("Date")
	plt.ylabel("Number of people")
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=8))
	y = range(0,2500000,250000)
	plt.yticks(y)
	plt.plot(day_sum.index,day_sum.Confirmed,color = "b", marker='x', label="Confirmed")
	plt.plot(day_sum.index,day_sum.Deaths,color = "r", marker='.', label="Deaths")
	plt.plot(day_sum.index,day_sum.Recovered,color = "g", marker='o', label="Recovered")
	plt.legend(loc='upper left')
	
	plt.savefig("question1.png")
	plt.show()



def Q2(filename):

	data = pd.read_csv(filename, parse_dates = ["ObservationDate"])
	data.columns = ["SNo", "ObservationDate", "State", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
	data = data.set_index("ObservationDate")
	day_sum = data.resample("D").sum()

	everyday_Confirmed = []
	everyday_Confirmed.append(None)
	everyday_Deaths = []
	everyday_Deaths.append(None)
	everyday_Recovered = []
	everyday_Recovered.append(None)

	for i in range(1,89):
		everyday_Confirmed.append(day_sum.Confirmed[i]-day_sum.Confirmed[i-1])

	for i in range(1,89):
		everyday_Deaths.append(day_sum.Deaths[i]-day_sum.Deaths[i-1])

	for i in range(1,89):
		everyday_Recovered.append(day_sum.Recovered[i]-day_sum.Recovered[i-1])

	# Plot
	plt.figure(dpi=128,figsize=(20,10))
	plt.title("nCOVID19-Increasing number of confirmed / recovered / deaths worldwide")
	plt.xlabel("Date")
	plt.ylabel("Number of people")
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=8))
	y = range(0,100000,5000)
	plt.yticks(y)
	plt.plot(day_sum.index,everyday_Confirmed,color = "b", marker='x', label="Daily increase Confirmed")
	plt.plot(day_sum.index,everyday_Deaths,color = "r", marker='.', label="Daily increase Deaths")
	plt.plot(day_sum.index,everyday_Recovered,color = "g", marker='o', label="Daily increase Recovered")
	plt.legend(loc='upper left')
	
	plt.savefig("question2.png")
	plt.show()


def Q3(filename):

	data = pd.read_csv(filename, parse_dates = ["ObservationDate"])
	data.columns = ["SNo", "ObservationDate", "State", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
	data = data.set_index("ObservationDate")
	day_sum = data.resample("D").sum()

	everyday_Confirmed = []
	everyday_Confirmed.append(None)
	everyday_Deaths = []
	everyday_Deaths.append(None)
	everyday_Recovered = []
	everyday_Recovered.append(None)

	for i in range(1,89):
		everyday_Confirmed.append((day_sum.Confirmed[i]-day_sum.Confirmed[i-1])/day_sum.Confirmed[i])

	for i in range(1,89):
		everyday_Deaths.append((day_sum.Deaths[i]-day_sum.Deaths[i-1])/day_sum.Deaths[i])

	for i in range(1,89):
		everyday_Recovered.append((day_sum.Recovered[i]-day_sum.Recovered[i-1])/day_sum.Recovered[i])
	
	# Plot
	plt.figure(dpi=128,figsize=(20,10))
	plt.title("nCOVID19-Increasing rate of confirmed / recovered / deaths worldwide")
	plt.xlabel("Date")
	plt.ylabel("Rate")
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=8))
	plt.yticks([0, 0.1, 0.2, 0.3, 0.4],
			[r'$0$', r'$20$', r'$40$', r'$60$', r'$80$'])
	plt.plot(day_sum.index,everyday_Confirmed,color = "b", marker='x', label="Daily increase Confirmed rate")
	plt.plot(day_sum.index,everyday_Deaths,color = "r", marker='.', label="Daily increase Deaths rate")
	plt.plot(day_sum.index,everyday_Recovered,color = "g", marker='o', label="Daily increase Recovered rate")
	plt.legend(loc='upper left')
	
	plt.savefig("question3.png")
	plt.show()




if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("question",type=str)
	args = parser.parse_args()
	filename = "covid_19_data.csv"

	if args.question[0]=="1":
		print("Question1") 
		Q1(filename) 

	elif args.question[0]=="2":
		print("Question2")
		Q2(filename) 
	
	elif args.question[0]=="3": 
		print("Question3")
		Q3(filename) 