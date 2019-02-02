def budget_update(balances,payperiod_transactions):
    desired_balances = ['Huntington Bank Asterisk-Free Checking', 'Huntington Bank Premier Savings',
                        'Mutual Savings Bank (Franklin, IN) QUINN M ANGRICK - CHECKING']
    total_spent = 0

    msg = 'Balances: \n'
    for key in desired_balances:
        msg += key + " " + balances[key] + "\n"

    msg += "\nTransactions This Pay Period: \n"

    for transaction in payperiod_transactions:
        total_spent += float(transaction[2])
        msg += transaction[0] + " " + transaction[1] + " " + transaction[2] + " " + "\n"

    msg+='Total Spent: ' + str(total_spent)


    return msg

if __name__ == "__main__":
    print(budget_update({'Huntington Bank Asterisk-Free Checking': '$232.12', 'Huntington Bank Premier Savings':
        '$2,051.61', 'Macatawa Bank - Personal HEALTH SAVINGS FAMILY': '$0.93', 'Mutual Savings Bank (Franklin, IN) QUINN M ANGRICK - CHECKING':
        '$1,740.71', 'FedLoan Servicing Direct Sub Stafford Loan': '-$1,958.29', 'FedLoan Servicing Direct Unsub Stafford Loan': '$0.00',
                         'FedLoan Servicing Federal Stafford Loan': '$0.00', 'FedLoan Servicing Federal Unsub Stafford Loan': '$0.00',
                         'Mutual Savings Bank (Franklin, IN) QUINN M ANGRICK - MORTGAGE LOAN': '-$150,918.52', 'Indiana CollegeChoice529 Asher M Angrick': '$856.98',
                         'Indiana CollegeChoice529 Calum N Angrick': '$856.98', 'Indiana CollegeChoice529 Hezekiah M Angrick': '$869.51',
                         'Wells Fargo Gentex Corp Retirement Svngs Pl & Trust': '$9,649.57', 'Vehicle Chevrolet Impala': '$1,644.00', 'Vehicle Chrysler Town & Country': '$5,524.00'},
                        [('12/03/2018', 'Huntington Cash Withdrawal 1126 North Main Street', '60.00'),
                        ('12/03/2018', 'ABCMouse', '9.95'), ('12/03/2018', 'ABCMouse', '4.95'),
                        ('12/03/2018', 'Wal-Mart', '169.41'),
                        ('12/03/2018', 'Huntington Cash Withdrawal 1126 North Main Street', '40.00'),
                        ('12/03/2018', 'Wal-Mart', '48.07'), ('12/03/2018', 'Toyota Cafeteria', '4.69'),
                        ('11/30/2018', "Papa Murphy's", '27.41'), ('11/29/2018', 'Wal-Mart', '7.40'),
                        ('11/29/2018', 'Toyota Cafeteria', '4.69'), ('11/29/2018', "Fazoli's", '19.43'),
                        ('11/28/2018', 'Marathon', '35.11'), ('11/28/2018', 'Amazon', '50.00'),
                        ('11/28/2018', 'Amazon', '173.61'), ('11/27/2018', 'Wal-Mart', '107.59'),
                        ('11/26/2018', 'Wal-Mart', '22.86'), ('11/26/2018', 'Wal-Mart', '81.60'),
                        ('11/26/2018', "Tom's Pancake House", '53.00'), ('11/26/2018', "Steak 'n Shake", '22.21'),
                        ('11/26/2018', 'Steam Games', '21.50'), ('11/26/2018', "Lowe's", '2.74'),
                        ('11/26/2018', 'Luca Pizza', '7.50'), ('11/26/2018', 'Amazon', '31.55'),
                        ('11/26/2018', 'Giv Fairhaven', '295.00'), ('11/26/2018', 'Moe Sw Grill', '22.93'),
                        ('11/26/2018', 'Merchandise Ret Walmart', '8.88'), ('11/26/2018', "Lowe's", '21.08')]))