import pandas as pd
from pathlib import Path

def load_csv_data(dir="../data/all_records_csvs") -> pd.DataFrame:
    dir = Path(dir)

    # our filenames are predetermined:
    channelnames = ["Al-Jazeera-English", "BBC-News", "CCTV-Video-News-Agency", "CNN-News", "DW-News", "Fox-News"]

    # initialize an empty dataframe
    df = pd.DataFrame()

    # combine all the datasets
    for channel in channelnames:
        filename = channel + ".csv"
        df1 = pd.read_csv(dir / filename)

        # clean leading and trailing whitespaces, if any
        df1.columns = [col.strip().lower() for col in df1.columns]
        
        # add additional column 'Channel' to each data set
        df1["channel"] = channel
        df = pd.concat([df, df1])
    
    return df

