import pandas as pd
from pathlib import Path

def load_data(dir="data") -> pd.DataFrame:
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
        for col_name in df1.columns:
            col_name.strip()
        # add additional column 'Channel' to each data set
        df1["channel"] = channel
        df = pd.concat([df, df1])
        return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    

