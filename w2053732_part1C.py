# Date: 11/12/2023

#Part C - predict progression outcomes for the use of Staff

#list for each progress
progress=[]
trailer=[]
retriever=[]
excluded=[]

def staff():
     while True:
          try:
               #checking the credit range
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
                    progress.append([passCredit,deferCredit,failCredit])
                    
                    
                    
               elif(passCredit==100 and deferCredit<=20 and failCredit<=20):
                    print("Progression Outcome:Progress(module trailer)")
                    trailer.append([passCredit,deferCredit,failCredit])
                    
                    

               elif(failCredit>=80):
                    print("Progression Outcome:Exclude")
                    excluded.append([passCredit,deferCredit,failCredit])
                    
                    
               else:
                    print("Progression Outcome:Do not progress – module retriever")
                    retriever.append([passCredit,deferCredit,failCredit])
                 


               #asking the staff member has done entering the credits
               while True:
                    done=input("\nWould you like to enter another set of data(yes[y]/quit[q])?:")
                    done=done.lower()
                    if(done=='y'):
                         break
                    elif(done=='q'):
                         print()
                         for i in progress:
                              print("Progress-- ",end="")
                              print(",".join(map(str,i)))
                                    
                         for i in trailer:
                              print("Progress (module trailer)--",end="")
                              print(",".join(map(str,i)))
                              
                         for i in retriever:
                              print("Module retriever--",end="")
                              print(",".join(map(str,i)))
                         
                         for i in excluded:
                              print("Exclude--",end="")
                              print(",".join(map(str,i)))
                                    
                         break
                    
               if(done=="q"):
                    #no of outcomes entered(displayed in histogram)
                    outcomes=len(progress+trailer+retriever+excluded)
                    break
          except ValueError:
               print("Integer required")

     
staff()
              
                    


