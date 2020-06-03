tarjetaCredito = str(input("Insert the number you'd like to check"))
suma = 0
for i in range(len(tarjetaCredito)//2):
    suma += int(tarjetaCredito[2*i])*2//10 + int(tarjetaCredito[2*i])*2%10 + int(tarjetaCredito[2*i+1])//10 + int(tarjetaCredito[2*i+1])%10 
print('Valid Lunh.') if(suma%10 == 0) else print('Invalid Lunh.')