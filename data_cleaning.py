# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:25:20 2021

@author: Laptop Zone
"""

import pandas as pd
df=pd.read_csv('C:/Users/Laptop Zone/jupyterNoteBook/salary_predic_ds/glsDr_jobs.csv')
#salary parsing
#remove -1 from salary coloum.
df['hourly']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer provided']=df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df= df[df['Salary Estimate']!='-1']
#remove unwanted text from salary
salary=df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd=salary.apply(lambda x: x.replace('K','').replace('$',''))
df['min_salary']= minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary']=minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary']= (df.min_salary+df.max_salary)/2

#company name text only
#already cleaned

#job location

df['job_state']= df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()
#df['same_state']=df.apply(lambda x: 1 if x.Location==x. )
df.columns
df['age']= df.Founded.apply(lambda x: x if x<1 else 2021-x )

#job description
#python
df['python_yn']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index=False)



