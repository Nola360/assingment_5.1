#Akinola Daramola Jr
#Programming Exercise 5.1
#Due Date: 07/13/2022

"""
Kilometer Converter?
 Write a program that asks the user to enter a distance in kilometer, then converts that distance to miles.
 The conversion formula is as follows:  Miles = kilometers X 0.6214

"""

#Define main function
def main():
    
    #Calling function
    km_converter()
    
#Define converter function
def km_converter() :
    #Declaring kilometers dynamically
    kilometers = float(input("Enter distance in kilometers: "))
    
    #Declaring value of miles variable
    miles = kilometers * 0.6214
    
    #Display kilometers converted to miles
    print(f"Kilometers: {kilometers:.2f}\nMiles: {miles:.2f}")

#Calling function
main()
