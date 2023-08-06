#To automatically generate an ATM withdrawal SMS in Python
#Withdrawal amount is given as input

Withdrawal_Amount = int(input()) #Withdrawal amount
Name = 'Sandeep '
Account_Number = ' ******123 '
Avaiable_Balance = '123450' #your Avaiable Balance
ATM_Branch = ' CBE_ATM '
import pytz
import datetime
IST = pytz.timezone("Asia/Kolkata")
ctime = datetime.datetime.now(IST)
After_Debit = int(Avaiable_Balance) - Withdrawal_Amount 
print('Dear '+Name+'\nYour Account Number ending with **123 has been debited with INR '+str(Withdrawal_Amount)+
      ' for a withdrawal in'+ATM_Branch+'on '+str(ctime)+ '\nYour available balance is INR '+str(After_Debit)+
      '\nThank you for banking. Have a great day.')
