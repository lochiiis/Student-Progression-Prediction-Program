# Date: 11/12/2023

#Part 1-A predict their progression outcome of individual student
#part 1-B Validation-Check type,range,total for pass,defer,fail inputs entered




def student():
     while True:
          try:
               
               #validating pass credit
               passCredit=int(input("Please enter your credits at pass:"))
               if(passCredit>120 or passCredit<0):
                    print("Out of range")
                    continue
               if(passCredit%20!=0):
                    print("Out of range")
                    continue

               #validating defer credit
               deferCredit=int(input("Please enter your credits at defer:"))
               if(deferCredit>120 or deferCredit<0):
                    print("Out of range")
                    continue
               if(deferCredit%20!=0):
                    print("Out of range")
                    continue
                    
               #validating fail credit
               failCredit=int(input("Please enter your credits at fail:"))
               if(failCredit>120 or failCredit<0):
                    print("Out of range")
                    continue
               if(failCredit%20!=0):
                    print("Out of range")
                    continue

               #checking if the total is eqaul to 120
               totCredit=passCredit+deferCredit+failCredit
               if(totCredit!=120):
                    print("Total incorrect")
                    continue
               
          
               #Generating progression outcomes using relevant credit scores
               elif(passCredit==120 and deferCredit==0 and failCredit==0):
                    print("Progression Outcome:Progress")
               elif(passCredit==100 and deferCredit<=20 and failCredit<=20):
                    print("Progression Outcome:Progress(module trailer)")
               elif(failCredit>=80):
                    print("Progression Outcome:Exclude")     
               else:
                    print("Progression Outcome:Do not progress – module retriever")
               break


          except ValueError:
               print("Integer required")


student()

















