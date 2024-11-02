# Date: 11/12/2023

#Histogram with the list extension

from graphics import *

from w2053732_part1C import progress
from w2053732_part1C import trailer
from w2053732_part1C import retriever
from w2053732_part1C import excluded



def histogram():
     #body of the histogram
     win = GraphWin("histogram", 500, 600) 
     win.setBackground("Mint Cream")
     outcomes=len(progress+trailer+retriever+excluded)


     my_heading = Text(Point(100, 30), 'histogram')

     message = Text(Point(150,50),("Histogram results"))
     message.setStyle("bold")
     message.setTextColor("black")
     message.setSize(20)
     message.draw(win)
     

     #Progress outcome
     rect1 = Rectangle(Point(30,400-len(progress*30)), Point(100,400))
     rect1.setOutline("#a2cd5a")
     rect1.setFill("#a2cd5a")
     rect1.draw(win)

     message1 = Text(Point(64,420),("Progress"))
     message7 = Text(Point(64,375-len(progress*30)),(len(progress)))
     message1.setStyle("bold")
     message1.setTextColor("black")
     message1.setSize(10)
     message1.draw(win)
     message7.draw(win)

     
     #Trailer outcome
     rect2 = Rectangle(Point(130,400-len(trailer*30)), Point(200,400))
     rect2.setOutline("#bcee68")
     rect2.setFill("#bcee68")
     rect2.draw(win)

     message2 = Text(Point(163,420),("Trailer"))
     message8 = Text(Point(163,375-len(trailer*30)),(len(trailer)))
     message2.setStyle("bold")
     message2.setTextColor("black")
     message2.setSize(10)
     message2.draw(win)
     message8.draw(win)

     #Retriever outcome
     rect3 = Rectangle(Point(230,400-len(retriever*30)), Point(300,400))
     rect3.setOutline("#8fbc8f")
     rect3.setFill("#8fbc8f")
     rect3.draw(win)
     
     message3 = Text(Point(264,420),("Retriver"))
     message9 = Text(Point(264,375-len(retriever*30)),(len(retriever)))
     message3.setStyle("bold")
     message3.setTextColor("black")
     message3.setSize(10)
     message3.draw(win)
     message9.draw(win)


     #Excluded outcome
     rect4 = Rectangle(Point(330,400-len(excluded*30)), Point(400,400))
     rect4.setOutline("#eea2ad")
     rect4.setFill("#eea2ad")
     rect4.draw(win)
     
     message4 = Text(Point(364,420),("Excluded"))
     message10 = Text(Point(364,375-len(excluded*30)),(len(excluded)))
     message4.setStyle("bold")
     message4.setTextColor("black")
     message4.setSize(10)
     message4.draw(win)
     message10.draw(win)

     #total number of outcomes
     message5 = Text(Point(120,500),(outcomes))
     message6 = Text(Point(260,500),("outcomes in total"))
     message5.setStyle("bold")
     message6.setStyle("bold")
     message5.setTextColor("black")
     message5.setSize(20)
     message6.setSize(20)
     message5.draw(win)
     message6.draw(win)
     
     
     


     line = Line(Point(0, 400), Point(500, 400))
     line.draw(win)

     win.getMouse()
     win.close()
     
histogram()
