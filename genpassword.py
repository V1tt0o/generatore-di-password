import random
p = 'needed'
char ='+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
while p == 'needed':
    num = input('quanti caratteri vuoi nella pasword?')
    if num >= '8':
        password =''
        for i in range (int(num)):
            password += random.choice(char)
        print('la tua password è:', password)
        x = input('ti piace la password?')
        if x == 'SI' or x == 'si' or x == 'Si':
            p = 'not needed'
        elif x == 'NO' or x == 'no' or x == 'No':
            p = 'needed'
        else:
            print ('rispondi solo con SI o NO')
    else:
        print ('la password deve essere di almeno 8 caratteri')
