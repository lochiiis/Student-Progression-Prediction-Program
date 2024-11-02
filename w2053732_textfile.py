# Date: 11/12/2023

#text file

def text():
     #writing the progression outcomes in the text file
     file=open("outcomes.txt","w")

     from w2053732_part1C import progress
     from w2053732_part1C import trailer
     from w2053732_part1C import retriever
     from w2053732_part1C import excluded

     for a in progress:
          file.write("Progress-- ")
          #converts each value in the nested list to string and join by commas
          file.write(",".join(map(str,a)))  
          file.write("\n")

     for b in trailer:
          file.write("Progress (module trailer)-- ")
          file.write(",".join(map(str,b)))
          file.write("\n")

     for c in retriever:
          file.write("Module retriever-- ")
          file.write(",".join(map(str,c)))
          file.write("\n")

     for d in excluded:
          file.write("Exclude-- ")
          file.write(",".join(map(str,d)))
          file.write("\n")


     file.close()

     #Accessing the stored data from the file and printing out

     storedData=open("outcomes.txt","r")
     print("-"*65)
     print("\n\nBelow shows the progression outcomes read from the text file\n")
     for line in storedData:
          print(line,end="")

     storedData.close()

text()

