"""
Graphing Code snippets that were helpful. 

"""

#Graph one file
jsonFile = "test.csv"
dataReddit = pd.read_csv(jsonFile)

#Graph just retweets and timestamps
dfR = pd.DataFrame(dataReddit, columns = ['Date', 'b'])
dfR.columns=['Date', 'a/b/c']
#print dfR

#pd.Timestamp(datetime(2012, 5, 1))
dfR['Date'] = pd.to_datetime(dfR['Date'])
dfR.index = dfR['Date']

#del dfR['Date']
#print dfR


#df.plot(style='.-')
retweets = dfR.plot(style='.-')

plt.tight_layout()
retweetsImage = retweets.get_figure()
retweetsImage.savefig('testing.png')

#Graph multiple (line)
fig = plt.figure()

ax = dfF.plot(style='.-')
ax2 = dfT.plot(ax=ax, style='.-')
ax3 = dfR.plot(ax=ax2, style='.-')

#Relabel legend
ax3.legend(["test", "test2", "test3"]);
ax3.set_yscale('log', basey=2)
retweetsImage = ax3.get_figure()
retweetsImage.savefig('testing.png')


#To be continued


