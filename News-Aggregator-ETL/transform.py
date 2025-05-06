import pandas as pd


def transform_data(data):

    articles = data.get('articles', [])
    

    df = pd.json_normalize(articles)
    
  
    df = df[['source.name', 'author', 'title', 'description', 'content', 'url', 'publishedAt']]
    
    print("Transform successful")
    return df