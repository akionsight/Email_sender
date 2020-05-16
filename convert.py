file = open('credentials.txt', 'r+')

rec_email = ""   
for ele in file.readlines(1):  
    rec_email += ele
    print(f"email is being sent from {rec_email}")    


password = "" 
for ele in file.readlines(2):  
    password += ele


