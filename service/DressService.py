import DataMockService as dms
import pandas as pd
from datetime import datetime

# Create a dictionary with the month numbers as keys and the month names as values
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

db_data = {}


def driver():
    db_data = mock_df_to_dict()
    print("Work on this data :")
    print(db_data)
    dates = date_values(db_data)

    non_date_items = get_non_date_data(db_data)
    print("Non Date Items :")
    print(non_date_items)

    grouped_month_sales_data = group_by_month_sum_sales(dates)
    print("Grouped Sales Data :")
    print(grouped_month_sales_data)

    print("Merged Dicts :")
    merged_dicts = merge_two_dicts(non_date_items, grouped_month_sales_data)
    print(merged_dicts)

    final_df = pd.DataFrame(merged_dicts)
    print(final_df)


def mock_df_to_dict():
    mock_df = dms.mock_mohit_scenario()
    data = mock_df.to_dict('list')
    return data


def date_values(db_data):
    new_data = {}
    items = iter(db_data.items())
    first_item = next(items)

    for k, v in items:
        new_data[k] = v
    # print(new_data)
    return new_data


def group_by_month_sum_sales(data_dict):
    month_grp_sales = {}
    for date_string, sales_list in data_dict.items():
        month_name = strip_month_as_string(date_string)
        if month_name in month_grp_sales:
            old_list = month_grp_sales[month_name]
            sum_up_list = add_two_lists(old_list, sales_list)
            month_grp_sales[month_name] = sum_up_list
        else:
            month_grp_sales[month_name] = sales_list

    # print(month_grp_sales)
    return month_grp_sales


def strip_month_as_string(date_string):
    month_num = datetime.strptime(date_string, '%Y-%m-%d').month
    month_str = month_dict[month_num]
    # print(month_str)
    return month_str


def add_two_lists(list1, list2):
    result = [sum(i) for i in zip(list1, list2)]
    return result


def get_non_date_data(db_data):
    copy_db_data = db_data
    items = iter(copy_db_data.items())
    first_item = next(items)
    tuple_to_dict = convert_to_dict(*first_item)
    return tuple_to_dict


def convert_to_dict(key, values):
    result_dict = {key: values}
    return result_dict


def merge_two_dicts(non_date_dict, month_sales_data_dict):
    for month,month_wise_sales in month_sales_data_dict.items():
        non_date_dict[month] = month_wise_sales
    return non_date_dict

if __name__ == '__main__':
    # strip_month_as_string('2023-12-10')
    # d = df_to_dict()
    # date_values(d)
    # {'2023-03-10': [72, 47, 40, 7, 75, 23, 84, 34, 65, 16], '2023-03-11': [76, 9, 22, 44, 43, 59, 15, 8, 31, 92]
    test_dicts = {'2023-03-10': [72, 47, 40, 7, 75, 23, 84, 34, 65, 16],
                  '2023-03-11': [76, 9, 22, 44, 43, 59, 15, 8, 31, 92],
                  '2023-01-10': [72, 47, 40, 7, 75, 23, 84, 34, 65, 16],
                  '2023-03-11': [76, 9, 22, 44, 43, 59, 15, 8, 31, 92],
                  '2023-05-10': [72, 47, 40, 7, 75, 23, 84, 34, 65, 16],
                  '2023-01-11': [76, 9, 22, 44, 43, 59, 15, 8, 31, 92],
                  }
    # data = group_by_month_sum_sales(test_dicts)
    # print(data)
    driver()
    # t = ((1, 'a'))
    # d = dict(t)
    # print(d)
