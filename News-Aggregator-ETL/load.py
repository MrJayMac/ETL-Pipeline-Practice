from sqlalchemy import create_engine

def load_data(df, connection_string):
    engine = create_engine(connection_string)


    df.to_sql(
        name='news_articles',
        con=engine,
        if_exists='replace',
        index=False
    )

    print ("Data loaded successfully into PostgreSQL")