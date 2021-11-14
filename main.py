import time as t
v = "v1 alpha"
print("Geometric Transformation Calculator " + v)
while __name__ == "__main__": #Infinite Loop when ran from CMD
    
    t.sleep(1) #Distinction
    
    countNum, CentreX, CentreY, TempX, TempY, PostX, PostY, VertStretch, HorizStretch, Rotation, Yflection, Xflection = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #Initialize Variables
    PreX, PreY, TempX, TempY, PostX, PostY, funcOrder= [], [], [], [], [], [], [] #Initialize Lists
    
    print("Don't use any letters nor symbols other than negative signs or decimal points!")
    print("Separate all X and Y values with spaces (i.e. 1 2 3 4...)") #Instructions
    PreX = (input("Pre X = ")).split(" ") #Turn X values into Lists for operations en masse
    PreY = (input("Pre Y = ")).split(" ") #Turn Y values into Lists for operations en masse
    PreX = [float(countNum) for countNum in PreX] #Turn X values into floats just for good measure
    PreY = [float(countNum) for countNum in PreY] #Turn Y values into floats just for good measure
    
    print("Now type in singular values.") #Instructions
    CentreX = float(input("Centre X = ")) #Input X point of Centre of Transformations
    CentreY = float(input("Centre Y = ")) #Input Y point of Centre of Transformations
    
    TempX = [float(countNum - CentreX) for countNum in PreX] #Subtract the CentreX from PreX and store it into list TempX
    TempY = [float(countNum - CentreY) for countNum in PreY] #Subtract the CentreY from PreX and store it into list TempX
    
    print("Choose a SINGULAR transformation to do... I'm working on the ability to change order of functions.") #Instructions
    
    VertStretch = input("Vertical Stretch Factor (Set to 1 to not include) = ") #Vertical Stretch
    if VertStretch == '' or VertStretch == 1: #If Vertical Stretch is not specified...
        VertStretch = 1 #Set it to one, thereby having no effect on the transformation.
    VertStretch = float(VertStretch) #Turn VertStretch into a float just for good measure
    
    HorizStretch = input("Horizontal Stretch Factor (Set to 1 to not include) = ") #Horizontal Stretch
    if HorizStretch == '': #If Horizontal Stretch is not specified...
        HorizStretch = 1 #Set it to one, thereby having no effect on the transformation.
    HorizStretch = float(HorizStretch) #Turn HorizStretch into a float just for good measure
    
    Rotation = input("Counterclockwise Rotation with 90, 180, 270 degrees (Set to 0 to not use) = ") #Rotation Factor
    Rotation = int(Rotation) #Make sure the value has no decimal
    
    Yflection = input("Reflection over y (Press ENTER to not include) = ") #Reflection changing Y values
    Xflection = input("Reflection over x (Press ENTER to not include) = ") #Reflection changing X values
        
    if VertStretch != 1: #If the value is being used...
        TempY = [float(countNum) * VertStretch for countNum in TempY] #Apply Vertical Stretch
        
    if HorizStretch != 1: #If the value is being used...
        TempX = [float(countNum) * HorizStretch for countNum in TempX] #Apply Horizontal Stretch
        
    if Rotation > 0: #If the value is being used...
        
        if Rotation == 270: #If the value is to be rotated 270 degrees counterclockwise...
            TempX, TempY = [float(countNum) for countNum in TempY], [float(countNum) * -1 for countNum in TempX] #Rotate it by 270 degrees counterclockwise (y, -x)
            
        elif Rotation == 180: #If the value is to be rotated 180 degrees...
            TempX, TempY = [float(countNum) * -1 for countNum in TempX], [float(countNum) * -1 for countNum in TempY] #Rotate it by 180 degrees counterclockwise (x, -y)
            
        elif Rotation == 90: #If the value is to be rotated 90 degrees counterclockwise...
            TempX, TempY = [float(countNum) * -1 for countNum in TempY], [float(countNum) for countNum in TempX] #Rotate it by 90 degrees counterclockwise (-y, x)
    
    try: #Confirms that Yflection is an integer
        Yflection = int(Yflection)
    except:
        Yflection = 'N'
        
    try: #Confirms that Xflection is an integer
        Xflection = int(Xflection)
    except:
        Xflection = 'N'
    
    if (isinstance(Yflection, int) or isinstance(Yflection, float)) and Yflection != None: #If we can reflect with this variable...
        Yflection = int(Yflection) #For extra measure
        TempY = [(Yflection+((countNum)-Yflection)*-1) for countNum in TempY] #Reflect over y = Xflection
    
    if (isinstance(Xflection, int) or isinstance(Xflection, float)) and Xflection != None: #If we can reflect with this variable...
        Xflection = int(Xflection) #For extra measure
        TempX = [(Xflection+((countNum)-Xflection)*-1) for countNum in TempX] #Reflect over x = Xflection
    
    PostX, PostY = [(countNum) + CentreX for countNum in TempX], [(countNum) + CentreY for countNum in TempY] #Subtract the CentreX and CentreY from TempX and TempY respectively
    
    input(f"Pre-Image\nX = {PreX}\nY = {PreY}\n\nPost-Image\nX = {PostX}\nY = {PostY}\n\nPress ENTER to continue...") #Return the results
    print("\n")
