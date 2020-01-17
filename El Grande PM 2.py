#El Grande Calculator
#There are 19 Calculators
#They are first defined, and then are called from CallCalc
#Once one Calculator has been run, the user can restart the program from run Again
import math
import time


#____________________________________________________________________________Algebra/Trig Calculators Defined_________________________________________________________________

#Calculator for Quadtratic Formula and Discriminant is defined (a)


def AlgA():
    #Explains Calculator
    #Calculator for the quadratic formula / discriminant
    #WARNING the final answer will come up with an error if the discrinant is negative
    print('Calculator for the quadratic formula ((-b +- Sqrt b^2-4ac)/2a) and the discriminant(b^2-4ac)')
    print('You find the variables in satndard quadratic form ax^2 + bx + c')
      

    print ('First value, a')
    while True:
        try:
    #Variable 1, a,
            a = float(input())
            break
        except ValueError:
           continue
    

    print('Second value, b')
    while True:
        try:
    #Variable 2, b
            b = float(input())
            break
        except ValueError:
           continue  
    print('Third Value, c')
    while True:
        try:
    #Variable 3, c 
            c = float(input())
            break
        except ValueError:
           continue
    #Quick Calculation
    aecell = (((b)**2)-4*a*c)
    #Calculator returns response
    print('\n')
    print('\n')
    print('The discriminant is')
    print(aecell)

    #explains answer
    print('\n')
    time.sleep(.5)
    print ('If the answer is negative, you have 2 unreal answers')
    time.sleep(.5)
    print ('If the answer is a postive number that has decimals, you have 2 answers')
    time.sleep(.5)
    print ('If the answer is a positive number, no decimals, then you can factor!')
    print('\n')
    print('\n')


    #Asks if it should do the rest of the quatratic formula
    #Cannot complete if discriminant is negative (can't find sqr root of negative)
    print ('Would you like to complete the rest of the quadractic formula? (Say "yes" if you do) \n Note, if discriminant is negative, program will come up with an error (You cannot find the square root of negatives)')
    #Response must be "yes" if you want to get the answers for the complete quadratic formula
    run = input()
    if run == 'yes':
        decell = ((-b + (math.sqrt(aecell)))/2*a)
        vecell = ((-b - (math.sqrt(aecell)))/2*a)
        print ('\n')
        print ('The answers are:')
        print ('\n')
        print ('\n')
        
        print ('For addition:')
        print(decell)
        print('\n')

        print ('For subtraction:')
        print(vecell)
        print('\n')
        time.sleep(.5)


        
#Law of Cosiges Calculator is defined (b)

def AlgB():
    #Explains Calculator
    #Calculator for Law of Cosines
    print('Calculator for Law of Cosines((a^2+b^2)-2*a*b*cos(c))')
    print ('First value, Side value 1 (b)')
    while True:
        try:
    #Variable 1, a, (side value)
            a = float(input())
            break
        except ValueError:
           continue
    

    print('Second value, Side value 2(b)')
    while True:
        try:
    #Variable 2, b, (side value)
            b = float(input())
            break
        except ValueError:
           continue  
    print('Third Value, Angle value (C)')
    while True:
        try:
    #Variable 3, C, (angle value)
            c = float(input())
            break
        except ValueError:
           continue
    #Quick Calculation
    accel = (math.sqrt((a**2+b**2)-2*a*b*math.cos(c)))
    #Calculator returns response
    print('The side value (c) across from angle C is:')
    print(accel)


def AlgC():
    #Explains Calculator
    #Calculator for Law of Sines
    print('Calculator for Law of Sines(Sin(A)/a = Sin(B)/b')
    print ('First value, side value 1 (a)')
    while True:
        try:
    #Variable 1, a, (side value)
            a = float(input())
            break
        except ValueError:
           continue
    print('Second value, angle value A (The angle across from side a)')
    while True:
        try:
    #Variable 2, b, (side value)
            b = float(input())
            break
        except ValueError:
           continue
    accel = ((math.sin(a))/b)
    print ('The ratiom is:')


def AlgD():
    #Explains Calculator
    #Calculator for X vertex value
    print('Calculator for X vertex value (-b/2a)')
    print ('First value, b (found in standard quadratic form, 2nd term)')
    while True:
        try:
            b = float(input())
            break
        except ValueError:
           continue
    print('Second value, a (found in standard quadratic form, 1st term)')
    while True:
        try:
            a = float(input())
            break
        except ValueError:
           continue
    accel = ((-b)/(2*a))
    print ('The ratiom is:')



#____________________________________________________________________________3d Calculators Defined_________________________________________________________________
#Volume of Sphere Calculator is defined (3dA)

    
def ThreeA():
    #Explains Calculator
    #Calculator for Volume of a Sphere
    print('Calculator for volume of a Sphere((4/3)π*r^3)')
    print ('First value, Radius value (r)')
    while True:
        try:
    #Variable 1, r, radius value
            r = flat(input())
            break
        except ValueError:
           continue
        
    accel = ((4/3)*math.pi*(r**3))
    print ('The Volume is:')
    print (accel)

    
#Surface Area of Sphere Calculator is defined (3dB)

    
def ThreeB():
    #Explains Calculator
    #Calculator for Surface Area of Sphere
    print('Calculator for Volume of a Sphere(4*π*(r^2)')
    print ('First value, Radius value (r)')
    while True:
        try:
    #Variable 1, r, radius value
            r = float(input())
            break
        except ValueError:
           continue
        
    accel = (4*math.pi*(r**2))
    print ('The Surface Area is:')
    print (accel)

    
#Volume of Cylinder Calculator is defined (3dC)

    
def ThreeC():
    #Explains Calculator
    #Calculator for the Volume of a Cylinder
    print('Calculator for volume of a Cylinder(π*(r**2)*h)')
    print ('First value, Radius value (r)')
    while True:
        try:
    #Variable 1, r, radius value
            r = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Height value (h)')
    while True:
        try:
    #Variable 2, h, Height value
            h = int(input())
            break
        except ValueError:
           continue
        
    accel = (math.pi*(r**2)*h)
    print ('The Volume is:')
    print (accel)


#Surface Area of Cylinder Calculator is defined (3dD)

    
def ThreeD():
    #Explains Calculator
    #Calculator for the Surface Area of a Cylinder
    print('Calculator for Surface Area of a Cylinder (2*π*r)*(r+h)')
    print ('First value, Radius value (r)')
    while True:
        try:
    #Variable 1, r, radius value
            r = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Height value (h)')
    while True:
        try:
    #Variable 2, h, Height value
            h = float(input())
            break
        except ValueError:
           continue
        
    accel = ((2*math.pi*r)*(r+h))
    print ('The Surface Area is:')
    print (accel)


#Lateral Area of Cylinder Calculator is defined (3dE)

    
def ThreeE():
    #Explains Calculator
    #Calculator for the Lateral Area of a Cylinder
    print('Calculator for Lateral Area of a Cylinder (2*π*r*h)')
    print ('First value, Radius value (r)')
    while True:
        try:
    #Variable 1, r, radius value
            r = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Height value (h)')
    while True:
        try:
    #Variable 2, h, Height value
            h = int(input())
            break
        except ValueError:
           continue
        
    accel = (2*math.pi*r*h)
    print ('The Lateral Area is:')
    print (accel)


#Volume of a Pyramid (3dF)

    
def ThreeF():
    #Explains Calculator
    #Calculator for Volume of Pyramid
    print('Calculator for Volume of a Pyramid ((1/3)*b*h)')
    print ('First value, Base value (B) \n(To get B, multiply the Square on the bottom of the Pyramids by Length time Width)')
    while True:
        try:
    #Variable 1, r, radius value
            b = float(input())
            break
        except ValueError:
           continue

    print ('Second value, Height value (h)')
    while True:
        try:
    #Variable 2, h, Height value
            h = float(input())
            break
        except ValueError:
           continue
        
    accel = ((1/3)*b*h)
    print ('The Volume is:')
    print (accel)


#Surface Area of a Pyramid (3dG)

    
def ThreeG():
    #Explains Calculator
    #Calculator for Surface Area of Pyramid
    print('Calculator for Surface Area of a Pyramid ((1/2*lp)+B)')
    print ('First value, Base value (B) \n(To get B, multiply the Square on the bottom of the Pyramids by Length times Width)')
    while True:
        try:
    #Variable 1, B, Base value
            b = float(input())
            break
        except ValueError:
           continue

    print ('Second value, Lateral Height value (l) \n(You can find this, if not already found, through trig functions)')
    while True:
        try:
    #Variable 2, l, Lateral Height value
            l = float(input())
            break
        except ValueError:
           continue
    print ('Third value, Perimeter of Base value \n(If not found, add the sides of the base up)')
    while True:
        try:
    #Variable 3, p, Perimeter of Base value
            p = float(input())
            break
        except ValueError:
           continue
    
        
    accel = (((1/2)*l*p)+b)
    print ('The Surface Area is:')
    print (accel)


#Lateral Area of a Pyramid (3dH)

    
def ThreeH():
    #Explains Calculator
    #Calculator for Lateral Area of Pyramid
    print('Calculator for Lateral Area of a Pyramid (1/2*lp)')
    print ('First value, Lateral Height value (l) \n(You can find this, if not already found, through trig functions)')
    while True:
        try:
    #Variable 1, l, Lateral Height value
            l = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Perimeter of Base value \n(If not found, add the sides of the base up)')
    while True:
        try:
    #Variable 2, p, Perimeter of Base value
            p = float(input())
            break
        except ValueError:
           continue
    
        
    accel = ((1/2)*l*p)
    print ('The Lateral Area is:')
    print (accel)


#Volume of a Cone (3dI)

    
def ThreeI():
    #Explains Calculator
    #Calculator for Volume of Cone
    print('Calculator for Volume of a cone(1/3*π*r^2*h)')
    print ('First value, Radius value (r)')
    while True:
        try:
    #Variable 1, r, Radius value
            r = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Height value (h)')
    while True:
        try:
    #Variable 2, h, Height Value
            h = float(input())
            break
        except ValueError:
           continue
    
        
    accel = ((1/3)*math.pi*(r**2)*h)
    print ('The Volume is:')
    print (accel)


#Surface Area of a Cone (3dJ)

    
def ThreeJ():
    #Explains Calculator
    #Calculator for Surface Area of Cone
    print('Calculator for Surface Area of a cone(π*r(1+r))')
    print ('First value, Radius value (r)')
    while True:
        try:
   #Variable 1, r, Radius value
            r = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Lateral Height value (l)')
    while True:
        try:
   #Variable 2, l, Lateral Height Value
            l = float(input())
            break
        except ValueError:
           continue
    
        
    accel = (math.pi*r*(1+r))
    print ('The Surface Area is:')
    print (accel)


#Lateral Area of a Cone (3dK)

    
def ThreeK():
    #Explains Calculator
    #Calculator for Lateral Area of Cone
    print('Calculator for Lateral Area of a cone(π*r*l)')
    print ('First value, Radius value (r)')
    while True:
        try:
   #Variable 1, r, Radius value
            r = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Lateral Height value (l)')
    while True:
        try:
   #Variable 2, l, Lateral Height Value
            l = float(input())
            break
        except ValueError:
           continue
    
        
    accel = (math.pi*r*l)
    print ('The Lateral Area is:')
    print (accel)

    
#Volume of a Rectangular Prism (3dL)

    
def ThreeL():
    #Explains Calculator
    #Calculator for Volume of a Rectangular Prism
    print('Calculator for Volume of a Rectangular Prism (lwh)')
    print ('First value, Length (l)')
    while True:
        try:
   #Variable 1, l, Length value
            l = float(input())
            break
        except ValueError:
            continue
    print ('Second value, Width (w)')
    while True:
        try:
   #Variable 2, w, Width value
            w = float(input())
            break
        except ValueError:
            continue
    print ('Third value, Height (h)')
    while True:
        try:
   #Variable 3, h, Height value
            h = float(input())
            break
        except ValueError:
            continue


    accel = (l*w*h)
    print ('The Volume is:')
    print (accel)

    
#Surface Area of a Rectangular Prism (3dM)

    
def ThreeM():
    #Explains Calculator
    #Calculator for Surface Area of Cone
    print('Calculator for Surface Area of a Rectangular Prism(2lw+2lh+2wh)')
    print ('First value, Length (l)')
    while True:
        try:
   #Variable 1, l, Length value
            l = float(input())
            break
        except ValueError:
            continue
    print ('Second value, Width (w)')
    while True:
        try:
   #Variable 2, w, Width value
            w = float(input())
            break
        except ValueError:
            continue
    print ('Third value, Height (h)')
    while True:
        try:
   #Variable 3, h, Height value
            h = float(input())
            break
        except ValueError:
            continue


    accel = ((2*l*w)+(2*l*h) +(2*w*h))
    print ('The Surface Area is:')
    print (accel)


#Volume of any Prism (3N)


def ThreeN():
    #Explains Calculator
    #Calculator for Volume of any Prism
    print('Calculator for Volume of any Prism(B*h)')
    print ('First value, Base value (B) \n(To get B, find the area of the base. Many ways to do this depending on the shape)')
    while True:
        try:
    #Variable 1, B, Base value
            b = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Height (h)')
    while True:
        try:
   #Variable 2, h, Height value
            h = float(input())
            break
        except ValueError:
            continue

        
    accel = (b*h)
    print ('The Volume is:')
    print (accel)


#Surface Area of any Prism (3dO)


def ThreeO():
    #Explains Calculator
    #Calculator for Lateral Area of any Prism
    print('Calculator for Surface Area of any Prism((h*p)+2B)')
    print ('First value, Base value (B) \n(To get B, find the area of the base. Many ways to do this depending on the shape)')
    while True:
        try:
    #Variable 1, B, Base value
            b = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Perimeter of Base value \n(If not found, add the sides of the base up)')
    while True:
        try:
    #Variable 2, p, Perimeter of Base value
            p = float(input())
            break
        except ValueError:
           continue
    print ('Third value, Height (h)')
    while True:
        try:
   #Variable 3, h, Height value
            h = float(input())
            break
        except ValueError:
            continue

        
    accel = ((h*p)+(2*b))
    print ('The Volume is:')
    print (accel)


#Lateral Area of any Prism (3dP)


def ThreeP():
    #Explains Calculator
    #Calculator for Lateral Area of any Prism
    print('Calculator for Lateral Area of any Prism(p*h)')
    print ('First value, Perimeter of Base value \n(If not found, add the sides of the base up)')
    while True:
        try:
    #Variable 1, p, Perimeter of Base value
            p = float(input())
            break
        except ValueError:
           continue
    print ('Second value, Height (h)')
    while True:
        try:
   #Variable 2, h, Height value
            h = float(input())
            break
        except ValueError:
            continue

        
    accel = (p*h)
    print ('The Lateral Area is:')
    print (accel)

#____________________________________________________________________________2d Calculators defined_________________________________________________________________ 

def TwoA():
    #Explains Calculator
    #Calculator for Pythagorean Theorem
    print('Calculator for Pythagorean Theorem')
    print ('First value, side a')
    while True:
        try:
    #Variable 1, a, side 1 value
            a = float(input())
            break
        except ValueError:
           continue
    print ('Second value, side b')
    while True:
        try:
    #Variable 2, b, side 2 value
            b = float(input())
            break
        except ValueError:
           continue

    accel = (math.sqrt((b**2)*(a**2)))
    print ('Side C is:')
    print (accel)


def TwoB():
    #Explains Calculator
    #Calculator for Area of a Circle
    print('Calculator for Area of a Circle')
    print ('First value, Radius value')
    while True:
        try:
    #Variable 1, a, side 1 value
            r = float(input())
            break
        except ValueError:
           continue
        
    accel = (math.pi*(r**2))
    print ('The area of the Circle is:')
    print (accel)


def TwoC():
    #Explains Calculator
    #Calculator for Circumfrence of a Circle
    print('Calculator for Circumfrence of a Circle')
    print ('First value, Radius value')
    while True:
        try:
    #Variable 1, a, side 1 value
            r = float(input())
            break
        except ValueError:
           continue
        
    accel = (2*math.pi*r)
    print ('The ircumfrence of the Circle is:')
    print (accel)


def TwoD():
    #Explains Calculator
    #Calculator for Area of a Rectangle
    print('Calculator for Area of a Rectangle')
    print ('First value, Length value')
    while True:
        try:
    #Variable 1, a, side 1 value
            l = float(input())
            break
        except ValueError:
           continue
    print ('Secong value, Width value')
    while True:
        try:
    #Variable 1, a, side 1 value
            w = float(input())
            break
        except ValueError:
           continue
        
    accel = (l*w)
    print ('The Area of the Rectangle is:')
    print (accel)


def TwoE():
    #Explains Calculator
    #Calculator for Perimeter of a Rectangle
    print('Calculator for Perimeter of a Rectangle')
    print ('First value, Length value')
    while True:
        try:
    #Variable 1, a, side 1 value
            l = float(input())
            break
        except ValueError:
           continue
    print ('Secong value, Width value')
    while True:
        try:
    #Variable 1, a, side 1 value
            w = float(input())
            break
        except ValueError:
           continue
        
    accel = (2*(1+w))
    print ('The Area of the Rectangle is:')
    print (accel)


def TwoF():
    #Explains Calculator
    #Calculator for Perimeter of a Rectangle
    print('Calculator for  Area of a Triagle')
    print ('First value, Base value')
    while True:
        try:
    #Variable 1, a, side 1 value
            b = float(input())
            break
        except ValueError:
           continue
    print ('Secong value, Height value')
    while True:
        try:
    #Variable 1, a, side 1 value
            h = float(input())
            break
        except ValueError:
           continue
        
    accel = ((1/2)*b*h)
    print ('The Area of the Triagle is:')
    print (accel)


def TwoG():
    #Explains Calculator
    #Calculator for Area of a Parallelogram
    print('Calculator for  Area of a Parallelogram')
    print ('First value, Base 1 value')
    while True:
        try:
    #Variable 1, a, side 1 value
            a = float(input())
            break
        except ValueError:
           continue
    print ('First value, Base 2 value')
    while True:
        try:
    #Variable 1, a, side 1 value
            b = float(input())
            break
        except ValueError:
           continue
    print ('Secong value, Height value')
    while True:
        try:
    #Variable 1, a, side 1 value
            h = float(input())
            break
        except ValueError:
           continue
        
    accel = ((1/2)*h*(a+b))
    print ('The Area of the Parallelogram is:')
    print (accel)








#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-Working on adding dictionarys or index, currently just if statements_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


#____________________________________________________________________________Algebra/Trig Menu_________________________________________________________________
def Alg():
    print('Hi! Welcome to the Algebra/Trig Menu. From here you can call Algebra or Trig formula calculators. \n\n Which Calculator would you like to run today, friend?')
    print(' a = Quadratic Formula/Disriminant\n b = Law of Cosigns \n c = Law of sines \n d = X value of vertex \n e = Slope formula \n f = Midpoint formula \n Only the first two work currently, we are under construction :)')
    AlgRun = input()
    if AlgRun == 'a':
        AlgA()
    if AlgRun == 'b':
        AlgB()
    if AlgRun == 'c':
        AlgC()
    if AlgRun == 'd':
        AlgD()
    if AlgRun == 'e':
        #AlgE()
        print ('We are currently undergoing construction on this calculator. The maker of El Grande Calculator apologizes for the inconvenience.')
    if AlgRun == 'f':
        #AlgF()
        print ('We are currently undergoing construction on this calculator. The maker of El Grande Calculator apologizes for the inconvenience.')

#____________________________________________________________________________3d Menu_________________________________________________________________
def Three():
    print('Howdy! Welcome to the Three Dimensional Menu. From here you can call Three Dimensional Geometry formula calculators. \n\n Which Calculator would you like to run today, partner?')
    print(' a = Volume of a Sphere \n b = Surface Area of a Sphere')
    print(' c = Volume of a Cylinder \n d = Surface Area of a Cylinder \n e = Lateral Area of a Cylinder')
    print(' f = Volume of a Pyramid \n g = Surface Area of a Pyramid \n h = Lateral Area of a Pyramid')
    print(' i = Volume of a Cone \n j = Surface Area of a Cone \n k = Lateral Area of a Cone')
    print(' l = Volume of a Rectangular Prism \n m = Surface Area of a Rectangular Prism')
    print(' n = Volume of any Prism \n o = Surface Area of any Prism \n p = Lateral Area of a any Prism')
    ThreeRun = input()
    if ThreeRun == 'a':
        ThreeA()
    if ThreeRun == 'b':
        ThreeB()
    if ThreeRun == 'c':
        ThreeC()
    if ThreeRun == 'd':
        ThreeD()
    if ThreeRun == 'e':
        ThreeE()
    if ThreeRun == 'f':
        ThreeF()
    if ThreeRun == 'g':
        ThreeG()
    if ThreeRun == 'h':
        ThreeH()
    if ThreeRun == 'i':
        ThreeI()
    if ThreeRun == 'j':
        ThreeJ()
    if ThreeRun == 'k':
        ThreeK()
    if ThreeRun == 'l':
        ThreeL()
    if ThreeRun == 'm':
        Three()
    if ThreeRun == 'n':
        ThreeN()
    if ThreeRun == 'o':
        ThreeO()
    if ThreeRun == 'p':
        ThreeP()
#____________________________________________________________________________2d Menu_________________________________________________________________
def Two():
    print ('G\'day mate! Welcome to the Two Dimensional Menu. From here you can call Two Dimensional Geometry formula calculators. \n\n Which Calculator would you like to run today, mate?')
    print (' a = Pythagorean Theorem \n b = Area of a Circle \n c = Circumfrence of a Circle \n d = Area of a Rectangle \n e = Perimeter of a Rectangle \n f = Area of a Triagle \n g = Area of a Parallelogram')
    TwoRun = input()
    if TwoRun == 'a':
        TwoA()
    if TwoRun == 'b':
        TwoB()
    if TwoRun == 'c':
        TwoC()
    if TwoRun == 'd':
        TwoD()
    if TwoRun == 'e':
        TwoE()
    if TwoRun == 'f':
        TwoF()
    if TwoRun == 'g':
        TwoG()
        




        

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-_-__-_-_-_-Main Menu_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_    
def CalcMenu():
    print('Hello. This is the main menu of El Grande Calulator. From here you can go to a more specific menu of calulator programs. \n\n Which type of Calculator would you be intrested in running today?')
    print(' a = Algebra or Trig Calculators \n b = Three dimenisional formula Calculators \n c = Two dimenisional Calculator formulas')

    menu = input()
    if menu == 'a':
        Alg()
    if menu == 'b':
        Three()
    if menu == 'c':
        Two()
   



    
CalcMenu()


     



#This is runAgain
#It can rerun the whole program

def runAgain():
    print('\n\n')
    time.sleep(.75)
    print ('Do you want to run El Grande Calculator again? (Say "yes" if you do)')
    #Response must be "yes" if you want to rerun the program
    run = input()
    if run == 'yes':
        CalcMenu()
        runAgain()
runAgain()
