def circlecalculations (useroption,suboption):
    if(useroption==1 and suboption==2):
        radius=float(input("Enter radius value?"))
        diameter=2*radius
        print("diameter=",diameter)
    elif(useroption==1 and suboption==2):
        radius=float(input("Enter radius value?"))
        cir=2*3.14*radius
        print("circumference=",cir)
    else:
        radius=float(input("Enter radius value?"))
        area=3.14*(radius*radius)
        print("area=",area)
def squarecalculations(useroption,suboption):
    if(useroption==2 and suboption==1):
        width=float(input("Enter width?"))
        perimeter=4*width
        print("perimeter=",perimeter)
    else:
        width=float(input("Enter width?"))
        area=width*width
        print("area=",area)
def rectanglecalculations(useroption,suboption):
    if(useroption==3 and suboption==1):
        length=float(input("Enter length?"))
        width=float(input("Enter width?"))
        perimeter=(2*length)+(2*width)
        print("perimeter=",perimeter)
    else:
        length=float(input("Enter length?"))
        width=float(input("Enter width?"))
        area=length*width
        print("area=",area)
def MainMenu():
    print("press 1 to circle")
    print("press 2 to square")
    print("press 3 to rectangle")
    useroption=int(input("press 1/2/3..?"))

    if(useroption==1):
        print("....options....")
        print("press 1 to diameter")
        print("press 2 to circumference")
        print("press 3 to area")
        suboption=int(input("press 1/2/3 ...?"))
        circlecalculations(useroption,suboption)

    elif(useroption==2 or useroption==3):
        print("....options....")
        print("press 1 to perimeter")
        print("press 2 to area")
        suboption=int(input("press 1/2...?"))
        if(useroption==2):
            squarecalculations(useroption,suboption)
        elif(useroption==3):
            rectanglecalculations(useroption,suboption)

programexit=1
while(programexit!=0):
    MainMenu()
    programexit=int(input("press 0 to exit, 1 to continue...?"))
