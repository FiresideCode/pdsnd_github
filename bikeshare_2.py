import time as t
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to explore data for Chicago, New York City, or Washington? \n")
        city = city.strip().lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Invalid city choosen")
        else:
            break
            

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nSecondly, would you like to view data for January, February, March, April, May, June, or All? \n")
        if month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("Invalid month choosen")
        else:
            break
            
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nFinally, what day of the week are interested in: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All? \n")
        if day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("Invalid day choosen")
        else:
            break
            
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # Converting Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extracting  month and day from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day

    # Month filter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    # Day filter
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = t.time()

    # display the most common month
    print("The most common month is: ", df['month'].mode()[0], "\n")

    # display the most common day of week
    print("The most common day of week is: ", df['day'].mode()[0], "\n")


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = t.time()

    # display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0], "\n")

    # display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0], "\n")


    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "-->" + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0], "\n")


    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = t.time()

    # display total travel time
    print("The total travel time is: ", df['Trip Duration'].sum(), "\n")


    # display mean travel time
    print("The total mean time is: ", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = t.time()

    # Display counts of user types
    user_types = df['User Type'].count()
    print('Number of user types: ', user_types, "\n")
    

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].count()
        print('Gender count: ', gender, "\n")
    else:
        print("Gender not available for this city!", "\n")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('\nThe earliest birth year is: ', earliest_birth_year)

        most_recent_birth_year = df['Birth Year'].max()
        print('\nThe most recent birth year is: ', most_recent_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common birth year is: ', common_birth_year)
    else:
        print("Birth year not available for this city!", "\n")
    
                         

    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)

         
def more_data(df):
    """ Displays 5 more rows of data per time"""

    # Display more row of data
    row = 0
    while True:
        raw_data = input("\nWould you like to view the raw data - 5 rows at a time? 'Yes' or 'No'? \n")
        if raw_data.lower() not in ['yes', 'no']:
            print('Your choice is invalid!')     
        else:
            break
    
    if raw_data == 'yes':
        while True:
            row += 5
            print(df.iloc[row : row + 5])
            more = input("\nWould you like to view more data? 'Yes' or 'No' \n")
            if more == 'no':
                break
    elif raw_data == 'no':
        return

          


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
