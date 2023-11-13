import os
import controllers.fs as fs

files = {
    "users": "./atm-files/users.txt",
    "accounts": "./atm-files/accounts.txt",
    "transaction_details": "./atm-files/tran_details.txt",
    "transaction_table": "./atm-files/tran_table.txt",
}

transaction_detail = """11/01/2023_10:29:02|11111|new|5000
11/02/2023_12:31:45|22222|new|10000
11/02/2023_14:21:53|11111|chk|
11/02/2023_11:12:26|33333|new|8000
11/02/2023_08:43:09|11111|dep|6000
11/03/2023_11:25:57|22222|dep|15000
11/03 2023_14:16:43|33333|dep|7500
11/04/2023_13:41:49|11111|гер|
11/05/2023_17:02:14|22222|wdr|11000
11/05/2023_18:15:32|11111|wdr|4000
11/07/2023_09:36:17|33333|wdr|6500
11/07/2023_18:25:47|11111|dep|2000"""

users = """maestro@gmail.com|Abc1234$|usr|A|11/01/2023_10:29:02
andoy@gmail.com|Abc1234$|usr|A|11/01/2023_12:31:45
palaboy@gmail.com|Abc1234$|usr|A|11/01/2023_11:12:26"""

accounts = """maestro@gmail.com|11111|Maestro|9000|11/07/2023_18:25:47|dep
andoy@gmail.com|22222|Andoy|14000|11/05/2023_17:02:14|wdr
palaboy@gmail.com|33333|Andoy|10000|11/10/2023_18:47:47|rep"""

transaction_table = """new|Initial Balance
wdr|Withdrawal
dep|Deposit
chk|Check Balance
rep|Transaction Report"""


if not os.path.exists(files["users"]):
    print("Users file not found. Creating file with default content...")
    admin_user = (
        "python@gmail.com|admin|adm|A|10/31/2023_08:36:09\n"
        

    )
    fs.create(files["users"])  # NOTE: may be omitted
    # fs.write will create the file if it doesn't exist
    fs.write(files["users"], admin_user)
elif os.path.exists(files["users"]):
    fs.append(files["users"], users)

if not os.path.exists(files["accounts"]):
    print("Accounts file not found. Creating file...")
    fs.create(files["accounts"])
elif os.path.exists(files["accounts"]):
    fs.append(files["accounts"], accounts)

if not os.path.exists(files["transaction_details"]):
    print("Transaction Details file not found. Creating file...")
    fs.create(files["transaction_details"])
elif os.path.exists(files["transaction_details"]):
    fs.append(files["transaction_details"], transaction_detail)

if not os.path.exists(files["transaction_table"]):
    print("Transaction Table file not found. Creating file with default content...")
    transaction_codes = (
        "new|Initial Balance\n"
        + "wdr|Withdrawal\n"
        + "dep|Deposit\n"
        + "chk|Check Balance\n"
        + "rep|Transaction Report\n"
    )
    fs.create(files["transaction_table"])  # NOTE: may be omitted
    # fs.write will create the file if it doesn't exist
    fs.write(files["transaction_table"], transaction_codes)
elif os.path.exists(files["transaction_table"]):
    fs.append(files["transaction_table"], transaction_table)