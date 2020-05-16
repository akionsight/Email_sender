import os.path
tru_fal = os.path.isfile('credentials.txt')
if tru_fal == True:
    tru_fal = 'true'
elif tru_fal == False:
    tru_fal = 'false'