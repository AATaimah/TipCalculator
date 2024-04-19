print ("Hi, this is the the Tip Calculator. How can I help you?")
# Array of workers
workers = ['Abu Omar','Abu Talal','Abu Mahmoud','Abu Yousef','Abdullah','Abu Yazan','Khatab',"Khader",'Mahmoud','Mostafa','Wael',"Monir",'Mohammed A','Abood','Mohammed F','Sara Eid','Weeam']
pay = []
totalPay = []

register = float(input ('Total amount of tips registered: '))

# Instead of doing the math, this will add up all the paper bills
fives = int(input('Total number of 5s: '))
tens = int(input('Total number of 10s: '))
twenties = int(input('Total number of 20s: '))
fifties = int(input('Total number of 50s: '))
hunnids = int(input('Total number of 100s: '))
totalTips = (fives*5) + (tens*10) + (twenties*20)+ (fifties*50) +(hunnids*100)

print ('The total amount of tips collected is: '+ str(totalTips))

# Setting aside 25% of collected tips to account for taxes
salesTax = round((register*0.25)/5) * 5

# Remainder that goes to employees
newTips = totalTips - (salesTax) 


def tips ():

    # Iterate over the list of employees and user can input their hours for calculation
    for i in range (len(workers)):
        worker = workers[i]

        # Input validation so that all the inputs for 'hours' are (or could be) floats (valid input)
        while True:
            try:
                hours = float(input('Enter the number of hours that '+ worker +' has worked: '))
                if hours < 0 or hours > 100:
                    print('Hours should be between 0 and 100')
                else: 
                    break

            except ValueError:
                print('please enter a valid number of hours')
                

        # How much an employee worked as a fraction of 40
        perHour = round (hours/40 , 2)
        pay.append(perHour)


    totalCuts = sum(pay)
    indie = round((newTips / totalCuts)/5) * 5


    # Iterate over workers list again and print all the employees and their deserved tips        
    for q in range (len(workers)):
        each = round(((pay[q] * indie)/5)) * 5
        totalPay.append(each)
        print(workers[q] + " should get: $" +str(each))

    print ("Sales tax set aside: $" + str(salesTax))

    #These are mentioned after the q is iterated
    finalPay = sum(totalPay)
    remainder = newTips - finalPay
    print ("The remainder should be: $" + str(remainder))
    print ("A full time worker would recieve: $" + str(indie))

tips()
    
