import csv
import datetime



def mint_data(account_data):
    matched_transactions = []
    descs = []
    dates = []
    data_list = []

    with open(account_data) as f:
        data = csv.DictReader(f)
        for row in data:
            descs.append(row['Description'])
            dates.append(row['Date'])
            data_list.append(row)
        paycheck = datetime.datetime.strptime(dates[descs.index('Toyota Industria Direct')],"%m/%d/%Y").date()
        for transaction in data_list:
            transdate = datetime.datetime.strptime(transaction["Date"],"%m/%d/%Y").date()
            is_this_payperiod = transdate > paycheck
            if is_this_payperiod:
                matched_transactions.append((transaction["Date"],transaction['Description'], transaction['Amount']))

    return matched_transactions

if __name__ == "__main__":
    print(mint_data('test_transactions.csv'))