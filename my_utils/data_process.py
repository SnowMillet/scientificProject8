from rqdatac import is_st_stock
import datetime
import seaborn as sns
import numpy as np
import pandas as pd


# 打标签
def label_data(data: pd.DataFrame, percent_select, is_show=False) -> pd.DataFrame:
    data = data.sort_values(by='yield_rate', ascending=False)

    n_stock_select = np.multiply(percent_select, data.shape[0])
    n_stock_select = np.around(n_stock_select).astype(int)

    # 绘制分布
    if is_show:
        iloc_yield_rate = data.columns.get_loc('yield_rate')

        select_data_yield_rate = pd.concat(
            [data.iloc[n_stock_select[i][0]:n_stock_select[i][1], iloc_yield_rate] for i in
             range(n_stock_select.shape[0])])

        sns.displot(data=select_data_yield_rate, kde=True, aspect=3)

    # 打标签
    data.insert(loc=0, column='return_bin', value=np.nan)

    for i in range(n_stock_select.shape[0]):
        data.iloc[n_stock_select[i][0]:n_stock_select[i][1], data.columns.get_loc('return_bin')] = i

    data = data.dropna(axis=0)

    return data


# 剔除 ST 股票
def remove_st(stocks_list: list, date: datetime.date) -> list:
    temp0 = is_st_stock(order_book_ids=stocks_list,
                        start_date=date,
                        end_date=date)

    temp1 = pd.DataFrame(temp0.values.T,
                         index=temp0.columns,
                         columns=['is_st_stock'])

    temp2 = temp1[temp1['is_st_stock'] == False]

    stocks_list_no_st = temp2.index.values.tolist()

    return stocks_list_no_st


# 计算每月最后一个交易日的日期
def calculate_last_trading_date_month(trading_dates_list: list) -> list:
    trading_dates_list_m = list()
    for i in range(len(trading_dates_list) - 1):
        if trading_dates_list[i].month != trading_dates_list[i + 1].month:
            trading_dates_list_m.append(trading_dates_list[i])
        else:
            pass
    return trading_dates_list_m


if __name__ == '__main__':
    pass
