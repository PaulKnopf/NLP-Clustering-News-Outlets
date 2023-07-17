import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
from utils import load_csv_data

# This function combines our 6 csv datasets from different channels into 1
def process_data():
    df = load_csv_data()

    # group by 'Title' & ' Description', and sort by descending ' Views'
    df.groupby(by=['Title', ' Description'])
    df.sort_values(by=[' Views'], ascending=False)

    # output as CSV-file to designated folder with current date in name
    today = date.today()
    string_today = "{}-{}-{}".format(today.day, today.month, today.year)
    df.to_csv("..\\data\\combined-" + string_today + ".csv", index=False)

    # store the csv file as a read file for output
    csv_file = pd.read_csv("..\\data\\combined-" + string_today + ".csv")
    return csv_file


# This function creates plots for exploratory data analysis (EDA)
def create_plots(csv_file):
    df = csv_file
    print("Dataframe dimension (#rows, #columns): ")
    print(df.shape)

    # Set the range intervals for the x-axis
    view_ranges = [0, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 3000000, np.inf]
    labels = ['0-1K', '1K-5K', '5K-10K', '10K-50K', '50K-100K', '100K-500K', '500K-1M', '1M-3M', '3M+']

    # Group the data by channel and count the frequencies for each view range
    channel_counts = df.groupby('Channel')[' Views'].apply(lambda x: np.histogram(x, bins=view_ranges)[0])
    num_channels = len(channel_counts)

    # Create the line graph for each channel
    for i, (channel, counts) in enumerate(channel_counts.items()):
        plt.plot(labels, counts, marker='o', label=channel)

    # Set the labels and title
    plt.xlabel('Views Range')
    plt.ylabel('Frequency')
    plt.title('Frequency of Views Range by Channel')

    # Rotate the x-axis labels if needed
    plt.xticks(rotation=45)

    # Add legend
    plt.legend()

    # Adjust the figure size to show the legend properly
    fig = plt.gcf()
    fig.set_size_inches(12, 10)

    # Save the plot
    plt.savefig('..\\graphs\\views-by-channel.png')

    # Display the chart
    plt.show()

create_plots(process_data())

# if __name__ == '__main__':
#     dw_news_data_frame = pd.read_csv("..\\data\\DW-News.csv")
#
#     print(dw_news_data_frame.columns.tolist())
#     dw_news_sorted = dw_news_data_frame.sort_values(by=['Title'])
#
#     titles = dw_news_data_frame['Title'].unique()
#     processed_data = dw_news_data_frame.groupby(by=['Title', ' Description']).max()
#     # print(titles)
#     # print(len(titles))
#     # print("sorted data: ", dw_news_sorted)
#     print(processed_data)
