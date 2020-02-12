#Author: Jeet Shah

#Importing required libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Reading csv file
file1_path = "C:/Users/inspiron/Desktop/CHARUSAT/Sem-5/Software Group Project/"
matches_ipl = pd.read_csv(file1_path+"matches.csv")

file2_path = "C:/Users/inspiron/Desktop/CHARUSAT/Sem-5/Software Group Project/"
balls_ipl = pd.read_csv(file2_path+"deliveries.csv")


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')


def see_records():
	print("Reading First 5 records of file to check if file is successfully read or not")
	print(matches_ipl.head(5))
	return 0

#Code for some basic statistical data 
def basic_stats():
	print("Total Number of Matches played in IPL to date are:"+str(matches_ipl['id'].count()))
	print("Total Seasons done of Indian Premier League till 2019 are:"+str(len(matches_ipl['season'].unique())))
	print("Teams that have participated in IPL in any season are:")
	print(matches_ipl['team1'].unique())
	print("Total teams that have participated in IPL in any season is:"+str(len(matches_ipl['team1'].unique())))
	return 0




#DLS method is used incase the match is shortened due to any issues natural/artificial i.e. No full overs are bowled
def dls_applied():
	print("The number of matches in which DLS method is applied:"+str(matches_ipl['dl_applied'].sum()))
	return 0


def max_win_runs():
	print("Team Winning by Maximum Runs:"+str(matches_ipl['win_by_runs'].max()))
	return 0


def top_venues():
	print("Top 5 venues with most number of matches in IPL history are: \n" + str(matches_ipl['venue'].value_counts().head(5)))
	return 0


def toss_decision():
	print("Toss Decision from " + str(matches_ipl['id'].count())+ " matches in IPL are \n"+str(matches_ipl['toss_decision'].value_counts()))
	return 0


def mom():
	print("Top 5 Players on the basis of Maximum Man of The Match Awards:\n" + str(matches_ipl['player_of_match'].value_counts().head(5)))
	return 0



def graph_mom():
	mom = matches_ipl['player_of_match'].value_counts().head(5)
	plt.plot(mom)
	plt.show()
	return 0



def superover():
	print("Total Number of Matches in which Super Over was bowled:"+str(matches_ipl[matches_ipl['result']=="tie"]['result'].count()))
	return 0

def max_number():
	print("The season which witnessed Maximum Number of Matches:\ns"+str(matches_ipl['season'].value_counts().head(1)))
	return 0

def max_cities():
	print("The Cities which have hosted a IPL match are:\n"+str(matches_ipl['city'].value_counts()))
	return 0

def season_win():
	print("Season wise Winners \n")
	print(matches_ipl.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']].reset_index(drop=True))
	return 0

def graph_match():
	sns.countplot(x='season',data=matches_ipl)
	plt.title('Matches vs Season')
	plt.show()
	return 0

def graph_city():
	sns.countplot(y='city',data=matches_ipl)
	plt.xlabel('Matches')
	plt.ylabel('Cities')
	plt.title('City-wise Matches ')
	plt.show()
	return 0

def graph_home():
	temp_data = pd.melt(matches_ipl,id_vars=['id','season'],value_vars=['team1','team2'])
	sns.countplot(y='team1',data=matches_ipl)
	plt.xticks(rotation='vertical')
	plt.title('Home Matches')
	plt.show()
	return 0

def graph_away():
	temp_data = pd.melt(matches_ipl,id_vars=['id','season'],value_vars=['team1','team2'])
	sns.countplot(y='team2',data=matches_ipl)
	plt.xticks(rotation='vertical')
	plt.title('Away Matches')
	plt.show()
	return 0

def graph_maximum_wins():
	temp_data = pd.melt(matches_ipl,id_vars=['id','season'],value_vars=['team1','team2'])
	sns.countplot(y="winner",data=matches_ipl)
	plt.title("Maximum Wins")
	plt.show()
	return 0

def virat_kohli():
	print("Balls Virat Kohli has faced during IPL(2008-2016):"+str(balls_ipl[balls_ipl['batsman']=='V Kohli']['batsman'].value_counts()))
	return 0


#Top Run Scorers in IPL
def top_run_scorers():
	temp_df = balls_ipl.groupby('batsman')['batsman_runs'].agg('sum').reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['batsman'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['batsman_runs']), width=width, color='blue')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Top run scorers in IPL")
	autolabel(rects)
	plt.show()
	return 0

#Batsman with maximum 4's
def maximum4s():
	temp_df = balls_ipl.groupby('batsman')['batsman_runs'].agg(lambda x: (x==4).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['batsman'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['batsman_runs']), width=width, color='green')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Batsman with most number of 4's")
	autolabel(rects)
	plt.show()
	return 0

#Batsman with maximum 6's
def maximum6s():
	temp_df = balls_ipl.groupby('batsman')['batsman_runs'].agg(lambda x: (x==6).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['batsman'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['batsman_runs']), width=width, color='m')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Batsman with most number of sixes.!")
	autolabel(rects)
	plt.show()
	return 0

def toss_winner_match():
	toss_match = matches_ipl['toss_winner'] == matches_ipl['winner']
	toss_match.groupby(toss_match).size()
	sns.countplot(toss_match)
	plt.title('Toss Winner is Match Winner')
	plt.show()
	return 0


#Batsman with max dot balls
def maximumdots():
	temp_df = balls_ipl.groupby('batsman')['batsman_runs'].agg(lambda x: (x==0).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['batsman'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['batsman_runs']), width=width, color='c')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Batsman with most number of dot balls.!")
	autolabel(rects)
	plt.show()
	return 0

#Bowler who has bowled maximum balls
def maximumballs():
	temp_df = balls_ipl.groupby('bowler')['ball'].agg('count').reset_index().sort_values(by='ball', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['bowler'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['ball']), width=width, color='cyan')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Top Bowlers - Number of balls bowled in IPL")
	autolabel(rects)
	plt.show()
	return 0

#Bowler with maximum dot balls
def bowlerdots():
	temp_df = balls_ipl.groupby('bowler')['total_runs'].agg(lambda x: (x==0).sum()).reset_index().sort_values(by='total_runs', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['bowler'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['total_runs']), width=width, color='yellow')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Top Bowlers - Number of dot balls bowled in IPL")
	autolabel(rects)
	plt.show()
	return 0

#Bowlers who has given more extras
def extras():
	temp_df = balls_ipl.groupby('bowler')['extra_runs'].agg(lambda x: (x>0).sum()).reset_index().sort_values(by='extra_runs', ascending=False).reset_index(drop=True)
	temp_df = temp_df.iloc[:10,:]
	labels = np.array(temp_df['bowler'])
	ind = np.arange(len(labels))
	width = 0.9
	fig, ax = plt.subplots()
	rects = ax.bar(ind, np.array(temp_df['extra_runs']), width=width, color='magenta')
	ax.set_xticks(ind+((width)/2.))
	ax.set_xticklabels(labels, rotation='vertical')
	ax.set_ylabel("Count")
	ax.set_title("Bowlers with more extras in IPL")
	autolabel(rects)
	plt.show()
	return 0


#Commom Dismissal Types
def dismissal_kinds():
	plt.figure(figsize=(12,6))
	sns.countplot(x='dismissal_kind', data=balls_ipl)
	plt.xticks(rotation='vertical')
	plt.show()
	return 0


print("Select the Stats you want to see...(select the number corresponding to it)")

while(1):
	print("\t\t1.See the first 5 full records")
	print("\t\t2.Basic statistical data of IPL")
	print("\t\t3.Number of matches in which DLS has been applied")
	print("\t\t4.Team winning by maximum runs")
	print("\t\t5.Venues with maximum number of matches")
	print("\t\t6.Toss Decisions")
	print("\t\t7.Top 5 Man of the Match")
	print("\t\t8.Graph of Man of the Match")
	print("\t\t9.Total Super Overs")
	print("\t\t10.Season which had max matches")
	print("\t\t11.Cities which has hosted maximum matches")
	print("\t\t12.Season Wise Winners")
	print("\t\t13.Graph of Total Matches")
	print("\t\t14.Graph of City Wise Matches")
	print("\t\t15.Graph of Home Matches")
	print("\t\t16.Graph of Away Matches")
	print("\t\t17.Maximum Wins Graph")
	print("\t\t18.Number of balls Virat Kohli has faced")
	print("\t\t19.Top Run Scorers")
	print("\t\t20.Batsman with maximum 4's")
	print("\t\t21.Batsman with maximum 6's")
	print("\t\t22.Batsman who has played maximum dot balls")
	print("\t\t23.Bowlers with Maximum Balls bowled")
	print("\t\t24.Bowlers with maximum dots")
	print("\t\t25.Bowlers who has given maximum extras")
	print("\t\t26.Graph of Dismissal Kinds")
	print("\t\t27.Toss Winner is Match Winner")
	print("\t\t28.-----EXIT------")

	number = int(input("Enter the Number:"))

	if number == 1:
		see_records()
	elif number == 2:
		basic_stats()
	elif number == 3:
		dls_applied()
	elif number == 4:
		max_win_runs()
	elif number == 5:
		top_venues()
	elif number == 6:
		toss_decision()
	elif number == 7:
		mom()
	elif number == 8:
		graph_mom()
	elif number == 9:
		superover()
	elif number == 10:
		max_number()
	elif number == 11:
		max_cities()
	elif number == 12:
		season_win()
	elif number == 13:
		graph_match()
	elif number == 14:
		graph_city()
	elif number == 15:
		graph_home()
	elif number == 16:
		graph_away()
	elif number == 17:
		graph_maximum_wins()
	elif number == 18:
		virat_kohli()
	elif number == 19:
		top_run_scorers()
	elif number == 20:
		maximum4s()
	elif number == 21:
		maximum6s()
	elif number == 22:
		maximumdots()
	elif number == 23:
		maximumballs()
	elif number == 24:
		bowlerdots()
	elif number == 25:
		extras()
	elif number == 26:
		dismissal_kinds()
	elif number == 27:
		toss_winner_match()
	elif number == 28:
		exit(0)
	else:
		print("Invalid Choice")

