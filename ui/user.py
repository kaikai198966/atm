# this menu will be displayed when the type of the user is admin ("adm")
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


def make_deposit(user_id, amount=0):
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


def make_withdrawal(user_id, amount=0):
    amount = input("Enter amount to Withdraw: ")
    amount = int(amount)
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
    transaction = api.get_transactions(account["account_number"])

    prompt = (
        f"List of transactions for Account Number {account['account_number']}"
        + f"from {date_range_start} to {date_range_end} are as follows:\n"
    )
    print(prompt)

    prompt_header = (
        "Transaction Date\t\t"
        + "Transaction Time\t\t"
        + "Transaction Amount\t\t"
        + "Running Balance\n"
    )
    print(prompt_header, transaction)
