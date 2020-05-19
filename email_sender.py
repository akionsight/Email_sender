import others
import convert
import run_run
if others.tru_fal == 'false':
    open("credentials.txt", 'a')
    print("this is the first time setup, please enter the following details about YOUR email address, you will never be asked this again")
    sender_email = input("enter your email address:- ")
    sender_password = input("enter your password, be careful :- ")
    file = open('credentials.txt', 'a')
    file.write(f'{sender_email}\n')
    file.write(f'{sender_password}\n')
    file.close()
    print("your credentials have been saved and locked, restart this program and start sending emails !! ")
else:
    import run_run
    exec('run_run')


