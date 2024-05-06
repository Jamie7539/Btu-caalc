# Ask the user for room name
roomChoice = input("Enter the room name: ")
    
# Ask the user the size of the room in meters
cubicMeters = float(input("What is the size of " + roomChoice + " in cubic meters? "))
    
# Ask for room type
roomType = input("Is the room a lounge, dining, bathroom, bedroom, hallway, or kitchen? ")

# Determine multiplier based on room type
if roomType.lower() in ['lounge', 'dining', 'bath']:
    roomMultiplier = 5
elif roomType.lower() == 'bedroom':
    roomMultiplier = 4 
elif roomType.lower() in ['hallway', 'kitchen']:
     roomMultiplier = 3
else:
    print("Invalid input, code will now go crazy")
    roomMultiplier = 99999999999999999999999
        
# Ask if the room is facing north
northFacing = input("Is the room facing north? (yes/no) ")
if northFacing.lower() == 'yes':
    roomMultiplier *= 1.15
    
# Ask if room has French windows
frenchWindow = input("Does the room have French windows? (yes/no) ")
if frenchWindow.lower() == 'yes':
    roomMultiplier *= 1.2
    
# Ask if windows are double glazed
doubleGlaze = input("Are the windows double glazed? (yes/no) ")
if doubleGlaze.lower() == 'yes':
    roomMultiplier *= 0.9
    
# Calculate heat
BTU_Heat = cubicMeters * roomMultiplier
# Print the result
print(f"the required heat for {roomChoice} is: {BTU_Heat} ")