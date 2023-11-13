path = {
    "users": "./atm-files/users.txt",
    "accounts": "./atm-files/accounts.txt",
    "transaction_details": "./atm-files/tran_details.txt",
    "transaction_table": "./atm-files/tran_table.txt",
}

def get_all_users():
    users = {} 

    with open(path["users"], "rt") as file:
        file = file.split("\n")
        for line in file: 
            line = line.strip()
            user_id, password, user_type, status, date_created = line.split("|")
            users[user_id] = {
                "username": user_id,
                "password": password,
                "type": user_type,
                "status": status,
                "date_created": date_created,
            } 

    return users  

def get_all_accounts():
    accounts = {}

    with open(path["accounts"], "rt") as file:
        file = file.split("\n")
        for line in file:  
            line = line.strip()
            (
                user_id,
                act_num,
                act_name,
                outstand_bal,
                last_transaction_date,
                last_transaction_details,
            ) = line.split("|")

            accounts[user_id] = {
                "user_id": user_id,
                "account_number": act_num,
                "account_name": act_name,
                "outstanding_balance": outstand_bal,
                "last_transaction_date": last_transaction_date,
                "last_transaction_details": last_transaction_details,
            }

    return accounts 


def get_all_transactions():
    transactions = []

    with open(path["transaction_details"], "rt") as file:
        file = file.split("\n")
        for line in file:
            line = line.strip()  
            (tran_date, act_num, tran_code, tran_amount) = line.split("|")
            transactions.append(
                {
                    "transaction_date": tran_date,
                    "account_number": act_num,
                    "transaction_code": tran_code,
                    "transaction_amount": tran_amount,
                }
            ) 

    return transactions 


def get_user(user_id):
    users = get_all_users() 
    return users.get(user_id)


def get_account(user_id):
    accounts = get_all_accounts()
    return accounts.get(user_id)


def get_transactions(account_number):
    all_transactions = get_all_transactions()
    account_transactions = []
    for transactions in all_transactions:
        if transactions["account_number"] == account_number:
            del transactions["account_number"]
            account_transactions.append(transactions)
    return account_transactions 


def append_user(
    user_data={
        "user_id": None,
        "password": None,
        "type": None,
        "status": None,
        "created_date": None,
    }
):
    
    data = user_data["user_id"] + "|"
    +user_data["password"] + "|"
    +user_data["type"] + "|"
    +user_data["status"] + "|"
    +user_data["created_date"] + "\n"

    with open(path["users"], "at") as file:
        file.write(data)
    return data  
    
def append_account(
    account_data={
        "user_id": None,
        "account_number": None,
        "account_name": None,
        "outstanding_balance": None,
        "last_transaction_date": None,
        "last_transaction_details": None,
    }
):

    data = account_data["user_id"] + "|"
    +account_data["account_number"] + "|"
    +account_data["account_name"] + "|"
    +account_data["outstanding_balance"] + "|"
    +account_data["last_transaction_date"] + "\n"

    with open(path["accounts"], "at") as file:
        file.write(data)

    return data


def append_to_account(
    account_data={
        "user_id": None,
        "account_number": None,
        "account_name": None,
        "outstanding_balance": None,
        "last_transaction_date": None,
        "last_transaction_details": None,
    }
):
    accounts = get_all_accounts() 
    accounts[account_data["user_id"]]
    set_accounts(accounts) 

    return account_data


def set_accounts(accounts_data={}):
    data = ""
    
    for account in accounts_data:
        data += account["user_id"] + "|"
        +account["account_number"] + "|"
        +account["account_name"] + "|"
        +account["outstanding_balance"] + "|"
        +account["last_transaction_date"] + "|"
        +account["last_transaction_details"] + "\n"

    with open(path["accounts"], "wt") as file:
        file.write(data)
    


def append_transaction_details(
    transaction_data={
        "transaction_date": None,
        "account_number": None,
        "transaction_code": None,
        "transaction_amount": None,
    }
):

    data = transaction_data["transaction_date"] + "|"
    +transaction_data["account_number"] + "|"
    +transaction_data["transaction_code"] + "|"
    +transaction_data["transaction_amount"] + "\n"

    with open(path["transaction_details"], "at") as file:
        file.write(data)


