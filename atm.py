import time
import re
import getpass
import api

timestamp = lambda: time.strftime("%Y/%m/%d_%H:%M:%S")

format_date = lambda date: time.strptime(date, "%m/%d/%Y")

while True:
    print(f"Welcome to ABC BANK")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    user = api.get_user(username)

    if not user:
        print("User not found\n")
        continue

    if not password == user["password"]:
        print("Incorrect password\n")
        continue

    print("\n")

    if user["type"] == "adm":
        import ui.admin

        while True:
            prompt = (
                f"Welcome to ABC BANK\n"
                + "A - Add Admin Account\n"
                + "D - Add Depositor Account\n"
                + "Q - Quit\n"
            )

            print(prompt)
            option = input("Select an option: ")
            option = option.strip().lower()
            print("\n")

            def is_user_existing(user_id):
                user = api.get_user(user_id)
                if user:
                    print("User already exists. Please try again.\n")
                    return True
                return False

            def credentials_input_is_valid(email, password):
                password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,}$"
                email_pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
                if not re.match(email_pattern, email):
                    print("Enter a valid email for User ID.\n")
                    return False
                if not re.match(password_pattern, password):
                    print(
                        "Invalid password. Please try again.\n"
                        + "Password should be at least 8 characters long, "
                        + "with at least 1 uppercase letter, "
                        + "1 lowercase letter, 1 number, and 1 special character.\n"
                    )
                    return False
                return True

            match option:
                case "a":
                    while True:
                        print("Add Admin Account")

                        new_user_id = input("Enter User ID: ")
                        password = getpass.getpass("Enter Password: ")

                        # TODO: CONSULT KAI for repeat password

                        if not credentials_input_is_valid(new_user_id, password):
                            continue

                        if is_user_existing(new_user_id):
                            continue

                        api.append_user(
                            {
                                "user_id": new_user_id,
                                "password": password,
                                "type": "adm",
                                "status": "Active",
                                "created_date": timestamp(),
                            }
                        )

                        loop = input("Enter another account? (Y/N): ")
                        match loop.strip().lower():
                            case "y":
                                continue
                            case "n":
                                break
                            case _:
                                print("Invalid input.\n")
                case "d":
                    while True:
                        print("Add Admin Account")

                        timestamp = timestamp()

                        print("Add Depositor Account")

                        account_number = input("Enter Account Number: ")
                        account_name = input("Enter Account Name: ")
                        user_id = input("Enter User ID: ")
                        password = getpass.getpass("Enter Password: ")
                        initial_deposit = input("Initial Deposit: ")

                        initial_deposit = float(initial_deposit)

                        if not credentials_input_is_valid(user_id, password):
                            continue

                        if is_user_existing(user_id):
                            continue

                        if initial_deposit < 2000:
                            print("Initial deposit must be at least 2000.\n")
                            continue

                        api.append_user(
                            {
                                "user_id": user_id,
                                "password": password,
                                "type": "usr",
                                "status": "Active",
                                "created_date": timestamp,
                            }
                        )
                        api.append_account(
                            {
                                "user_id": user_id,
                                "account_number": account_number,
                                "account_name": account_name,
                                "outstanding_balance": initial_deposit,
                                "last_transaction_date": timestamp,
                                "last_transaction_details": "new",
                            }
                        )
                        api.append_transaction_details(
                            {
                                "transaction_date": timestamp,
                                "account_number": account_number,
                                "transaction_code": "new",
                                "amount": initial_deposit,
                            }
                        )
                        loop = input("Enter another account? (Y/N): ")
                        match loop.strip().lower():
                            case "y":
                                continue
                            case "n":
                                break
                            case _:
                                print("Invalid input.\n")
                case "q":
                    exit(0)
                case _:
                    print("Invalid input.\n")
                    continue

    if user["type"] == "usr":
        import ui.user

        while True:
            prompt = (
                f"Welcome to ABC BANK\n"
                + "B - Check for balance\n"
                + "D - Make deposit\n"
                + "W - Make withdrawal\n"
                + "R - Transaction Report\n"
                + "Q - Quit\n"
            )

            print(prompt)
            option = input("Select an option: ")
            option = option.strip().lower()
            print("\n")

            match option:
                case "b":
                    user = api.get_account(user_id=user_id)

                    user_id = user["user_id"]
                    balance = user["outstanding_balance"]

                    api.append_transaction_details(
                        {
                            "transaction_date": timestamp(),
                            "account_number": user["account_number"],
                            "transaction_code": "chk",
                        }
                    )

                    prompt = f"Hi, {user_id}! Your current balance is {balance}."
                    print(prompt)
                case "d":
                    amount = input("Enter amount to Deposit: ")
                    amount = float(amount)
                    if amount < 0:
                        print("Deposit amount must be greater than zero")
                        continue  # TODO: CONSULT KAI IF the error should pushed through to be logged
                    elif amount > 500000:
                        print("Deposit amount must not be greater than 500,000")
                        continue  # TODO: CONSULT KAI IF the error should pushed through to be logged

                    account = api.get_account(user_id)
                    account["outstanding_balance"] += amount
                    api.append_account(account)
                    api.append_transaction_details(
                        {
                            "transaction_date": timestamp(),
                            "account_number": account["account_number"],
                            "transaction_code": "dep",
                            "transaction_amount": amount,
                        }
                    )

                    prompt = f"""Deposit Transaction successfully completed.
                        Your new Outstanding balance is {account["outstanding_balance"]}.
                        """
                    print(prompt)
                case "w":
                    amount = input("Enter amount to Withdraw: ")
                    amount = float(amount)
                    if amount < 0:
                        print("Withdrawal Amount must be greater than zero")

                    account = api.get_account(user_id)

                    if account["outstanding_balance"] < amount:
                        print(
                            f"Amount must not be greater than {account['outstanding_balance']}"
                        )

                    account["outstanding_balance"] -= amount

                    api.append_account(account)
                    api.append_transaction_details(
                        {
                            "transaction_date": timestamp(),
                            "account_number": account["account_number"],
                            "transaction_code": "wdr",
                            "transaction_amount": amount,
                        }
                    )

                    prompt = f"""Withdrawal Transaction is successfully completed.
                        Your new Outstanding balance is {account["outstanding_balance"]}.
                        """
                    print(prompt)
                case "r":
                    print("Transaction Report")

                    date_range_start = input("Enter Start Date (mm/dd/yyyy): ")
                    date_range_end = input("Enter End Date (mm/dd/yyyy): ")

                    account = api.get_account(user_id)
                    transactions = api.get_transactions(account["account_number"])

                    prompt = (
                        f"List of transactions for Account Number {account['account_number']} "
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

                        if format_date(transaction_date) < format_date(
                            date_range_end
                        ) or format_date(transaction_date) > format_date(
                            date_range_start
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

                case "q":
                    exit(0)

            loop = input("Want to transact another? (Y/N): ")
            loop = loop.strip().lower()
            match loop:
                case "y":
                    continue
                case "n":
                    break
                case _:
                    print("Invalid input.\n")
