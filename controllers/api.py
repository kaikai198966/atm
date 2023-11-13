import env  # import the environment variables module
import controllers.fs as fs  # import the file manager module


# read the users file and return a dictionary of all users
def get_all_users():
    users = {}  # placeholder dictionary for all users

    file = fs.read(env.files["users"]).split("\n")

    # read the users file and loop through it
    for line in file:  # loop through the file
        # one line in the file is one user's data
        line = line.strip()

        # split the pipe-separated data into a list
        user_id, password, user_type, status, date_created = line.split("|")
        # assign the values to the keys of the user's dictionary
        users[user_id] = {
            "username": user_id,
            "password": password,
            "type": user_type,
            "status": status,
            "date_created": date_created,
        }  # placeholder dictionary of a user

    return users  # return the dictionary of ALL users


# read the accounts file and return a dictionary of all accounts
def get_all_accounts():
    accounts = {}  # placeholder dictionary for all accounts

    file = fs.read(env.files["accounts"]).split("\n")

    # read the accounts file and loop through it
    for line in file:  # loop through the file
        # one line in the file is one account's data
        line = line.strip()  # remove the trailing spaces

        # split the pipe-separated data into a list
        (
            user_id,
            act_num,
            act_name,
            outstand_bal,
            last_transaction_date,
            last_transaction_details,
        ) = line.split("|")
        # assign the values to the keys of the account's dictionary
        accounts[user_id] = {
            "user_id": user_id,
            "account_number": act_num,
            "account_name": act_name,
            "outstanding_balance": outstand_bal,
            "last_transaction_date": last_transaction_date,
            "last_transaction_details": last_transaction_details,
        }  # placeholder dictionary of an account

    return accounts  # return the dictionary of ALL accounts


def get_all_transactions():
    transactions = []  # placeholder dictionary for all transactions

    file = fs.read(env.files["transaction_details"]).split("\n")

    # read the transactions file and loop through it
    for line in file:
        # one line in the file is one transaction made
        line = line.strip()  # remove the trailing spaces
        (tran_date, act_num, tran_code, tran_amount) = line.split("|")
        # assign the values to the keys of the transaction's dictionary
        transactions.append(
            {
                "transaction_date": tran_date,
                "account_number": act_num,
                "transaction_code": tran_code,
                "transaction_amount": tran_amount,
            }
        )  # placeholder dictionary of an account's transactions

    return transactions  # return the dictionary of ALL transactions


def get_user(user_id):
    users = get_all_users()  # get all users
    return users.get(user_id)  # return the user with the given user_id


def get_account(user_id):
    accounts = get_all_accounts()  # get all accounts
    return accounts.get(user_id)  # return the account with the given user_id

def get_transactions(account_number):
    all_transactions = get_all_transactions()  # get all transaction
    account_transactions = []
    for transactions in all_transactions:
        if transactions["account_number"] == account_number:
            del transactions["account_number"]
            account_transactions.append(transactions)
    return account_transactions  # return the account with the given transaction


def append_user(
    user_data={
        "user_id": None,
        "password": None,
        "type": None,
        "status": None,
        "created_date": None,
    }
):
    # take every values and create a pipe-separated string
    data = user_data["user_id"] + "|"
    +user_data["password"] + "|"
    +user_data["type"] + "|"
    +user_data["status"] + "|"
    +user_data["created_date"] + "\n"

    fs.append(env.files["users"], data)  # overwrite the file with the new data

    return data  # return the dictionary of the account


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
    # take every values and create a pipe-separated string
    data = account_data["user_id"] + "|"
    +account_data["account_number"] + "|"
    +account_data["account_name"] + "|"
    +account_data["outstanding_balance"] + "|"
    +account_data["last_transaction_date"] + "\n"

    fs.append(env.files["accounts"], data)  # overwrite the file with the new data

    return data  # return the dictionary of the account


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
    accounts = get_all_accounts()  # get all accounts
    accounts[account_data["user_id"]]  # modify the account with the given user_id
    set_accounts(accounts)  # overwrite the file with the new data

    return account_data  # return the dictionary of the accountusers


def set_accounts(accounts_data={}):
    data = ""

    # loop through the accounts dictionary
    for account in accounts_data:
        # each key is an account
        # take each value and create a pipe-separated string
        data += account["user_id"] + "|"
        +account["account_number"] + "|"
        +account["account_name"] + "|"
        +account["outstanding_balance"] + "|"
        +account["last_transaction_date"] + "|"
        +account["last_transaction_details"] + "\n"

    fs.write(env.files["accounts"], data)  # overwrite the file with the new data


def append_transaction_details(
    transaction_data={
        "transaction_date": None,
        "account_number": None,
        "transaction_code": None,
        "transaction_amount": None,
    }
):
    # take every values and create a pipe-separated string
    data = transaction_data["transaction_date"] + "|"
    +transaction_data["account_number"] + "|"
    +transaction_data["transaction_code"] + "|"
    +transaction_data["transaction_amount"] + "\n"

    fs.append(
        env.files["transaction_details"], data
    )  # overwrite the file with the new data
