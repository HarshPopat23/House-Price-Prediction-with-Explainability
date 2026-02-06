import pandas as pd
from sklearn.preprocessing import StandardScaler

def encode_categorical(df):
    cat_cols = [
        'MS Zoning','Street','Lot Shape','Land Contour','Utilities',
        'Lot Config','Land Slope','Condition 1','Condition 2',
        'Bldg Type','House Style','Roof Style','Roof Matl',
        'Exter Qual','Exter Cond','Foundation',
        'Bsmt Qual','Bsmt Cond','Bsmt Exposure',
        'BsmtFin Type 1','BsmtFin Type 2',
        'Heating','Heating QC','Electrical','Kitchen Qual',
        'Functional','Garage Type','Garage Finish',
        'Garage Qual','Garage Cond','Sale Type',
        'Sale Condition','Neighborhood',
        'Exterior 1st','Exterior 2nd','Paved Drive'
    ]

    return pd.get_dummies(df, columns=cat_cols, drop_first=True)


def scale_numerical(df):
    num_cols = [
        'PID','MS SubClass','Lot Frontage','Lot Area',
        'Overall Qual','Overall Cond','Year Built',
        'Year Remod/Add','Mas Vnr Area',
        'BsmtFin SF 1','BsmtFin SF 2','Bsmt Unf SF',
        'Total Bsmt SF','1st Flr SF','2nd Flr SF',
        'Low Qual Fin SF','Gr Liv Area','TotRms AbvGrd',
        'Garage Yr Blt','Garage Area','Wood Deck SF',
        'Open Porch SF','Enclosed Porch','3Ssn Porch',
        'Screen Porch','Pool Area','Misc Val',
        'Mo Sold','Yr Sold'
    ]

    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df
