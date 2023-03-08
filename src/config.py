import os
import pandas as pd

# Only update this variable; Month should be written in shortcut
MONTH_YEAR = 'May_2022'

MONTH_INDEX = {'Jan':0,'Feb':1,'Mar':2,'Apr':3,'May':4,'Jun':5,'Jul':6,'Aug':7,'Sep':8,'Oct':9,'Nov':10,'Dec':11}
MONTH = MONTH_YEAR.split('_')[0]
YEAR = MONTH_YEAR.split('_')[1]
MONTH_START = pd.date_range(YEAR, periods=12, freq='MS').strftime("%d-%b-%Y")[MONTH_INDEX[MONTH]]
MONTH_END = pd.date_range(YEAR, periods=12, freq='M').strftime("%d-%b-%Y")[MONTH_INDEX[MONTH]]

DATA_PATH = f'./dataset/{MONTH_YEAR}/'

DATA_PATH_ORIGINAL = f'./dataset/{MONTH_YEAR}/original/'

STATEMENTS = ['DEBIT_HDFC','CREDIT_HDFC','DEBIT_STD','CREDIT_CITI']

PASSWORDS =  {'DEBIT_HDFC': None, 'CREDIT_HDFC': 'DOOS0406', 'DEBIT_STD':None, 'CREDIT_CITI':'DOOS04JUN'}

DEBIT_HDFC_ORIGINAL = os.path.join(DATA_PATH_ORIGINAL, 'DEBIT_HDFC.xls')
CREDIT_HDFC_ORIGINAL = os.path.join(DATA_PATH_ORIGINAL, 'CREDIT_HDFC.pdf')
DEBIT_STD_ORIGINAL = os.path.join(DATA_PATH_ORIGINAL, 'DEBIT_STD.csv')
CREDIT_CITI_ORIGINAL = os.path.join(DATA_PATH_ORIGINAL, 'CREDIT_CITI.pdf')
TEMP = os.path.join(DATA_PATH_ORIGINAL, 'TEMP.pdf')

DEBIT_HDFC = os.path.join(DATA_PATH, 'DEBIT_HDFC.csv')
CREDIT_HDFC = os.path.join(DATA_PATH, 'CREDIT_HDFC.csv')
DEBIT_STD = os.path.join(DATA_PATH, 'DEBIT_STD.csv')
CREDIT_CITI = os.path.join(DATA_PATH, 'CREDIT_CITI.csv')

ALL_TRANSACTIONS = os.path.join(DATA_PATH, 'TRANSACTIONS.csv')

EXPENSES_PLOT = os.path.join(DATA_PATH, 'expenses.png')