# this menu will be displayed when the type of the user is admin ("adm")
import re
import controllers.api as api
import utils

def is_user_existing(user_id):
    user = api.get_user(user_id)
    if user:
        print("User already exists. Please try again.\n")
        return True
    return False

def credentials_input_is_valid(email, password):
    password_pattern = (
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,}$"
    )
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


def create_admin_account():
        print("Add Admin Account")

        new_user_id = input("Enter User ID: ")
        password = input("Enter Password: ")

        if not credentials_input_is_valid(new_user_id, password):
            return

        if is_user_existing(new_user_id):
            return

        api.append_user(
            {
                "user_id": new_user_id,
                "password": password,
                "type": "adm",
                "status": "Active",
                "created_date": utils.timestamp(),
            }
        )


def create_depositor_account():
        timestamp = utils.timestamp()

        print("Add Depositor Account")

        account_number = input("Enter Account Number: ")
        account_name = input("Enter Account Name: ")
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")
        initial_deposit = input("Initial Deposit: ")

        initial_deposit = float(initial_deposit)

        if not credentials_input_is_valid(user_id, password):
            return
        
        if is_user_existing(user_id):
            return

        if initial_deposit < 2000:
            print("Initial deposit must be at least 2000.\n")
            return

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