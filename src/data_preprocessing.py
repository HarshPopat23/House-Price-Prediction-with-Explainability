import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def basic_cleaning(df):
    df = df.copy()

    drop_cols = [
        'Alley', 'Mas Vnr Type', 'Fireplace Qu',
        'Pool QC', 'Fence', 'Misc Feature'
    ]
    df.drop(columns=drop_cols, inplace=True)

    mean_cols = [
        'Lot Frontage', 'Mas Vnr Area', 'BsmtFin SF 1',
        'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
        'Bsmt Full Bath', 'Bsmt Half Bath',
        'Garage Cars', 'Garage Area'
    ]
    df[mean_cols] = df[mean_cols].fillna(df[mean_cols].mean())

    garage_cols = ['Garage Type', 'Garage Finish', 'Garage Qual', 'Garage Cond']
    df[garage_cols] = df[garage_cols].fillna("No Garage")

    df['Electrical'] = df['Electrical'].fillna(df['Electrical'].mode()[0])
    df['Garage Yr Blt'] = df['Garage Yr Blt'].fillna(df['Year Built'])

    bsmt_cols = [
        'Bsmt Qual', 'Bsmt Cond', 'Bsmt Exposure',
        'BsmtFin Type 1', 'BsmtFin Type 2'
    ]
    df[bsmt_cols] = df[bsmt_cols].fillna("No Basement")

    df['Central Air'] = df['Central Air'].map({'Y': 1, 'N': 0})

    return df
