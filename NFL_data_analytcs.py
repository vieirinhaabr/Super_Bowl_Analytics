import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

if __name__ == "__main__":
    # initialize

# Inspect CSV files
def inspect_csv():
    tv.info()
    print('\n')
    halftime_musicians.info()

# Prepare seaborn graph (without seaborn lib)
def pg():
    #get_ipython().run_line_magic('matplotlib', 'inline')
    plt.style.use('seaborn')
    plt.xlabel('Combined Points')
    plt.ylabel('Number of Super Bowls')
    plt.show()

def shls():
    display(super_bowls[super_bowls['combined_pts'] > 70])
    display(super_bowls[super_bowls['combined_pts'] < 70])

# Difference points on super bowl's
def pd():
    plt.hist(super_bowls.difference_pts)
    plt.xlabel('Point Difference')
    plt.ylabel('Number of Super Bowls')
    plt.show()

# Closest and biggest difference between team's
def cb():
    display(super_bowls[super_bowls['difference_pts'] == 1])
    display(super_bowls[super_bowls['difference_pts'] >= 35])

# When difference on score is minor, is the audience biggest (seaborn graph)
def adp():
    games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

    sns.regplot(x='difference_pts', y='share_household', data=games_tv)

# Ad cost graph's about super bowl
def adcost():
    plt.subplot(3, 1, 1)
    plt.plot(tv['super_bowl'], tv['avg_us_viewers'], color='#648FFF')
    plt.title('Average Number of US Viewers')

    plt.subplot(3, 1, 2)
    plt.plot(tv['super_bowl'], tv['rating_household'], color='#DC267F')
    plt.title('Household Rating')

    plt.subplot(3, 1, 3)
    plt.plot(tv['super_bowl'], tv['ad_cost'], color='#FFB000')
    plt.title('Ad Cost')
    plt.xlabel('SUPER BOWL')

    plt.tight_layout()

# Musicians up to and including Super Bowl XXVII
def msb():
    halftime_musicians[halftime_musicians['super_bowl'] <= 27]


# Count appearances for each musician and sort them from most to least
def coma():
    halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
    halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Who performer more than one appearances
def wpmto():
    halftime_appearances[halftime_appearances['super_bowl'] > 1]

# Remove most marching bands and count songs played
def rmb():
    no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
    no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]
    cns(no_bands)

def cns(dataframe):
    most_songs = int(max(dataframe['num_songs'].values))
    plt.hist(dataframe.num_songs.dropna())
    plt.xlabel('Number of Songs Per Halftime Show Performance')
    plt.ylabel('Number of Musicians')
    plt.show()

    dataframe = dataframe.sort_values('num_songs', ascending=False)