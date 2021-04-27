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
minus_kd=salary.apply(lambda x: x.replace('K','')).replace('$','')



