import convert
def main_function(sender_email, password, rec_email, text, subject):
    import smtplib
    message = f'Subject:{subject}\n\n{text}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print('login success')
    print("sending, email.")
    server.sendmail(sender_email,rec_email,message)
    print(f"email sent to {rec_email} from {sender_email}")
    

cred_of_user = open("credentials.txt", "r+")
rec_email = input("enter recivers email:- ")
subject = input("enter subject:- ")
text = input("enter text in email:- ")
sender_email = convert.rec_email
password = convert.password
main_function(sender_email,password,rec_email,text,subject)




    