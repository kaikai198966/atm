import os
import env 
import controllers.fs as fs


def default():
    if not os.path.exists(env.files["users"]):
        print("Users file not found. Creating file with default content...")
        admin_user = (
            env.master_account["username"]
            + "|"
            + env.master_account["password"]
            + "|"
            + env.master_account["status"]
            + "|"
            + env.master_account["created_date"]
            + "\n"
        )
        fs.create(env.files["users"]) # NOTE: may be omitted
        # fs.write will create the file if it doesn't exist
        fs.write(env.files["users"], admin_user)

    if not os.path.exists(env.files["accounts"]):
        print("Accounts file not found. Creating file...")
        fs.create(env.files["accounts"])

    if not os.path.exists(env.files["transaction_details"]):
        print("Transaction Details file not found. Creating file...")
        fs.create(env.files["transaction_details"])

    if not os.path.exists(env.files["transaction_table"]):
        print("Transaction Table file not found. Creating file with default content...")
        transaction_codes = (
            "new|Initial Balance\n"
            + "wdr|Withdrawal\n"
            + "dep|Deposit\n"
            + "chk|Check Balance\n"
            + "rep|Transaction Report\n"
        )
        fs.create(env.files["transaction_table"]) # NOTE: may be omitted
        # fs.write will create the file if it doesn't exist
        fs.write(env.files["transaction_table"], transaction_codes)
