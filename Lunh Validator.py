number = str(input("Insert the number you'd like to check: "))
suma = 0
for i in range(len(number)//2):
    suma += int(number[2*i])*2//10 + int(number[2*i])*2%10 + int(number[2*i+1])//10 + int(number[2*i+1])%10 
print('Valid Lunh.') if(suma%10 == 0) else print('Invalid Lunh.')
