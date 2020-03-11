#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:43:24 2019

@author: danielqiao
"""

import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)

test = [True for i in range(100)]
for j in range(400):
    test.append(False)
len(test)

def date_sorter():
    
    # Your code here
    '''
    04/20/2009; 04/20/09; 4/20/09; 4/3/09
    Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
    (?P<month>\d?\d)[/|-](?P<day>([0-2]?[0-9])|([3][01]))[/|-](?P<year>[\d{4}|\d{2}])

    Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    (?P<month>[a-zA-Z]{3,})\.?-? ?(?P<day>\d\d?)(th|nd|st)?,?-? ?(?P<year>\d{4})
    
    20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    (?P<day>\d?\d) ?(?P<month>[a-zA-Z]{3,})\.?,? (?P<year>\d{4})
    
    Feb 2009; Sep 2009; Oct 2010
    (?P<month>[A-Z][a-z]{3,}),?\.? (?P<year>\d{4})
    
    6/2008; 12/2009
    (?P<month>\d\d?)/(?P<year>\d{4})

    2009; 2010
    (?P<year>\d{4})
    '''
    
    df_ans = df.str.extractall(r'(?P<month>\d?\d)[/|-](?P<day>\d?\d)[/|-](?P<year>\d{4})')
    not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    df_ans = df_ans.append(df[not_duplicated].str.extractall(r'(?P<month>\d?\d)[/|-](?P<day>([0-2]?[0-9])|([3][01]))[/|-](?P<year>\d{2})'))
    not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    df_ans = df_ans.append(df[not_duplicated].str.extractall(r'(?P<day>\d?\d) ?(?P<month>[a-zA-Z]{3,})\.?,? (?P<year>\d{4})'))
    not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    df_ans = df_ans.append(df[not_duplicated].str.extractall(r'(?P<month>[a-zA-Z]{3,})\.?-? ?(?P<day>\d\d?)(th|nd|st)?,?-? ?(?P<year>\d{4})'))
    not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])

    without_day = df[not_duplicated].str.extractall('(?P<month>[A-Z][a-z]{2,}),?\.? (?P<year>\d{4})')
    without_day = without_day.append(df[not_duplicated].str.extractall(r'(?P<month>\d\d?)/(?P<year>\d{4})'))
    without_day['day'] = 1
    df_ans = df_ans.append(without_day)
    not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])

    without_month = df[not_duplicated].str.extractall(r'(?P<year>\d{4})')
    without_month['day'] = 1
    without_month['month'] = 1
    df_ans = df_ans.append(without_month)
    not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])

    # Year
    df_ans['year'] = df_ans['year'].apply(lambda x: '19' + x if len(x) == 2 else x)
    df_ans['year'] = df_ans['year'].apply(lambda x: str(x))

    # Month
    df_ans['month'] = df_ans['month'].apply(lambda x: x[1:] if type(x) is str and x.startswith('0') else x)
    month_dict = {'February': 2, 'Dec': 12, 'Apr': 4, 'Jan': 1, 'Janaury': 1,'August': 8, 'October': 10,'September': 9, 'Mar': 3, 'November': 11, 'Jul': 7, 'January': 1,'Feb': 2, 'May': 5, 'Aug': 8, 'Jun': 6, 'Sep': 9, 'Oct': 10, 'June': 6, 'March': 3, 'July': 7, 'Since': 1, 'Nov': 11, 'April': 4, 'Decemeber': 12, 'Age': 8}
    
    df_ans = df_ans.replace(month_dict)
    df_ans['month'] = df_ans['month'].apply(lambda x: str(x))
    df_ans['day'] = df_ans['day'].apply(lambda x: str(x))

    df_ans['date'] = df_ans['month'] + '/' + df_ans['day'] + '/' + df_ans['year']
    df_ans['date'] = pd.to_datetime(df_ans['date'])

    df_ans = df_ans.sort_values(by='date')
    return_rank = pd.Series(list(df_ans.index.labels[0]))
    
    return return_rank # Your answer here

date_sorter()