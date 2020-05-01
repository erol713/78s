import pandas as pd
import json
import numpy as np


def dpsum(request):

    df = pd.read_excel(
        'reports/Vivacom - Data Protector/Report/Vivacom Data Protector Deployment Table.xlsx')

    df = df[1:]  # take the data less the header row

    new_header = df.iloc[0]  # grab the first row for the header
    df.columns = new_header
    df = df[1:]
    df = pd.DataFrame(df)
    df = df.reset_index(drop=True)
    df = df.rename(columns={np.nan: 'values'})
    x = df['DATA PROTECTOR'].isnull().idxmax()

    summ = df[:x]
    summ = summ[summ['DATA PROTECTOR'].notnull()]
    summ = summ[(summ['Production'] != 0) | (summ['Non-production'] != 0)]
    summ = summ.drop('values', axis=1)
    summ = summ.reset_index(drop=True)
    summ['Licenses'] = summ['DATA PROTECTOR']
    summ = summ.drop('DATA PROTECTOR', axis=1)
    summ = summ.to_json()

    return (summ)
