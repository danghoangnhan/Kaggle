import pandas as pd


def fillMissing(df, alter: dict):
    for key in alter:
        df[key] = df[key].fillna(alter[key])
    return df


def dropFields(df, cols):
    for field in cols:
        df.drop([field], axis=1, inplace=True)
    return df


def category_onehot_multcols(columns, original_df):
    df_final = original_df
    i = 0
    for fields in columns:
        df1 = pd.get_dummies(original_df[fields],
                             drop_first=True)
        original_df.drop([fields], axis=1, inplace=True)
        if i == 0:
            df_final = df1.copy()
        else:
            df_final = pd.concat([df_final, df1], axis=1)
        i = i + 1
    df_final = pd.concat([original_df, df_final], axis=1)
    return df_final


def generatedData(fileName: str = "test.csv"):
    df = pd.read_csv(fileName)
    df = fillMissing(df)
    df.drop(['Alley'], axis=1, inplace=True)
    df['BsmtCond'] = df['BsmtCond'].fillna(df['BsmtCond'].mode()[0])
    df['BsmtQual'] = df['BsmtQual'].fillna(df['BsmtQual'].mode()[0])
    df['FireplaceQu'] = df['FireplaceQu'].fillna(df['FireplaceQu'].mode()[0])
    df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])
    df.drop(['GarageYrBlt'], axis=1, inplace=True)
    df['GarageFinish'] = df['GarageFinish'].fillna(df['GarageFinish'].mode()[0])
    df['GarageQual'] = df['GarageQual'].fillna(df['GarageQual'].mode()[0])
    df['GarageCond'] = df['GarageCond'].fillna(df['GarageCond'].mode()[0])

    df.drop(['Id'], axis=1, inplace=True)
    df.drop(['PoolQC', 'Fence', 'MiscFeature'], axis=1, inplace=True)

    df['MasVnrType'] = df['MasVnrType'].fillna(df['MasVnrType'].mode()[0])
    df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].mode()[0])
    df['BsmtExposure'] = df['BsmtExposure'].fillna(df['BsmtExposure'].mode()[0])
    df['BsmtFinType2'] = df['BsmtFinType2'].fillna(df['BsmtFinType2'].mode()[0])

    X = df.drop(['SalePrice'], axis=1)
    Y = df['SalePrice']

    return X, Y


def export(df, fileName: str = 'formulatedtest.csv'):
    df.to_csv(fileName, index=False)
