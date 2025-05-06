import pandas as pd

def transform_data(data):
    if data is None:
        print("Error: No data provided to transform.")
        return None
        
    if 'daily' not in data:
        print("Error: 'daily' key not found in data.")
        return None

    daily_data = data['daily']
    df = pd.DataFrame(daily_data)
    
    # Add time column if not present
    if 'time' not in df.columns:
        # The API returns dates in order, so we can create a date range
        from datetime import datetime, timedelta
        today = datetime.now().date()
        dates = [today + timedelta(days=i) for i in range(len(df))]
        df['time'] = [d.strftime('%Y-%m-%d') for d in dates]

    df = df.rename(columns={
        'temperature_2m_max':'tempmax',
        'temperature_2m_min':'tempmin',
        'precipitation_sum':'totalrainfall',
    })

    # Ensure all required columns exist
    for col in ['time', 'tempmax', 'tempmin', 'totalrainfall']:
        if col not in df.columns:
            print(f"Error: '{col}' column missing in transformed data.")
            return None
            
    df = df[['time', 'tempmax', 'tempmin', 'totalrainfall']]
    
    print("Data transformed successfully")
    return df