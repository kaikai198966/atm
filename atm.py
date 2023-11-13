import getpass
import controllers.api
import initializers.check_files
import env
import utils  # may be omitted, also omit line 9

initializers.check_files.default()  # check if files exist, create files with default content if not

utils.clear_console() # NOTE: may be omitted

while True:
    print(f"Welcome to {env.bank_name}")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    user = controllers.api.get_user(username)

    if password is not user[password]:
        print("Incorrect password\n")
        continue
    if not user:
        print("User not found\n")
        continue
    if user["type"] is "adm":
        import ui.admin

        while True:
            prompt = (
                f"Welcome to {env.bank_name}\n"
                + "A - Add Admin Account\n"
                + "D - Add Depositor Account\n"
                + "Q - Quit\n"
            )

            print(prompt)
            option = input("Select an option: ")
            option = option.strip().lower()
            print("\n")

            match option:
                case "a":
                    while True:
                        ui.admin.create_admin_account()
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
                        ui.admin.create_depositor_account()
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
                    print("Invalid input.")
                    continue

    if user["type"] is "usr":
        import ui.user

        while True:
            prompt = (
                f"Welcome to {env.bank_name}\n"
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
                    ui.user.check_for_balance(user_id=username, password=password)
                case "d":
                    ui.user.make_deposit(user_id=username, password=password)
                case "w":
                    ui.user.make_withdrawal(user_id=username, password=password)
                case "r":
                    ui.user.report_transaction(user_id=username)
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
                    print("Invalid input.")
