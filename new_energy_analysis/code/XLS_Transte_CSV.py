import pandas as pd


# 2使用第三方库pandas将xlsx文件转csv文件
def xlsx_to_csv_pd():
    data_xls = pd.read_excel('../data/2.xls', index_col=0)
    print('type(data_xls) :\n', type(data_xls))
    print(data_xls)
    print('--------')
    data_xls = data_xls.drop(labels=u'dateTime', axis=1)
    print(data_xls)
    data_xls.to_csv('../data/2.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()