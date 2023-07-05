import turtle
import threading

aliveCells = []
birthCells = set()
recentBirth = []
deadCells = set()
cells = set()
    
class gameoflife:

    global cells
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def alive(self):
        turtle.goto(self.x*15,self.y*15)
        turtle.dot(12)
        cells.add(self)
        aliveCells.append([self.x,self.y])
        
    def checkNeighbour(self):
        
        counter = 0
        if [self.x,self.y - 1] in aliveCells:
            counter += 1
        if [self.x,self.y + 1] in aliveCells:
            counter += 1
        if [self.x - 1,self.y] in aliveCells:
            counter += 1
        if [self.x + 1,self.y] in aliveCells:
            counter += 1
        if [self.x - 1,self.y - 1] in aliveCells:
            counter += 1
        if [self.x - 1,self.y + 1] in aliveCells:
            counter += 1
        if [self.x + 1,self.y - 1] in aliveCells:
            counter += 1
        if [self.x + 1,self.y + 1] in aliveCells:
            counter += 1

        return counter

    def cellVerdict(self):
        if self.checkNeighbour() > 3:
            deadCells.add(self)
        elif self.checkNeighbour() < 2:
            deadCells.add(self)
        elif self.checkNeighbour() in [2,3]:
            pass #print("(",self.x,",",self.y,") Stays alive to next generation")

    def dead(self):
        #print("(",self.x,",",self.y,") is dead")
        turtle.goto(self.x*15,self.y*15)
        turtle.dot(12,"lightgrey")
        aliveCells.remove([self.x,self.y])
        cells.remove(self)
        

    def giveBirth(self):
        if [self.x,self.y] not in recentBirth:
            if self.checkNeighbour() == 3:
                #print("(",self.x,",",self.y,") is born")
                birthCells.add(self)
                recentBirth.append([self.x,self.y])
            
    def birth(self):
        childCell = gameoflife(self.x,self.y - 1)
        childCell.giveBirth()
        childCell = gameoflife(self.x,self.y + 1)
        childCell.giveBirth()
        childCell = gameoflife(self.x - 1,self.y)
        childCell.giveBirth()
        childCell = gameoflife(self.x + 1,self.y)
        childCell.giveBirth()
        childCell = gameoflife(self.x - 1,self.y - 1)
        childCell.giveBirth()
        childCell = gameoflife(self.x - 1,self.y + 1)
        childCell.giveBirth()
        childCell = gameoflife(self.x + 1,self.y - 1)
        childCell.giveBirth()
        childCell = gameoflife(self.x + 1,self.y + 1)
        childCell.giveBirth()

def grid(x,y):

    turtle.speed(5)
    turtle.penup()
    turtle.ht()

    for yaxis in range(x,y):
        for xaxis in range(x,y):
            turtle.goto(xaxis*15,yaxis*15)
            turtle.dot(12, "lightgrey")


def deadCellsMethod():
    global deadCells
    for y in deadCells:
        y.dead()
    deadCells = set()
    

def birthCellsMethod():
    global birthCells
    for w in birthCells:
        w.alive()
    birthCells = set()
    
if __name__ == '__main__':    

    turtle.tracer(False)   
    grid(-22,22)

    cell1 = gameoflife(0,0)
    cell2 = gameoflife(0,1)
    cell3 = gameoflife(0,-1)
    cell4 = gameoflife(0,-2)
    cell5 = gameoflife(0,3)
    cell6 = gameoflife(0,4)
    cell7 = gameoflife(0,-4)
    cell8 = gameoflife(0,-5)
    cell9 = gameoflife(-1,2)
    cell10 = gameoflife(1,2)
    cell11 = gameoflife(-1,-3)
    cell12 = gameoflife(1,-3)

    cell13 = gameoflife(-10,-11)
    cell14 = gameoflife(-11,-11)
    cell15 = gameoflife(-9,-11)
    cell16 = gameoflife(-10,-12)

    cell17 = gameoflife(10,10)
    cell18 = gameoflife(11,10)
    cell19 = gameoflife(9,10)
    cell20 = gameoflife(10,11)

    cell21 = gameoflife(-10,10)
    cell22 = gameoflife(-11,10)
    cell23 = gameoflife(-9,10)
    cell24 = gameoflife(-10,11)

    cell25 = gameoflife(10,-11)
    cell26 = gameoflife(11,-11)
    cell27 = gameoflife(9,-11)
    cell28 = gameoflife(10,-12)

##    cell29 = gameoflife(-19,-17)
##    cell30 = gameoflife(-19,-16)
##    cell31 = gameoflife(-19,-15)
##    cell32 = gameoflife(-19,-11)
##    cell33 = gameoflife(-19,-10)
##    cell34 = gameoflife(-19,-9)
##    cell35 = gameoflife(-17,-19)
##    cell36 = gameoflife(-16,-19)
##    cell37 = gameoflife(-15,-19)
##    cell38 = gameoflife(-17,-14)
##    cell39 = gameoflife(-16,-14)
##    cell40 = gameoflife(-15,-14)
##    cell41 = gameoflife(-17,-12)
##    cell42 = gameoflife(-16,-12)
##    cell43 = gameoflife(-15,-12)
##    cell44 = gameoflife(-17,-7)
##    cell45 = gameoflife(-16,-7)
##    cell46 = gameoflife(-15,-7)
##    cell47 = gameoflife(-14,-17)
##    cell48 = gameoflife(-14,-16)
##    cell49 = gameoflife(-14,-15)
##    cell50 = gameoflife(-14,-11)
##    cell51 = gameoflife(-14,-10)
##    cell52 = gameoflife(-14,-9)
##    cell53 = gameoflife(-12,-17)
##    cell54 = gameoflife(-12,-16)
##    cell55 = gameoflife(-12,-15)
##    cell56 = gameoflife(-12,-11)
##    cell57 = gameoflife(-12,-10)
##    cell58 = gameoflife(-12,-9)
##    cell59 = gameoflife(-11,-19)
##    cell60 = gameoflife(-10,-19)
##    cell61 = gameoflife(-9,-19)
##    cell62 = gameoflife(-11,-14)
##    cell63 = gameoflife(-10,-14)
##    cell64 = gameoflife(-9,-14)
##    cell65 = gameoflife(-11,-12)
##    cell66 = gameoflife(-10,-12)
##    cell67 = gameoflife(-9,-12)
##    cell68 = gameoflife(-11,-7)
##    cell69 = gameoflife(-10,-7)
##    cell70 = gameoflife(-9,-7)
##    cell71 = gameoflife(-7,-17)
##    cell72 = gameoflife(-7,-16)
##    cell73 = gameoflife(-7,-15)
##    cell74 = gameoflife(-7,-11)
##    cell75 = gameoflife(-7,-10)
##    cell76 = gameoflife(-7,-9)
##
##    cell77 = gameoflife(19,17)
##    cell78 = gameoflife(19,16)
##    cell79 = gameoflife(19,15)
##    cell80 = gameoflife(19,11)
##    cell81 = gameoflife(19,10)
##    cell82 = gameoflife(19,9)
##    cell83 = gameoflife(17,19)
##    cell84 = gameoflife(16,19)
##    cell85 = gameoflife(15,19)
##    cell86 = gameoflife(17,14)
##    cell87 = gameoflife(16,14)
##    cell88 = gameoflife(15,14)
##    cell89 = gameoflife(17,12)
##    cell90 = gameoflife(16,12)
##    cell91 = gameoflife(15,12)
##    cell92 = gameoflife(17,7)
##    cell93 = gameoflife(16,7)
##    cell94 = gameoflife(15,7)
##    cell95 = gameoflife(14,17)
##    cell96 = gameoflife(14,16)
##    cell97 = gameoflife(14,15)
##    cell98 = gameoflife(14,11)
##    cell99 = gameoflife(14,10)
##    cell100 = gameoflife(14,9)
##    cell101 = gameoflife(12,17)
##    cell102 = gameoflife(12,16)
##    cell103 = gameoflife(12,15)
##    cell104 = gameoflife(12,11)
##    cell105 = gameoflife(12,10)
##    cell106 = gameoflife(12,9)
##    cell107 = gameoflife(11,19)
##    cell108 = gameoflife(10,19)
##    cell109 = gameoflife(9,19)
##    cell110 = gameoflife(11,14)
##    cell111 = gameoflife(10,14)
##    cell112 = gameoflife(9,14)
##    cell113 = gameoflife(11,12)
##    cell114 = gameoflife(10,12)
##    cell115 = gameoflife(9,12)
##    cell116 = gameoflife(11,7)
##    cell117 = gameoflife(10,7)
##    cell118 = gameoflife(9,7)
##    cell119 = gameoflife(7,17)
##    cell120 = gameoflife(7,16)
##    cell121 = gameoflife(7,15)
##    cell122 = gameoflife(7,11)
##    cell123 = gameoflife(7,10)
##    cell124 = gameoflife(7,9)



    cell1.alive()
    cell2.alive()
    cell3.alive()
    cell4.alive()
    cell5.alive()
    cell6.alive()
    cell7.alive()
    cell8.alive()
    cell9.alive()
    cell10.alive()
    cell11.alive()
    cell12.alive()

    cell13.alive()
    cell14.alive()
    cell15.alive()
    cell16.alive()

    cell17.alive()
    cell18.alive()
    cell19.alive()
    cell20.alive()

    cell21.alive()
    cell22.alive()
    cell23.alive()
    cell24.alive()

    cell25.alive()
    cell26.alive()
    cell27.alive()
    cell28.alive()

##    cell29.alive()
##    cell30.alive()
##    cell31.alive()
##    cell32.alive()
##    cell33.alive()
##    cell34.alive()
##    cell35.alive()
##    cell36.alive()
##    cell37.alive()
##    cell38.alive()
##    cell39.alive()
##    cell40.alive()
##    cell41.alive()
##    cell42.alive()
##    cell43.alive()
##    cell44.alive()
##    cell45.alive()
##    cell46.alive()
##    cell47.alive()
##    cell48.alive()
##    cell49.alive()
##    cell50.alive()
##    cell51.alive()
##    cell52.alive()
##    cell53.alive()
##    cell54.alive()
##    cell55.alive()
##    cell56.alive()
##    cell57.alive()
##    cell58.alive()
##    cell59.alive()
##    cell60.alive()
##    cell61.alive()
##    cell62.alive()
##    cell63.alive()
##    cell64.alive()
##    cell65.alive()
##    cell66.alive()
##    cell67.alive()
##    cell68.alive()
##    cell69.alive()
##    cell70.alive()
##    cell71.alive()
##    cell72.alive()
##    cell73.alive()
##    cell74.alive()
##    cell75.alive()
##    cell76.alive()
##
##    cell77.alive()
##    cell78.alive()
##    cell79.alive()
##    cell80.alive()
##    cell81.alive()
##    cell82.alive()
##    cell83.alive()
##    cell84.alive()
##    cell85.alive()
##    cell86.alive()
##    cell87.alive()
##    cell88.alive()
##    cell89.alive()
##    cell90.alive()
##    cell91.alive()
##    cell92.alive()
##    cell93.alive()
##    cell94.alive()
##    cell95.alive()
##    cell96.alive()
##    cell97.alive()
##    cell98.alive()
##    cell99.alive()
##    cell100.alive()
##    cell101.alive()
##    cell102.alive()
##    cell103.alive()
##    cell104.alive()
##    cell105.alive()
##    cell106.alive()
##    cell107.alive()
##    cell108.alive()
##    cell109.alive()
##    cell110.alive()
##    cell111.alive()
##    cell112.alive()
##    cell113.alive()
##    cell114.alive()
##    cell115.alive()
##    cell116.alive()
##    cell117.alive()
##    cell118.alive()
##    cell119.alive()
##    cell120.alive()
##    cell121.alive()
##    cell122.alive()
##    cell123.alive()
##    cell124.alive()



    while True:
        for x in cells:
            x.birth()
            x.cellVerdict()

        x1 = threading.Thread(target=deadCellsMethod())   
        x2 = threading.Thread(target=birthCellsMethod())

        x1.start()
        x2.start()

        x1.join()
        x2.join()

        recentBirth = []
        turtle.update()
        
    turtle.mainloop()


        
        

