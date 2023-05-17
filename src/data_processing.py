import pandas


if __name__ == '__main__':
    dw_news_data_frame = pandas.read_csv("..\\data\\DW-News.csv")

    print(dw_news_data_frame.columns.tolist())
    dw_news_sorted = dw_news_data_frame.sort_values(by=['Title'])

    titles = dw_news_data_frame['Title'].unique()
    processed_data = dw_news_data_frame.groupby(by=['Title', ' Description']).max()
    # print(titles)
    # print(len(titles))
    # print("sorted data: ", dw_news_sorted)
    print(processed_data)
