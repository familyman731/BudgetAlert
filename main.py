import download
import send_email
import datetime
import filter_
import build_message

balances, account_data = download.downloadMintData()
payperiod_transactions = filter_.mint_data(account_data)
msg = build_message.budget_update(balances,payperiod_transactions)

with open("previous msg.txt",'r+') as f:
    prevMsg = f.read()
    if msg == prevMsg:
        print("No new transactions. Email not sent.")
        exit()
    f.seek(0)
    f.write(msg)

subject = str(datetime.date.today())+ " Transactions"
send_email.send_email(subject,msg)
