asteriks = "*" * 30
import random
from datetime import datetime
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%B %d, %Y")


#account
acctDB = {}
#main program start
def init():

   
    print("Welcome{}{}-{}\n".format(" to Basobank," , " Today is: " + date,time) +  asteriks)
    print("| 1 | Existing Customer\n| 2 | New Customer\n| 3 | Recover Account Details\n" + asteriks )
 
    UserInp = int(input("\nSelect Option: "))

    if(UserInp == 1):
        
        DemoLogin()
    elif(UserInp == 2):
        
        register()
    elif(UserInp == 3):
        recoverDetails()
    else:
        print("You have selected invalid option")
        init()

"""
    Login Operations
    begins
    """
def DemoLogin():
    allowedUsers = ['101010', '202020']
    allowedPassword = ['1010','2002']
    balanceAmt = 2000.00
    print("Use 101010 and 1010 for Demo User as Existing Customer")
    print(asteriks)
    Acct = input("Enter Account Number: ")
    if(Acct in allowedUsers):
        password = input("Enter Pin: ")
        print(asteriks)
        userId = allowedUsers.index(Acct)

        if(password == allowedPassword[userId]):

            print("Welcome {}{}-{}".format("Demo User, ", "Today is: " + date,time))
            print(asteriks)
            print("You're logged in!")
            print(asteriks)
            print('Select an option')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')
            print(asteriks)

            selectedOption = int(input('Please select an Option: '))
            print(asteriks)
            
        #Withdrawal
            
        if(selectedOption == 1):
            print('Withdrawal Selected')
            print(asteriks)
            print(' 1. savings\n 2. current\n')
            
            selectedOption = int(input('select an option: '))
            
            if(selectedOption == 1):
                print('Savings Account Selected to be Debited')
                print(asteriks)
                withdrawAmnt = float(input("Enter Amount: "))
                if (withdrawAmnt > balanceAmt):
                	print("Insufficient Balance!")
                else:
                	print("Take Your Cash: ")
                	exit()
             
                    
        elif(selectedOption == 2):
            print('Deposit Selected')
            print(asteriks)
            print(' 1. saving\n 2. current\n')

            selectedOption = int(input('select an option'))

            if(selectedOption == 1):
                print('Savings Account Selected to be Credited')
                print(asteriks)
                depositAmt = float(input("Enter amount: "))
                balanceAmt = balanceAmt + depositAmt
                print(balanceAmt)   
            
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            print(' 1. Report an issue\n 2. Exit\n')

            selectedOption = int(input('select an option'))

            if(selectedOption == 1):
                print('you selected %s' % selectedOption)
                ReportanIssue = input("Write issue: ")
                print('Thank you for your message, we will get back to you for.')   

            else:
                print('Invalid Option selected, please try again')



        else:
            print('Password Incorrect, please try again')

    else:

        print('Name not found, please try again')
        init()
        
#Login operations

def login():
	print("********* Login ***********")
	accountNumberFromUser = int(input("What is your account number? \n"))
	Upin = input("What is your pin \n")
	for accountNumber,userDetails in acctDB.items():
	           if (accountNumber == accountNumberFromUser):
	            	   
	            	   if(userDetails[2] == Upin):
	            	   	bankOperation(userDetails)
	    #    print('Invalid account or password')
	    #    login()





def register():
    print(asteriks + "Account Opening Page" + asteriks)

    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    pin = input("create a pin for yourself\n")
    if len(pin) > 4 or len(pin) < 4:
        print("Pin must be 4 digits")
        
        #Back to register
        
        register()
        
    phoneNo = input("Your Mobile Number\n")
    
    

    accountNumber = generateAccountNumber()
    acctDB[accountNumber] = [ first_name, last_name, pin, phoneNo]
    acctDB.update({"balance": 000.0})
    

    print("Your Account Has been created Successfully!")
    print(asteriks)
    print("Your Account Details:")
    print("Account Number:\t %d" % accountNumber)
    print("Full Name:\t " + first_name.title() + " " + last_name.title())
    print("Mobile Number:\t " + phoneNo)
    print("Please note that your mobile number will be use to receive transaction alerts!")
    print(asteriks)
    print("You have N000.00 in your Account")
    
    print("Thank you for choosing us")
    print(asteriks)
    print("\n")
    login()

#-- Recovery Starts --
def recoverDetails():
    print(asteriks + "\nLost Account Details\n" + asteriks)
    print("| 1 | Lost Account Number\n| 2 | Forgot Pin\n| 3 | Change Mobile Number\n" + asteriks)
    UserInp = int(input("\nSelect Option: "))

    if(UserInp == 1):
        print("how would like to recover your it?.Capitalize() ")
        
    elif(UserInp == 2):
        print("Pin recovery Page")
        print("Get your NUBAN number ready")
        
    elif(UserInp == 3):
        checker()
                
        
    else:
        print("You have selected invalid option")
        init()

def checker():
    print("Change Mobile Number Page")
    ninCheck = input("Have you registered for NIN? ")
    if ninCheck.lower() == 'yes':
        
        while True:
            UserInp = input("Enter NIN Number: ")
            print("Your NIN: %s \nThank You, we will get back to you!" %UserInp)
            init()
    else:
        print("Wrong input")
        checker()
# -- Recovery Ends --



#Banking Operations Start
def bankOperation(userDetails):
    print(asteriks)
    print("Log in Successful!")
          
    print(asteriks)
    print("Welcome {} {}-{}".format(userDetails[0].title()," | " + date,time))

    print(asteriks)
    
    print('Banking Option:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Balance')
    print('4. Log out')
    print(asteriks)
    selectedOption = int(input('Please select an Option: '))
    print(asteriks)
    

    if(selectedOption == 1):
        #Withdrawal
        withdrawalOperation()
        bankOperation(userDetails)
        
    elif(selectedOption == 2):
        #Deposit
        depositOperation()
        bankOperation(userDetails)
        
        
    elif(selectedOption == 3):
        
        balanceOperation()
        bankOperation(userDetails)
        
    elif(selectedOption == 4):
        
        #logout call
        
        logout()
    else:
      
        print("Invalid option selected")
        


def balanceOperation():
    #print Account Balance
    
    acctDB.get("balance")
    print("Your balance is N %f \nDeposit Transaction Completed" % acctDB["balance"])
    

def withdrawalOperation():
    #Withdrawal Process
    amt = float(input("Enter Amount: "))
    
    bal = acctDB.get("balance")
    bal = bal - amt
    acctDB["balance"] = bal
    print("Take Your Cash: ")
    print("Withdrawal Transaction completed.")
    
      

def depositOperation():
    #Deposit Process
    print("Deposit Operations")
    acctDB.get("balance")
    bal = acctDB.get("balance")
    amt = float(input("Enter amount: "))
    bal = amt + bal
    acctDB["balance"] = bal
    print("Your balance is N %f \nDeposit Transaction Completed" % acctDB["balance"])
    
    


def generateAccountNumber():

    return random.randrange(1000000009,10000000009)

def logout():
    print("You have successfully logged out!")
    print("Thank you for Banking with us!")
    login()


init()