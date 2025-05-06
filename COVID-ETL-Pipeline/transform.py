import pandas as pd
from datetime import datetime


def transform_data(data):
    df = pd.DataFrame(data)

    df = df[['country', 'cases', 'deaths', 'recovered', 'updated']]
    df['last_updated'] = df['updated'].apply(lambda x: datetime.utcfromtimestamp(x / 1000))

    df = df.drop(columns=['updated'])

    print ("Transform successful")
    return df