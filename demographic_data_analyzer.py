import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    age_men = df.loc[df['sex'] == 'Male']['age'].mean()
    average_age_men = round(age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df.loc[df['education'] == 'Bachelors'].count()[0]
    total_count = df.count()[0]
    percentage_bachelors = round(bachelors_count/total_count * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
  
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].count()[0]
  
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')].count()[0]

    # percentage with salary >50K
    adv_edu_rich = df.loc[(df['salary']=='>50K') & ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))].count()[0]
  
    low_edu_rich = df.loc[(df['salary']=='>50K') & ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))].count()[0]
  
    higher_education_rich = round(adv_edu_rich/higher_education * 100, 1)  #(46.5)
    lower_education_rich = round(low_edu_rich/lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours] #will make a df with min work hours = 1
  
    num_min_workers_rich = num_min_workers[num_min_workers['salary'] == '>50K'].count()[0]
  
    rich_percentage = round(num_min_workers_rich/len(num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?

    #1. Find number of people in every country
    no_of_people_in_countries = df['native-country'].value_counts()
  
    #2. Find number of people with salary > 50K in every country
    people_with_high_sal_in_countries = df[df['salary'] == '>50K']['native-country'].value_counts()
  
    #3. Find % of people with salary > 50K in every country
    countries_rich_people_percent = round(people_with_high_sal_in_countries/no_of_people_in_countries*100,1)

    #4. Find the highest earning country  ('Iran')
    highest_earning_country = countries_rich_people_percent.idxmax()
  
    #5. Highest percentage of people that earn >50K  (41.86)
    highest_earning_country_percentage = round(countries_rich_people_percent.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
  
    #1. Find number of people in India & of people with salary > 50K in India
    rich_people_india = df[(df['native-country']=='India') & (df['salary'] == '>50K')]
  
    #2. Find the most popular occupation for these people
    occupations_of_rich_people_india = rich_people_india['occupation'].value_counts()
  
    top_IN_occupation = occupations_of_rich_people_india.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
