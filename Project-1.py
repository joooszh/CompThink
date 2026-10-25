# DATABASE
in_lobby = False
list_login = ['1. Create New Account', '0. Exit']
list_topup = [1, 5, 10, 25, 50, 100]
account = []
password = []
balance = []
display = []
line1 = '-' * 50
line2 = '=' * 50
confirm = 'Input (y) to confirm or (n) to cancel'
makesure = 'Are you sure? (y/n)'
press_enter = 'Press Enter to continue'
while True:
    ### LOG IN INTERFACE
    print(line2)
    print('WELCOME TO UPSCIENCE!'.center(50))
    print(line2)
    for listlog in list_login:
        print(listlog)
    print('Input your choice by list number :')
    while True:
        login_menu = input()
        if not login_menu.isdigit():
            print('Input your choice by list number :')
            continue
        login_menu = int(login_menu)
        if login_menu not in range (len(list_login)):
            print('Input a valid choice number :')
            continue
        break
    ### EXIT FROM LOG IN
    if login_menu == 0:
        print(line1)
        print('EXIT UPSCIENCE'.center(50))
        print(line1)
        print('Close UpScience? (y/n)')
        exit_confirm = input()
        while exit_confirm.lower() not in ['y', 'n']:
            print(confirm)
            exit_confirm = input()
        if exit_confirm.lower() == 'y':
            break
    ### CREATE ACCOUNT
    elif login_menu == 1:
        while True:
            print(line1)
            print('CREATE NEW ACCOUNT'.center(50))
            print(line1)
            print('Create your username :')
            while True:
                acc = input()
                if acc == '':
                    print('Username must be at least 1 character!')
                    print('Input a valid username :')
                    continue
                if acc in account:
                    print('Username is taken!')
                    print('Input another username :')
                    continue
                break
            print('Create your password :')
            pw = input()
            while len(pw) < 8:
                print('Password must be at least 8 characters!')
                print('Input a valid password :')
                pw = input()
            print(makesure)
            user_confirm = input()
            while user_confirm.lower() not in ['y', 'n']:
                print('Input (y) to confirm or (n) to cancel :')
                user_confirm = input()
            if user_confirm.lower() == 'y':
                print('Account created!')
                input(press_enter)
                if '2. Log in' not in list_login:
                    list_login.insert(1, '2. Log in')
                account.append(acc)
                password.append(pw)
                balance.append(0)
                display.append(acc)
            break
    ### ACCOUNT LOGIN
    elif login_menu == 2:
        while True:
            print(line1)
            print('ACCOUNT LOGIN'.center(50))
            print(line1)
            for listacc in range (len(account)):
                print(f'{listacc + 1}. {display[listacc]} -- @{account[listacc]}')
            print('Choose your account by list number :')
            while True:
                acc_chosen = input()
                if not acc_chosen.isdigit():
                    print('Input your choice by list number :')
                    continue
                acc_chosen = int(acc_chosen)
                if acc_chosen < 1 or acc_chosen > len(account):
                    print('Input a valid choice number :')
                    continue
                break
            acc_chosen -= 1
            print(f'Log in to @{account[acc_chosen]}? (y/n)')
            login_confirm = input()
            while login_confirm.lower() not in ['y', 'n']:
                print('Input (y) to confirm or (n) to cancel :')
                login_confirm = input()
            if login_confirm.lower() == 'y':
                enterpw_attempt = 0
                while True:
                    print('Input your password :')
                    pw_chosen = input()
                    if pw_chosen != password[acc_chosen]:
                        print(f'Incorrect password! ({4 - enterpw_attempt} attempt{"s" if enterpw_attempt != 3 else ""} left)')
                        enterpw_attempt += 1
                        if enterpw_attempt == 5:
                            break
                    else:
                        break
                if pw_chosen != password[acc_chosen]:
                    print(line1)
                    print('Too many failed attempts, please try again later!')
                    print(line1)
                    input(press_enter)
                    continue
                in_lobby = True
                print('Login successful!')
                input(press_enter)
                break
            else:
                break
    ### MAIN MENU
    while in_lobby:
        print(line2)
        print('UPSCIENCE'.center(50))
        print(line2)
        print('1. Check Profile')
        print('2. Donate to Streamer')
        print('3. Top Up Balance')
        print('4. Terms and Conditions')
        print('0. Back to Login')
        print('Input your choice by list number :')
        while True:
            lobby_menu = input()
            if not lobby_menu.isdigit():
                print('Input by list number :')
                continue
            lobby_menu = int(lobby_menu)
            if lobby_menu < 0 or lobby_menu > 4:
                print('Input a valid choice number :')
                continue
            break
        ### BACK TO LOGIN
        if lobby_menu == 0:
            print(line1)
            print('BACK TO LOGIN'.center(50))
            print(line1)
            print('Return to the login screen? (y/n)')
            exit_confirm = input()
            while exit_confirm.lower() not in ['y', 'n']:
                print(confirm)
                exit_confirm = input()
            if exit_confirm.lower() == 'y':
                in_lobby = False
                break
        ### CHECK PROFILE
        elif lobby_menu == 1:
            while True:
                print(line1)
                print('YOUR PROFILE'.center(50))
                print(line1)
                print(f'Username : @{account[acc_chosen]}')
                print(f'Display Name : {display[acc_chosen]}')
                print(f'Password : {"*" * len(password[acc_chosen])}')
                print(f'Account Balance : ${balance[acc_chosen]}')
                print(line1)
                print('Input (S) to open settings or (Q) to exit profile :')
                profile_menu = input()
                while profile_menu.lower() not in ['s', 'q']:
                    print('Input a valid option :')
                    profile_menu = input()
                ### PROFILE SETTINGS
                if profile_menu.lower() == 's':
                    while True:
                        print(line1)
                        print('SETTINGS'.center(50))
                        print(line1)
                        print('1. Change Username')
                        print('2. Change Display Name')
                        print('3. Change Password')
                        print('0. Close Settings')
                        print('Input your choice by list number :')
                        while True:
                            setting_menu = input()
                            if not setting_menu.isdigit():
                                print('Input by list number :')
                                continue
                            setting_menu = int(setting_menu)
                            if setting_menu < 0 or setting_menu > 3:
                                print('Input a valid choice number :')
                                continue
                            break
                        ### BACK TO MAIN PROFILE
                        if setting_menu == 0:
                            print(line1)
                            print('Back to profile? (y/n)')
                            closesetting_confirm = input()
                            while closesetting_confirm.lower() not in ['y', 'n']:
                                print(confirm)
                                closesetting_confirm = input()
                            if closesetting_confirm.lower() == 'y':
                                break
                        ### CHANGE USERNAME
                        elif setting_menu == 1:
                            print(line1)
                            print(f'Current username : @{account[acc_chosen]}')
                            print('Input new username :')
                            while True:
                                change_acc = input()
                                if change_acc == '':
                                    print('Username must be at least 1 character!')
                                    print('Input a valid username :')
                                    continue
                                if change_acc in account:
                                    print('Username is taken!')
                                    print('Input another username :')
                                    continue
                                break
                            print(makesure)
                            changeacc_confirm = input()
                            while changeacc_confirm.lower() not in ['y', 'n']:
                                print('Input (y) to confirm or (n) to cancel :')
                                changeacc_confirm = input()
                            if changeacc_confirm.lower() == 'y':
                                account[acc_chosen] = change_acc
                                print(f'Username changed to @{change_acc}!')
                                input(press_enter)
                        ### CHANGE DISPLAY NAME
                        elif setting_menu == 2:
                            print(line1)
                            print(f'Current display name : {display[acc_chosen]}')
                            print('Input new display name :')
                            change_display = input()
                            while change_display == '':
                                print('Display name must be at least 1 character!')
                                print('Input a valid display name :')
                                change_display = input()
                            print(makesure)
                            changedisplay_confirm = input()
                            while changedisplay_confirm.lower() not in ['y', 'n']:
                                print('Input (y) to confirm or (n) to cancel :')
                                changedisplay_confirm = input()
                            if changedisplay_confirm.lower() == 'y':
                                display[acc_chosen] = change_display
                                print(f'Display name changed to {change_display}!')
                                input(press_enter)
                        ### CHANGE PASSWORD
                        elif setting_menu == 3:
                            checkpw_attempt = 0
                            print(line1)
                            print(f'Current password : {"*" * len(password[acc_chosen])}')
                            while True:
                                print('Input your current password :')
                                check_pw = input()
                                if check_pw != password[acc_chosen]:
                                    print(f'Incorrect password! ({4 - checkpw_attempt} attempt{"s" if checkpw_attempt != 3 else ""} left)')
                                    checkpw_attempt += 1
                                    if checkpw_attempt == 5:
                                        break
                                else:
                                    break
                            if checkpw_attempt == 5:
                                print(line1)
                                print('Too many failed attempts, please try again later!')
                                print(line1)
                                input(press_enter)
                                continue
                            print('Input new password :')
                            while True:
                                change_password = input()
                                if len(change_password) < 8:
                                    print('Password must be at least 8 characters!')
                                    print('Input a valid password :')
                                    continue
                                if change_password == password[acc_chosen]:
                                    print("New password can't be the same as the old one!")
                                    print('Input a valid password :')
                                    continue
                                break
                            print(makesure)
                            changepassword_confirm = input()
                            while changepassword_confirm.lower() not in ['y', 'n']:
                                print('Input (y) to confirm or (n) to cancel :')
                                changepassword_confirm = input()
                            if changepassword_confirm.lower() == 'y':
                                password[acc_chosen] = change_password
                                print('Password changed!')
                                print(line1)
                                input(press_enter)
                else:
                    break
        ### DONATE TO STREAMER
        elif lobby_menu == 2:
            while True:
                print(line1)
                print('DONATE TO STREAMER'.center(50))
                print(line1)
                print('You can donate to the streamer simply by entering their username!')
                print('You can also send extra content based on these milestones :')
                print('$1  --  You can add a message')
                print('$2  --  You can attach a song')
                print('$5  --  You can attach a video (max 1 min long)')
                print('Input (D) to continue donating or (Q) to exit :')
                donate_menu = input()
                while donate_menu.lower() not in ['d', 'q']:
                    print('Input a valid option :')
                    donate_menu = input()
                if donate_menu.lower() == 'd':
                    print(line1)
                    print(f'Your current balance : ${balance[acc_chosen]}')
                    if balance[acc_chosen] == 0:
                        print('You have no money to donate...')
                        input(press_enter)
                        continue
                    print("Please input the streamer's username :")
                    streamer_usn = input()
                    while streamer_usn == '':
                        print('Input a valid username :')
                        streamer_usn = input()
                    while True:
                        print('Input the amount of your donation :')
                        donate_amount = input()
                        if not donate_amount.isdigit():
                            print('Amount must be a whole number!')
                            continue
                        donate_amount = int(donate_amount)
                        if donate_amount <= 0:
                            print('Bruh...')
                            continue
                        break
                    if donate_amount > balance[acc_chosen]:
                        print('Insufficient balance!')
                        continue
                    else:
                        donate_properties = []
                        print("Please input a message you want to send (or leave it blank if you don't) :")
                        donate_msg = input()
                        if donate_msg == '':
                            donate_msg = '-'
                        if donate_amount >= 2:
                            print("Please input the link of the song you want to send (or leave it blank if you don't) :")
                            donate_song = input()
                            if donate_song == '':
                                donate_song = '-'
                        if donate_amount >= 5:
                            print("Please input the link of the video you want to send (or leave it blank if you don't) :")
                            donate_vid = input()
                            if donate_vid == '':
                                donate_vid = '-'
                        print("Here is a preview of your donation :")
                        print(f'Amount of donation : ${donate_amount}')
                        print(f'Donated to : {streamer_usn}')
                        if donate_amount >= 5:
                            print(f'Video attached : {donate_vid}')
                            donate_properties.append(donate_vid)
                        if donate_amount >= 2:
                            print(f'Song attached : {donate_song}')
                            donate_properties.append(donate_song)
                        print(f'Message for streamer : {donate_msg}')
                        donate_properties.append(donate_msg)
                        print('Send your donation? (y/n)')
                        donate_confirm = input()
                        while donate_confirm.lower() not in ['y', 'n']:
                            print('Input (y) to confirm or (n) to cancel :')
                            donate_confirm = input()
                        if donate_confirm.lower() == 'y':
                            balance[acc_chosen] -= donate_amount
                            print(line1)
                            print('Donation sent!')
                            print(f'Your current balance : ${balance[acc_chosen]}')
                            print(line1)
                            print('Here is an overview for your donation :')
                            print(f'{display[acc_chosen]} donated ${donate_amount} to {streamer_usn}!')
                            for prop in donate_properties:
                                if prop != '-':
                                    print(prop)
                            print(line1)
                            input(press_enter)
                            break
                else:
                    break
        ### TOP UP BALANCE
        elif lobby_menu == 3:
            while True:
                print(line1)
                print('TOP UP ACCOUNT BALANCE'.center(50))
                print(line1)
                print(f'Your current balance : ${balance[acc_chosen]}')
                print('Input (T) for top-up or (Q) to exit top up :')
                topup_menu = input()
                while topup_menu.lower() not in ['t', 'q']:
                    print('Please input (T) for top-up or (Q) to exit top up :')
                    topup_menu = input()
                if topup_menu.lower() == 't':
                    print(line1)
                    print('Price List :')
                    for listtop in range(len(list_topup)):
                        print(f'{listtop + 1}. ${list_topup[listtop]}')
                    print('Input your choice by list number :')
                    while True:
                        topup_choice = input()
                        if not topup_choice.isdigit():
                            print('Please choose by list number :')
                            continue
                        topup_choice = int(topup_choice)
                        if topup_choice < 1 or topup_choice > len(list_topup):
                            print('Input a valid choice number :')
                            continue
                        break
                    print(makesure)
                    topup_confirm = input()
                    while topup_confirm.lower() not in ['y', 'n']:
                        print('Input (y) to confirm or (n) to cancel :')
                        topup_confirm = input()
                    if topup_confirm.lower() == 'y':
                        print(f'Top up ${list_topup[topup_choice - 1]} succeeded!')
                        balance[acc_chosen] += list_topup[topup_choice - 1]
                        print(f'Your current balance : ${balance[acc_chosen]}')
                        input(press_enter)
                else:
                    break
        ### TnC
        elif lobby_menu == 4:
            print(line1)
            print('TERMS AND CONDITIONS'.center(50))
            print(line1)
            print('1. Users must be at least 18 years old, or have\n'
                  'permission from a parent or legal guardian. Users\n'
                  'must register with accurate personal data, which\n'
                  'is used only for verification and for communication\n'
                  'with the UPSCIENCE team, law enforcement, or other\n'
                  'parties the User has approved.')
            print()
            print('2. Users are fully responsible for all content they\n'
                  'display or publish on UPSCIENCE, and must ensure\n'
                  'it does not violate applicable law. Users agree to\n'
                  'hold UPSCIENCE harmless from any claims or lawsuits,\n'
                  'including those from government bodies or police,\n'
                  'arising from their content or activity.')
            print()
            print('3. Funds paid as tips, donations, or access to\n'
                  'rewards are non-refundable, unless otherwise stated\n'
                  'by UPSCIENCE or required by law.')
            print()
            print('4. UPSCIENCE may suspend or delete an account\n'
                  'and/or earnings if a user violates these Terms or\n'
                  'engages in suspicious activity, such as unusual fund\n'
                  'flows or abnormal account access. Actions taken will\n'
                  'be proportionate to the violation, ranging from a\n'
                  'warning to temporary blocking, permanent termination,\n'
                  'or legal action.')
            print()
            print('5. Users may not copy, reproduce, sell, resell, or\n'
                  'otherwise exploit any part of UPSCIENCE without\n'
                  'written permission. Each party to a transaction is\n'
                  'responsible for their own tax obligations, including\n'
                  'assessing, reporting, and paying taxes under applicable\n'
                  'law in the respective country.')
            print()
            while True:
                print('Input (Q) to go back to main menu :')
                reg_menu = input()
                if reg_menu.lower() == 'q':
                    break
                else:
                    print('Invalid input!')