import pandas as pd
import random


def mock_mohit_scenario():
    df = mock_dress_ids_for_date()
    date_wise_sales = make_date_wise_sales_data()
    #print(date_wise_sales)
    #print('################')
    date_wise_sales_df = pd.DataFrame(date_wise_sales)
    #print(date_wise_sales_df)
    # output_df = pd.concat([df, date_wise_sales_df], ignore_index=True)

    for key in date_wise_sales:
        df[key] = date_wise_sales_df[key]

    return df
    #print(df)


# def mock_dress_df():
#     print(pd.date_range(start='2019-4-1', end='2019-4-30', freq='D'))


# method return the dates of month as string list
def mock_list_date_of_month():
    df = pd.date_range(start='2023-3-10', end='2023-4-15', freq='D')

    l = [d.strftime('%Y-%m-%d') for d in df]
    # print(l)
    return l


# assuming there are 10 dresses..
# every date is a column
# here we will create 10 entries for every date

def mock_dress_ids_for_date():
    dress_pk_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dress_col_name = 'dress_id'
    df = pd.DataFrame(dress_pk_values, columns=[dress_col_name])
    # print(df)
    return df


def make_date_wise_sales_data():
    month_wise_sales = {}
    list_of_dates = mock_list_date_of_month()

    for i in range(len(list_of_dates)):
        month_wise_sales[list_of_dates[i]] = give_x_random_nums(10)

    # print(month_wise_sales)
    return month_wise_sales


# since the their are 10 dress, call this method
# this method return sales for x dresses
def give_x_random_nums(dress_count):
    rand_list = []
    for i in range(dress_count):
        rand_list.append(random.randint(1, 100))
    # print(rand_list)
    return rand_list


if __name__ == '__main__':
    # mock_dress_df()
    mock_list_date_of_month()
    # mock_dress_ids_for_date()
    # give_x_random_nums(10)
    #make_date_wise_sales_data()
    # mock_mohit_scenario()
