import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
                                Metanote:
Function calls are collected at the end of this document.
DataFrame loading and function definitions occur first.
'''

# load rankings data here:
wood_coasters = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_coasters = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# Let's get the info. for each column of each DataFrame:
print(wood_coasters.info())
print(steel_coasters.info())

# I know that one top-ranked wood roller coaster is sometimes listed 
# as "The Voyage" and sometimes as "Voyage." Let's replace all
# instances of "The Voyage" with "Voyage." 
wood_coasters.Name = wood_coasters.Name.replace('The Voyage', 'Voyage')

# There are two El Toro roller coasters: one in NJ and one in Germany. Rather
# than having to make a bunch of special cases and other kludges, let's just
# rename the German El Toro roller coasters. First get the rows containing
# entries for the German El Toro roller coaster, then replace the Name entry
# in those rows:

secondeltoro = wood_coasters[(wood_coasters.Name == 'El Toro') & \
                                                   (wood_coasters.Location == "Legendfeld, Germany")]
#print(secondeltoro)

wood_coasters.loc[55, 'Name'] = "El Toro German"
wood_coasters.loc[120,'Name'] = "El Toro German"

# Looking at the steel roller coasters, there are two Bizarros: one in MA and one in NJ. Let's
# rename the N.J. one, using the same procedure as above:

secondbizarro= steel_coasters[(steel_coasters.Name == 'Bizarro') & \
                                                   (steel_coasters.Location == "Jackson, N.J.")]
#print(secondbizarro)

steel_coasters.loc[18,'Name'] = "Bizarro N.J."

# Also, there are two Goliath roller coasters, one in Six Flags over Georgia and one in
# La Ronde. Again, rather than having to make a bunch of special cases and other
# kludges, let's just rename the Canadian Goliath:

secondgoliath= steel_coasters[(steel_coasters.Name == 'Goliath') & \
                                                   (steel_coasters.Park == "La Ronde")]
#print(secondgoliath)

steel_coasters.loc[55,'Name'] = "Goliath Canadian"
steel_coasters.loc[57,'Name'] = "Goliath Canadian"
steel_coasters.loc[59,'Name'] = "Goliath Canadian"


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that will plot the ranking of a given roller coaster over time as a line.
Your function should take a roller coaster’s name and a ranking DataFrame as arguments.
Make sure to include informative labels that describe your visualization.
Call your function with "El Toro" as the roller coaster name and the wood ranking DataFrame.
What issue do you notice? Update your function with an additional argument to alleviate the problem,
and retest your function.'''

# write function to plot rankings over time for 1 roller coaster here:

def plot_rankings_of_a_coaster(name,park,frame):

    coaster_frame = frame[(frame.Name == name) & (frame.Park == park)]

    # Use the data for this specific roller coaster to set the horizontal axis limits:
    min_year=min(coaster_frame['Year of Rank'])
    max_year=max(coaster_frame['Year of Rank'])
    rangeofxs = list(range(min_year, max_year+1))
    
    # Use the data for this specific roller coaster to set the verticl axis limits:
    max_ranking=min(coaster_frame.Rank)
    min_ranking=max(coaster_frame.Rank)
    rangeofys = list(range(max_ranking,min_ranking+1))

    # Plot the plot:
    plt.figure(figsize=(6,6))
    ax1 = plt.subplot(1,1,1)
    lineplot = plt.plot(coaster_frame['Year of Rank'], coaster_frame['Rank'], marker = 'o', color = 'purple')
    ax1.set_xticks(rangeofxs)
    ax1.set_yticks(rangeofys)
    ax1.invert_yaxis()
    plt.title('Yearly Rankings of {}'.format(name))
    plt.ylabel('Ranking')
    plt.xlabel('Year of Ranking')
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that will plot the ranking of two given roller coasters over time as lines.
Your function should take both roller coasters’ names and a ranking DataFrame as arguments.
Make sure to include informative labels that describe your visualization.
Call your function with "El Toro" as one roller coaster name, “Boulder Dash“ as the other
roller coaster name, and the wood ranking DataFrame. What issue do you notice?
Update your function with two additional arguments to alleviate the problem, and retest your function.'''

# write function to plot rankings over time for 2 roller coasters here:

def plot_rankings_of_two_coasters(name1,park1,frame1,name2,park2,frame2):

   # Select rankings for the two roller coasters at the two selected parks.
    coaster_1_frame = frame1[(frame1.Name == name1) & (frame1.Park == park1)]
    coaster_2_frame = frame2[(frame2.Name == name2) & (frame2.Park == park2)]

   # Figure out which roller coaster had the earliest ranking. For setting axis limits.
    min_year1=min(coaster_1_frame['Year of Rank'])
    min_year2=max(coaster_2_frame['Year of Rank'])
    if min_year1 < min_year2:
        theminyear = min_year1
    else:
        theminyear = min_year2

    # Figure out which roller coaster had the most recent ranking. For setting axis limits.
    max_year1=min(coaster_1_frame['Year of Rank'])
    max_year2=max(coaster_2_frame['Year of Rank'])
    if max_year1 > max_year2:
        themaxyear = max_year1
    else:
        themaxyear = max_year2

    # Figure out which roller coaster had the highest rank. For setting axis limits.
    max_ranking1=min(coaster_1_frame.Rank)
    max_ranking2=min(coaster_1_frame.Rank)
    if max_ranking1 < max_ranking2:
        themaxrank = max_ranking1
    else:
        themaxrank = max_ranking2

    # Figure out which roller coaster had the lowest rank. For setting axis limits.
    min_ranking1=max(coaster_1_frame.Rank)
    min_ranking2=max(coaster_2_frame.Rank)
    if min_ranking1 > min_ranking2:
        theminrank = min_ranking1
    else:
        theminrank = min_ranking2

    # Set the axis limits:    
    rangeofxs = list(range(theminyear, themaxyear+1))
    rangeofys = list(range(themaxrank,theminrank+1))

    # Plot the figure:
    plt.figure(figsize=(6,6))
    ax2 = plt.subplot(1,1,1)
    lineplot1 = plt.plot(coaster_1_frame['Year of Rank'], coaster_1_frame['Rank'], marker='o', color = 'red')
    lineplot2 = plt.plot(coaster_2_frame['Year of Rank'], coaster_2_frame['Rank'], marker='o', color = 'blue')
    ax2.set_xticks(rangeofxs)
    ax2.set_yticks(rangeofys)
    ax2.invert_yaxis()
    plt.legend([name1,name2])
    plt.title('Yearly Rankings of {} and {}'.format(name1,name2))
    plt.ylabel('Ranking')
    plt.xlabel('Year of Ranking')
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that will plot the ranking of the top n ranked roller coasters over time as lines.
Your function should take a number n and a ranking DataFrame as arguments.
Make sure to include informative labels that describe your visualization.
For example, if n == 5, your function should plot a line for each roller coaster that has a
rank of 5 or lower.
Call your function with a value for n and either the wood ranking or steel ranking DataFrame.'''

# write function to plot top n rankings over time here:

# I admit, I had to look at the Codecademy hint to see precisely what the prompt was getting at,
# but after looking at the hint I see that the prompt was to do a line plot of each roller coaster
# that had a ranking in the top n at some point during the years 2013 to 2018, and plot only
# the top n rankings. (So, for example, only plot ranks 5 and up, but do that for every roller
# coaster that was at any point ranked in the top 5). The main problem with this is that roller
# coasters can and do drop out of the top n regularly, and sometimes might appear only once.
# This code does what the prompt "wanted" done, with the added bonus of plotting "one and
# dones" as single data points so that they appear on the plot.

def plot_only_top_n_coasters(n,frame1):
    top_n_rankings = frame1[frame1.Rank <= n]

    max_rank = 1
    min_rank = 1
    namesofcoasters=[]

    plt.figure(figsize=(6,6))
    ax3 = plt.subplot(1,1,1)
    for i in set(top_n_rankings['Name']):
        this_frame = top_n_rankings[top_n_rankings['Name'] == i]
        if len(this_frame) > 1:
            plt.plot(this_frame['Year of Rank'], this_frame['Rank'], marker = 'o')
        else:
            plt.scatter(this_frame['Year of Rank'], this_frame['Rank'])
        namesofcoasters.append(i)
        this_min_rank = max(this_frame.Rank)
        if this_min_rank > min_rank:
            min_rank = this_min_rank
    rangeofys=list(range(max_rank,min_rank+1))
    ax3.set_xticks([2013,2014,2015,2016,2017,2018])
    ax3.set_yticks(rangeofys)
    ax3.invert_yaxis()
    plt.title('Top {} Roller Coasters per Year'.format(n))
    plt.ylabel('Ranking')
    plt.xlabel('Year of Ranking')
    plt.legend(namesofcoasters)
    plt.show()

# Now when I first read the prompt, I thought it wanted one to find every roller coaster which
# had ever been ranked in the top n (from 2013 to 2018 at least), and plot its yearly ranking
# regardless of whether it was a top n ranking or not. I personally feel that this is more informative,
# so I wrote a separate function to do that. If a roller coaster only had one ranking (because it was new,
# or it was closed after it was initially ranked), I again plot its rank as a single data point rather than
# a line.

def plot_n_rankings_of_coasters(n,frame1):
    top_n_rankings = frame1[frame1.Rank <= n]

    max_rank = 1
    min_rank = 1
    namesofcoasters=[]

    plt.figure(figsize=(6,6))
    ax3 = plt.subplot(1,1,1)
    for i in set(top_n_rankings['Name']):
        this_frame = frame1[frame1['Name'] == i]
        if len(this_frame) > 1:
            plt.plot(this_frame['Year of Rank'], this_frame['Rank'], marker='o')
        else:
            plt.scatter(this_frame['Year of Rank'], this_frame['Rank'])
        namesofcoasters.append(i)
        this_min_rank = max(this_frame.Rank)
        if this_min_rank > min_rank:
            min_rank = this_min_rank
    rangeofys=list(range(max_rank,min_rank+1))
    ax3.set_xticks([2013,2014,2015,2016,2017,2018])
    ax3.set_yticks(rangeofys)
    ax3.invert_yaxis()
    plt.title('Yearly Rankings of Top {} Roller Coasters'.format(n))
    plt.ylabel('Ranking')
    plt.xlabel('Year of Ranking')
    plt.legend(namesofcoasters)
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Now that you’ve visualized rankings over time, let’s dive into the actual statistics of roller coasters
themselves. Captain Coaster is a popular site for recording roller coaster information. Data on all
roller coasters documented on Captain Coaster has been accessed through its API and stored in
roller_coasters.csv. Load the data from the csv into a DataFrame and inspect it to gain familiarity
with the data.'''

# load roller coaster data here:

roller_coasters = pd.read_csv('roller_coasters.csv')

print(roller_coasters.info())


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that plots a histogram of any numeric column of the roller coaster DataFrame.
Your function should take a DataFrame and a column name for which a histogram should be
constructed as arguments. Make sure to include informative labels that describe your visualization.
Call your function with the roller coaster DataFrame and one of the column names.'''

# write function to plot histogram of column values here:

def plot_a_coaster_histogram(frame,columnname,numofbins):
    
    # Useful hint from Codecademy: Drop all blank values from the desired column:
    frame.dropna(subset=[columnname], inplace = True)

    # Plot the desired histogram.
    plt.figure(figsize=(6,6))
    # The height column has two roller coasters with heights of 920 feet which
    # makes plotting a histogram for the full range of values difficult. So,
    # I am hard-coding this function to only plot heights out to 140 feet.
    # If I can figure out how to pass that in as a kewyord argument, I will.
    if columnname != "height":
        plt.hist(frame[columnname], bins = numofbins)
    else:
        plt.hist(frame[columnname], bins = numofbins, range = (0,140))
    plt.title('Distribution of Roller Coaster {} Values'.format(columnname))
    plt.xlabel(columnname)
    plt.ylabel('Num. of Roller Coasters') 
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that creates a bar chart showing the number of inversions for each roller coaster at
an amusement park. Your function should take the roller coaster DataFrame and an amusement park
name as arguments. Make sure to include informative labels that describe your visualization.
Call your function with the roller coaster DataFrame and an amusement park name.'''

# write function to plot inversions by coaster at a park here:

def inversions_at_park(frame,park_name):

    # First, get all roller coasters in the selected amusement park:
    park_coasters = frame[frame.park == park_name]

    # Now plot the number of inversion bar chart:
    plt.figure(figsize=(6,8))
    ax5 = plt.subplot()
    plt.bar(range(len(park_coasters.name)), park_coasters.num_inversions)
    plt.title('Num. of Inversions per Roller Coaster at  {} '.format(park_name))
    plt.ylabel('Number of Inversions')
    ax5.set_xticks(range(len(park_coasters.name)))
    ax5.set_xticklabels(park_coasters.name)               
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that creates a pie chart that compares the number of operating roller coasters
('status.operating') to the number of closed roller coasters ('status.closed.definitely').
Your function should take the roller coaster DataFrame as an argument. Make sure to include
informative labels that describe your visualization.'''

# write function to plot pie chart of operating status here:

# I actually coded this function to take in two arguments: the DataFrame and a chart choice.
# The choice "prompt" will give you a pie chart containing precisely what the prompt wants,
# namely a pie chart just for roller coasters whose statuses are operating or closed definitely.
# However, not all rollrer coasters have one of those two statuses, so what we're really doing
# is comparing the percentage of operational to definitely closed roller coasters for just those
# two groups. It's a lot more interesting, in my opinion, to see the relative percentages of ALL
# recorded statuses, so if you choose "all" as the chartchoice argument you'll get a pie chart
# showing ALL statuses, not just operational or definitley closed.

def operational_status(frame,chartchoice):

    # Get the number of roller coasters in every reported operational status:
    status_counts=frame.groupby('status').name.count()
    
    # The prompt was to consider only two of the reported operational statuses.
    # So, isolate those two operational statuses, and count the number in each:
    operational_coasters=frame[frame.status == 'status.operating']
    closed_coasters=frame[frame.status == 'status.closed.definitely']
    
    operational_counts=operational_coasters.park.count()
    closed_counts=closed_coasters.park.count()
 
    limited_counts=[operational_counts,closed_counts]

    # Plot a pie chart. If "all" was chosen, a pie chart with all reported operational statuses
    # will be plotted. If "prompted" was chosen, a pie chart showing only the two prompted
    # operational statuses will be shown.
    plt.figure(figsize=(6,6))
    if chartchoice == 'all':
        plt.pie(status_counts)
        plt.legend(['Announced','Closed definitely','Closed Temporarily',\
                    'Under Construction','Operating','Relocated','Retracked','Rumored','Unknown'], loc = 3)
    elif chartchoice == 'prompted':
        plt.pie(limited_counts, colors = ['red','blue'])
        plt.legend(['Operating','Closed Definitely'], loc = 4)
    plt.axis('equal')
    plt.title('Operational Status of Indexed Roller Coasters')
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Write a function that creates a scatter plot of two numeric columns of the roller coaster DataFrame.
Your function should take the roller coaster DataFrame and two-column names as arguments.
Make sure to include informative labels that describe your visualization.
Call your function with the roller coaster DataFrame and two-column names.'''

# write function to create scatter plot of any two numeric columns here:

def plot_a_scatterplot(frame,column1,column2):

    # Since numerous roller coasters have unreported speeds, heights, etc., eliminate all
    # rows without values in either of the desired columns:
    frame.dropna(subset=[column1,column2], inplace = True)
    
    # As noted in the code for "plot_a_coaster_histogram", the height column has two roller coasters
    # with heights of 920 feet which when included on plots tends to wash out features in the scatter
    # plots for roller coasters of more modest heights. So, I am hard-coding this function to only plot
    # heights out to 140 feet. 
    if (column1 == "height") or (column2 == 'height'):
        frame = frame[frame.height <= 150]
    else:
        frame = frame

    # Now plot:
    plt.figure(figsize=(6,6))
    plt.scatter(frame[column1],frame[column2], color = 'green', marker = '*', linewidths = 0.5)
    plt.title('{} vs. {} for Indexed Roller Coasters'.format(column1,column2))
    plt.xlabel(column1)
    plt.ylabel(column2) 
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Part of the fun of data analysis and visualization is digging into the data you have and answering
questions that come to your mind.'''

# I'll tackle one of the prompted questions and a couple of my own.

'''Prompted question: Do roller coaster manufacturers have any specialties (do they focus on
speed, height, seating type, or inversions)?'''
# I chose this prompted question because it is the most interesting to me. First let's write a function
# that allows you to investigate the speed, height, etc. of all roller coasters made by a manufacturer:

def plot_manufacturer_specialties(frame,maker,columnname):
    # If the column is one that has numerical entries, drop the NaN values. Don't
    # do it for seating_type, as that kinda does encode some information.
    if columnname in ['speed','height','length','num_inversions']:
        frame.dropna(subset=[columnname], inplace = True)
    this_here_frame = frame[frame.manufacturer == maker]
      
    plt.figure(figsize=(6,6))
    ax6= plt.subplot()

    # if seating type or number of inversions is chosen, count the number of each seating type / inversion
    # the manufacturer made and make a bar chart:
    seating_counts = this_here_frame.groupby(['seating_type']).material_type.count().reset_index()
    inversion_counts = this_here_frame.groupby(['num_inversions']).material_type.count().reset_index()
  
    if columnname == 'seating_type':
        plt.bar(range(len(seating_counts)), seating_counts.material_type)
        ax6.set_xticks(range(len(seating_counts)))
        ax6.set_xticklabels(seating_counts.seating_type)
        plt.xticks(rotation=90)
        plt.title('Roller Coaster Seating Types made by {}'.format(maker))
        plt.ylabel('Number of Roller Coasters')
        plt.subplots_adjust(bottom=0.25)
    elif columnname == 'num_inversions':
        plt.bar(range(len(inversion_counts)), inversion_counts.material_type)
        ax6.set_xticks(range(len(inversion_counts)))
        ax6.set_xticklabels(inversion_counts.num_inversions)
        plt.xticks(rotation=90)
        plt.title('Num. of Inversions of Roller Coasters made by {}'.format(maker))
        plt.xlabel('Number of Inversions')
        plt.ylabel('Number of Roller Coasters')
        plt.subplots_adjust(bottom=0.25)        

    # if speed, height, or length were chosen, make a histogram:

    else:
        plt.hist(this_here_frame[columnname]) 
        plt.title('Distribution of {} Values for Roller Coasters made by {}'.format(columnname, maker))
        plt.xlabel(columnname)
        plt.ylabel('Num. of Roller Coasters') 

    plt.show()

# Now what if you wanted to look at aggregate statistics for all the roller coasters made by each of
# the manufacturers? We'll limit this one to speed, height, and length.

def aggregate_manufacturer_specialties(frame,columnname):

    # First of all, drop the NaN entries for that particular column:
    frame.dropna(subset=[columnname], inplace = True)

    # Now drop any rows where the manufacturer's name isn't known:
    frame = frame[frame.manufacturer != 'na']

    frame.sort_values(by=columnname, inplace = True, ascending = False)

    plt.figure(figsize=(10,10))
    ax7 = plt.subplot()
    sns.barplot(data = frame, x = 'manufacturer', y = columnname, ci = None)
    plt.xticks(rotation=90, fontsize = 6)
    plt.subplots_adjust(bottom=0.35)
    plt.title('Average {} for all Recorded Roller Coaster Manufacturers'.format(columnname))
    plt.ylabel('Average {}'.format(columnname))
    plt.xlabel('Manufacturer')
    plt.show()  
    
# And now for a couple of questions that I have.
# How many roller coasters made by each manufacturer are still operational?

def whats_operational_by_manufacturer(frame):
    # First of all, drop any rows where the manufacturer's name isn't known:
    frame = frame[frame.manufacturer != 'na']

    # Now select only the ones which are operational:
    frame =frame[frame.status == 'status.operating']

    # Count them up by manufacturer:
    operational_counts = frame.groupby(['manufacturer']).status.count().reset_index()
    operational_counts.sort_values(by='status', inplace = True, ascending = False)

    # Finally, plot a bar chart:

    plt.figure(figsize=(10,10))
    ax7 = plt.subplot()
    plt.bar(operational_counts.manufacturer, operational_counts.status)
    plt.xticks(rotation=90, fontsize = 6)
    plt.subplots_adjust(bottom=0.35)
    plt.title('Number of Operational Roller Coasters for all Recorded Roller Coaster Manufacturers')
    plt.ylabel('Number of Operational Roller Coasters')
    plt.xlabel('Manufacturer')
    plt.show()  

# Is there any correlation between the speed of a roller coaster and its ranking? How about height?
# Or even length?
# Naturally, this investigation will be limited to those roller coasters that have
# rankings as in the wood_coasters and steel_coasters tables. It will also be limited to the columns
# speed, height, and length in the roller_coasters table.

def rank_and_property(frame1,frame2,columnname):
   # First we need to select only those roller coasters which have rankings:
    frame = pd.merge(wood_coasters, roller_coasters, \
                                   left_on = 'Name', right_on = 'name', suffixes = ['_f1', '_f2'])

    # Remove rows with null values in the column name;
    frame.dropna(subset=[columnname], inplace = True)

    # Let's sort by ranking before dropping duplicates. This will keep a roller coaster's highest ranking:
    frame.sort_values(by='Rank', inplace = True, ascending = False)

    # In the rankings data frame, some coasters appear more than once. So drop the duplicates
    # according to the roller coaster's name (which I take from the ranking DataFrame):
    goodframe = frame.drop_duplicates(subset=['Name']) 

    print(goodframe.info())

    # Now plot:
    plt.figure(figsize=(6,6))
    ax8 = plt.subplot()
    plt.scatter(goodframe[columnname],goodframe.Rank, color = 'purple', \
                      marker = '*', linewidths = 0.5)
    plt.title('{} vs. Ranking for Indexed Roller Coasters'.format(columnname))
    plt.xlabel(columnname)
    plt.ylabel('Ranking of Roller Coaster')
    ax8.invert_yaxis()
    plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Now to actually call some functions and make some plots.

# First, "plot_rankings_of_a_coaster." The prompted function call is first; the second investigates the
# rankings of a particular Kennywood roller coaster, chosen because Kennywood is my hometown
# amusement park:
#plot_rankings_of_a_coaster('El Toro', 'Six Flags Great Adventure', wood_coasters)
#plot_rankings_of_a_coaster('Thunderbolt', 'Kennywood', wood_coasters)

# Next, "plot_rankings_of_two_coasters. Again, the first call is the prompted call to the function;
# the second is for two Kennywood roller coasters. I am calling the same DataFrame each time,
# but I coded it to take in two different DataFrames if you'd like.
#plot_rankings_of_two_coasters('El Toro', 'Six Flags Great Adventure',wood_coasters,\
#                                                   'Boulder Dash','Lake Compounce',wood_coasters)
#plot_rankings_of_two_coasters('Jack Rabbit', 'Kennywood',wood_coasters,\
#                                                   'Thunderbolt','Kennywood',wood_coasters)

 # Now for the top "n" yearly rankings of roller coasters. plot_only_top_n limits the plot to just top n
 # rankings for every roller coaster ever ranked in the top n. plot_n_rankings_of_coasters plots all
 # yearly rankings for every roller coaster ever ranked in the top n, whether a particular yearly ranking
 # was in the top n or not.
#plot_only_top_n_coasters(5,wood_coasters)
#plot_n_rankings_of_coasters(5,steel_coasters)

# Next up: plot_a_coaster_histogram. The last parameter is for the bin size, so you can adjust the bin
# size for your chosen histogram as you like it.
#plot_a_coaster_histogram(roller_coasters,'speed',20)

# Now for inversions_at_a_part, which is a specific bar chart to show the number of inversions along
# the track for every roller coaster at a particular park. Since Kennywood is my hometown
# amusement park, I am naturally choosing it for my function call.
#inversions_at_park(roller_coasters,'Kennywood')

# Next up: operational_status. Choose "all" to make a pie plot for all recorded statuses; choose
# "prompted" to make a pie chart just for the two statuses the prompt "wanted."
#operational_status(roller_coasters,'prompted')

# Now for plot_a_scatterplot, which will plot a scatter plot for any two numerical columns in the
# DataFrame "roller_coasters" that you'd like.
#plot_a_scatterplot(roller_coasters,'speed','height')

# Let's now move on to function calls for manufacturer information. First we'll call
# plot_manufacturer_specialties, which allows you to plot information about
# seating_type, num_inversions, speed,  height, or length for a particular manufacturer:
# plot_manufacturer_specialties(roller_coasters,'Vekoma','speed')

# If you wanted to look at average speed, height, or length for all manufacturers in the
# DataFrame, call aggregate_manufacturer_specialties:
#aggregate_manufacturer_specialties(roller_coasters,'length')

# Who's built the most stuff that's still operational? Call whats_operational_by_manufacturer to
# find out.
#whats_operational_by_manufacturer(roller_coasters)

# And lastly, let's say you want to see if there is any correlation between the speed of a roller coaster
# and its ranking. Or how about height and ranking? or even length and ranking?
# rank_and_property will let you do that.
# Caveat: The highest ranking of a roller coaster is kept for this plot, so there can be multiple 1s,
# 2s, etc. 
rank_and_property(steel_coasters,roller_coasters,'speed')
# Spoiler alert: No, there doesn't seem to be a strong correlation.

# The above calculation has flaws (it might be better to do average rank, for example), but it also leads
# to more interesting questions: Which manufacturers made the highest ranked roller coasters? Which
# roller coasters built before, say, 1970 are still operational? Do newer roller coasters have more
# inversions than older ones? Are they faster?

# Other potentially interesting questions which I might code in later:
# Do newer roller coasters tend to be more highly ranked than older ones?
# Of parks with more than one roller coaster, which one is the most highly ranked?
# Which parks have the most highly ranked roller coasters?
