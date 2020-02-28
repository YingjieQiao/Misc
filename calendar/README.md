### Calendar year: 

The goal of top-down design is for each module to provide clearly defined functionality, which collectively provides all of the required functionality of the program.

The three overall steps of the calendar year program are getting the requested year from the user, creating the calendar year structure, and displaying the year. The functionality of displaying the calendar year is not too complex and can be contained in a single function. However, constructing the calendar year takes significantly more steps. Part of a well- designed program is to break those steps up, along their logical boundaries into their own functions. Implement the following functions to produce a program that can construct and display a calendar year:

#### (a) 
def leap_year(year): Returns True if the input argument year is a leap year. Oth- erwise, returns False. Check http://en.wikipedia.org/wiki/Leap_year#Algorithm for how to do this.

#### (b)
def day_of_week_jan1(year): Returns the day of the week for January 1 of the in- put argument year. year must be between 1800 and 2099. The returned value must be in the range 0-6 (where 0-Sun, 1-Mon, . . ., 6-Sat). Check http://en.wikipedia. org/wiki/Determination_of_the_day_of_the_week#Gauss.27_algorithm for how to do this. The weekday of the first of January in year A is given by:
d = R(1 + 5R(A − 1, 4) + 4R(A − 1, 100) + 6R(A − 1, 400), 7)
where R(y,x) is a function that returns the remainder when y is divided by x. In
Python, it is similar to executing y % x.

#### (c)
def num_days_in_month(month_num, leap_year): Returns the number of days in a given month. month_num must be in the range 1-12, inclusive. leap_year must be True if the month occurs in a leap year. Otherwise, it should be False.

#### (d)
def construct_cal_month(month_num, first_day_of_month, num_days_in_month): Returns a formatted calendar month for display on the screen. month_num must be
in the range 1-12, inclusive. first_day_of_month must be in the range 0-6 (where 0-Sun, 1-Mon, . . ., 6-Sat). Return a list of strings of the form,
[month_name, week1, week2, ...,]
For example, the first two weeks of January 2015 will be
[’January’,’ 1 2 3’,’ 4 5 6 7 8 910’]
as the first two weeks for January 2015 will be displayed as
123 4 5 6 7 8 9 10
If the number of days of the last week is less than seven, no spaces are added after the last date. For example, the last week of December 2015 will be

’ 27 28 29 30 31’

Notice that the number of days is five days, and that there are no spaces added after the characters 31. Note also that there are three spaces reserved for each day. In this way, there are two spaces before 4 and two spaces between 4 and 5, but only one space before 27 and between 27 and 28. To test, define the following function:

```
def print_cal_month(list_of_str): ret_val=’’
    for l in list_of_str:
    ret_val+= l.replace(’ ’,’*’) ret_val+=’\n’
    return ret_val
  ```
  
The above function replaces the spaces with * and display each item in the list in a
new line. If you run the following code:
`ans=construct_cal_month(1,5,31) print(print_cal_month(ans))`
it should output:

```
January 
*****************1**2 
**3**4**5**6**7**8**9 
*10*11*12*13*14*15*16 
*17*18*19*20*21*22*23 
*24*25*26*27*28*29*30 
*31
```

Note that the `*` marks here should be replaced by whitespaces.

#### (e)
def construct_cal_year(year): Return a formatted calendar year for display on the screen. year must be in the range 1800-2099, inclusive. Return a list of the form,
[year, month1, month2, month3, ..., month12]
in which year is an int and each month is a sublist (i.e. month1, month2, . . .) is of the form
[month_name, week_1_dates, week_2_dates, ...,]
The main function is:
(f) def display_calendar(calendar_year): Returns a formatted calendar display as
a string, based on the provided calendar_year.


Sample run:
```
January
  S  M  T  W  T  F  S
           1  2  3  4
  5  6  7  8  9 10 11
 12 13 14 15 16 17 18
 19 20 21 22 23 24 25
 26 27 28 29 30 31

February
  S  M  T  W  T  F  S
                    1
  2  3  4  5  6  7  8
  9 10 11 12 13 14 15
 16 17 18 19 20 21 22
 23 24 25 26 27 28 29

March
  S  M  T  W  T  F  S
  1  2  3  4  5  6  7
  8  9 10 11 12 13 14
 15 16 17 18 19 20 21
 22 23 24 25 26 27 28
 29 30 31

April
  S  M  T  W  T  F  S
           1  2  3  4
  5  6  7  8  9 10 11
 12 13 14 15 16 17 18
 19 20 21 22 23 24 25
 26 27 28 29 30

May
  S  M  T  W  T  F  S
                 1  2
  3  4  5  6  7  8  9
 10 11 12 13 14 15 16
 17 18 19 20 21 22 23
 24 25 26 27 28 29 30
 31

June
  S  M  T  W  T  F  S
     1  2  3  4  5  6
  7  8  9 10 11 12 13
 14 15 16 17 18 19 20
 21 22 23 24 25 26 27
 28 29 30

July
  S  M  T  W  T  F  S
           1  2  3  4
  5  6  7  8  9 10 11
 12 13 14 15 16 17 18
 19 20 21 22 23 24 25
 26 27 28 29 30 31

August
  S  M  T  W  T  F  S
                    1
  2  3  4  5  6  7  8
  9 10 11 12 13 14 15
 16 17 18 19 20 21 22
 23 24 25 26 27 28 29
 30 31

September
  S  M  T  W  T  F  S
        1  2  3  4  5
  6  7  8  9 10 11 12
 13 14 15 16 17 18 19
 20 21 22 23 24 25 26
 27 28 29 30

October
  S  M  T  W  T  F  S
              1  2  3
  4  5  6  7  8  9 10
 11 12 13 14 15 16 17
 18 19 20 21 22 23 24
 25 26 27 28 29 30 31

November
  S  M  T  W  T  F  S
  1  2  3  4  5  6  7
  8  9 10 11 12 13 14
 15 16 17 18 19 20 21
 22 23 24 25 26 27 28
 29 30

December
  S  M  T  W  T  F  S
        1  2  3  4  5
  6  7  8  9 10 11 12
 13 14 15 16 17 18 19
 20 21 22 23 24 25 26
 27 28 29 30 31
```
