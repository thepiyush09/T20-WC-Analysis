import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
df= pd.read_csv("matches.csv")
#Data Analysis-----------

#Display of Dataset
print(df)
#Display the first few rows of the dataset:
print(df.head())

#Get a summary of the dataset
print(df.info())
print(df.describe())

#Count the number of matches won by each team
matches_won = df['Winning_team'].value_counts()
print(matches_won)

#Analyze the toss decision
toss_decision = df['Toss_decision'].value_counts()
print(toss_decision)

#Analyze match results based on toss decisions
result_by_toss = df.groupby('Toss_decision')['Winning_team'].value_counts()
print(result_by_toss)

#Visualization of Data---------------

#Plot the number of matches won by each team:
plt.figure(figsize=(12, 6))
sns.countplot(y='Winning_team', data=df, order=df['Winning_team'].value_counts().index)
plt.title('Number of Matches Won by Each Team')
plt.xlabel('Number of Matches')
plt.ylabel('Teams')
plt.show()

#Plot the toss decisions:
plt.figure(figsize=(6, 6))
sns.countplot(x='Toss_decision', data=df)
plt.title('Toss Decision Analysis')
plt.xlabel('Toss Decision')
plt.ylabel('Count')
plt.show()

#Plot the match results based on toss decisions:
plt.figure(figsize=(12, 6))
sns.countplot(y='Toss_decision', hue='Winning_team', data=df)
plt.title('Match Results Based on Toss Decisions')
plt.xlabel('Count')
plt.ylabel('Toss Decision')
plt.show()

#Additional Data Analysis--------------------

#Analyze matches with Super Over:
super_over_matches = df[df['Super_over_match'] == 'Yes']
print(super_over_matches)

#Analyze matches by venue:
matches_by_venue = df['Venue_stadium'].value_counts()
print(matches_by_venue)

#Plot the distribution of match results by venue:
plt.figure(figsize=(14, 8))
sns.countplot(y='Venue_stadium', data=df, order=df['Venue_stadium'].value_counts().index)
plt.title('Number of Matches Played at Each Venue')
plt.xlabel('Number of Matches')
plt.ylabel('Venue Stadium')
plt.show()


