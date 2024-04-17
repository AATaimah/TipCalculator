print ("Hi, this is the the Tip Calculator. How can I help you?")
workers = ['Abu Omar','Abu Talal','Abu Mahmoud','Abu Yousef','Abdullah','Abu Yazan','Khatab',"Khader",'Mahmoud','Mostafa','Wael',"Monir",'Mohammed A','Abood','Mohammed F','Sara Eid','Weeam']
pay = []
totalPay = []

register = float(input ('Total amount of tips registered: '))

fives = int(input('Total number of 5s: '))
tens = int(input('Total number of 10s: '))
twenties = int(input('Total number of 20s: '))
fifties = int(input('Total number of 50s: '))
hunnids = int(input('Total number of 100s: '))
totalTips = (fives*5) + (tens*10) + (twenties*20)+ (fifties*50) +(hunnids*100)

print ('The total amount of tips collected is: '+ str(totalTips))

bigBoss = round((register*0.25)/5) * 5
newTips = totalTips - (bigBoss) 


def tips ():


    for i in range (len(workers)):
        worker = workers[i]
        hours = float(input('Enter the number of hours that '+ worker +' has worked: '))


        if hours < 0:
            return ('Hours invalid')

        else:
            pp = round (hours/40 , 2)
            pay.append(pp)


        totalCuts = sum(pay)
        indie = round((newTips / totalCuts)/5) * 5
        finalPay = sum(totalPay)
        remainder = newTips - finalPay


            
    for q in range (len(workers)):
        each = round(((pay[q] * indie)/5)) * 5
        totalPay.append (each)
        print(workers[q] + " should get: $" +str(totalPay [q]))

    print ("Sales tax set aside: $" + str(bigBoss))
    finalPay = sum(totalPay)
    remainder = newTips - finalPay
    print ("The remainder should be: $" + str(remainder))
    print ("A full time worker would recieve: $" + str(indie))

tips()
    
