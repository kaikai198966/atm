# this menu will be displayed when the type of the user is admin ("adm")
import time
import controllers.api as api
import utils


def check_for_balance(user_id):
    user = api.get_account(user_id=user_id)

    user_id = user["user_id"]
    balance = user["outstanding_balance"]

    api.append_transaction_details(
        {
            "transaction_date": utils.timestamp(),
            "account_number": user["account_number"],
            "transaction_code": "chk",
        }
    )

    prompt = f"Hi, {user_id}! Your current balance is {balance}."
    print(prompt)


def make_deposit(user_id):
    amount = input("Enter amount to Deposit: ")
    amount = float(amount)
    if amount < 0:
        print("Deposit amount must be greater than zero")
        return  # TODO: CONSULT KAI IF the error should pushed through to be logged
    elif amount > 500000:
        print("Deposit amount must not be greater than 500,000")
        return  # TODO: CONSULT KAI IF the error should pushed through to be logged

    account = api.get_account(user_id)
    account["outstanding_balance"] += amount
    api.append_account(account)
    api.append_transaction_details(
        {
            "transaction_date": utils.timestamp(),
            "account_number": account["account_number"],
            "transaction_code": "dep",
            "transaction_amount": amount,
        }
    )

    prompt = f"""Deposit Transaction successfully completed.
    Your new Outstanding balance is {account["outstanding_balance"]}.
    """
    print(prompt)


def make_withdrawal(user_id):
    amount = input("Enter amount to Withdraw: ")
    amount = float(amount)
    if amount < 0:
        print("Withdrawal Amount must be greater than zero")

    account = api.get_account(user_id)

    if account["outstanding_balance"] < amount:
        print(f"Amount must not be greater than {account['outstanding_balance']}")

    account["outstanding_balance"] -= amount

    api.append_account(account)
    api.append_transaction_details(
        {
            "transaction_date": utils.timestamp(),
            "account_number": account["account_number"],
            "transaction_code": "wdr",
            "transaction_amount": amount,
        }
    )

    prompt = f"""Withdrawal Transaction is successfully completed.
    Your new Outstanding balance is {account["outstanding_balance"]}.
    """
    print(prompt)


def report_transaction(user_id):
    print("Transaction Report")

    date_range_start = input("Enter Start Date (mm/dd/yyyy): ")
    date_range_end = input("Enter End Date (mm/dd/yyyy): ")

    account = api.get_account(user_id)
    transactions = api.get_transactions(account["account_number"])

    prompt = (
        f"List of transactions for Account Number {account['account_number']}"
        + f"from {date_range_start} to {date_range_end} are as follows:\n"
    )
    print(prompt)

    prompt_header = (
        "Transaction Date\t"
        + "Transaction Time\t"
        + "Transaction Amount\t"
        + "Running Balance\n"
    )

    print(prompt_header)

    for transaction in transactions:
        # TODO CONSULT KAI about the float problem

        transaction_date = transaction["transaction_date"].split("_")[0]
        transaction_time = transaction["transaction_date"].split("_")[1]

        # TODO CONSULT KAI about the time options

        running_balance = 0

        transaction["transaction_amount"] = (
            float(transaction["transaction_amount"])
            if transaction["transaction_amount"]
            else 0
        )
        if (
            transaction["transaction_code"] == "dep"
            or transaction["transaction_code"] == "new"
        ):
            running_balance += transaction["transaction_amount"]
        if transaction["transaction_code"] == "wdr":
            running_balance -= transaction["transaction_amount"]

        if time.strptime(transaction_date, "%m/%d/%Y") < time.strptime(
            date_range_start, "%m/%d/%Y"
        ) or time.strptime(transaction_date, "%m/%d/%Y") > time.strptime(
            date_range_start, "%m/%d/%Y"
        ):
            continue

        print(
            transaction_date
            + "\t\t"
            + transaction_time
            + "\t\t"
            + str(transaction["transaction_amount"])
            + "\t\t\t"
            + str(running_balance)
        )
