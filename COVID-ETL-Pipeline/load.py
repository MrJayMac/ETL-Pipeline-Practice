from sqlalchemy import create_engine

def load_data(df, db_connection_string):

    engine = create_engine(db_connection_string)

    df.to_sql(
        name='covid_stats',
        con=engine,
        if_exists='replace',
        index=False
    )

    print ("Data loaded successfully into PostgreSQL")