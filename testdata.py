import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    inp=input("enter a city (chicago, new york city, washington): ")
    while inp !='chicago' and inp !='new york city'and inp !='washington':
            inp=input("please enter a valid  city (chicago, new york city, washington)")
    city=inp        

    # TO DO: get user input for month (all, january, february, ... , june)
    inp=input("enter a month(all,january,february,....): ")
    while inp not in months:
            inp=input("please enter a valid  month: ")
    month=inp        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    inp=input("enter a day(saturday,sunday,.....): ")
    while inp not in days:
            inp=input("please enter a valid  day: ")
    day=inp
    print('-'*40)
    return city, month, day


#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df["End Time"]= pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df["hour"]= pd.to_datetime(df['Start Time']).dt.hour
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week']==day.title()]
    
    return df
    




#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print("common month",df['month'].mode()[0])

    # TO DO: display the most common day of week

    print("common day",df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour

    print("common hour",df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("common start station: ",df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print("common end station: ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    print("common combinayion of start station and end station: ",df.groupby(['Start Station','End Station']).size().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Delta Time']=df['End Time']-df['Start Time']
    # TO DO: display total travel time
    print("total time travel:  ",df["Delta Time"].sum())

    # TO DO: display mean travel time
    print("total time travel mean:  ",df["Delta Time"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print("user types count:  ",df["User Type"].value_counts()[0])
    # TO DO: Display counts of gender
    print("Gender count:  ",df["Gender"].value_counts()[0])

    # TO DO: Display earliest, most recent, and most common year of birth
    print("earliest:  ",df["Birth Year"].min()," Recent year : ",df["Birth Year"].max(),"  most common year of birth",df["Birth Year"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
