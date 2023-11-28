#This code is going to allow the user to type a state that they want to find the statistics for different crime rates
# Here we are defining crime statistics data rates
#These crime rates are based off of every 1,000 people/incidents
crime_data = {
#this information will give you all the crime statistics data in Alabama
    "Alabama": {
        "Homicide": 7.3,
        "Robbery": 80.4 ,
        "Burglary": 531.9,
        "Assault": 381.0,
    },
#this information will give you all the crime statistics data in Alaska
    "Alaska": {
        "Homicide": 10.8,
        "Robbery": 103.16,
        "Burglary": 9.7,
        "Assault": 16.8,
    },
#this information will give you all the crime statistics data in Arizona
 "Arizona": {
        "Homicide": 7.34,
        "Robbery": 0.61,
        "Burglary": 3.22,
        "Assault": 29.36,
    },
#this information will give you all the crime statistics data in Arkansas
 "Arkansas": {
        "Homicide": 16.1,
        "Robbery": 0.61,
        "Burglary": 4.86,
        "Assault": 15.6,
    },
#this information will give you all the crime statistics data in California
 "California": {
        "Homicide": 5.7,
        "Robbery": 122.1,
        "Burglary": 367.5,
        "Assault": 330.0,
    },
#this information will give you all the crime statistics data in Colorado
 "Colorado": {
        "Homicide": 0.06,
        "Robbery": 0.74,
        "Burglary": 2.71,
        "Assault": 3.30,
    },
#this information will give you all the crime statistics data in Connecticut
 "Connecticut": {
        "Homicide": 4.22,
        "Robbery": 0.54,
        "Burglary": 1.41,
        "Assault": 0.83,
    },
#this information will give you all the crime statistics data in Delaware
 "Delaware": {
        "Homicide": 0.09,
        "Robbery": 0.57,
        "Burglary": 2.37,
        "Assault": 3.25,
    },
#this information will give you all the crime statistics data in Florida
 "Florida": {
        "Homicide": 0.06,
        "Robbery": 0.51,
        "Burglary": 2.13,
        "Assault": 2.94,
    },
#this information will give you all the crime statistics data in Georgia
 "Georgia": {
        "Homicide": 0.08,
        "Robbery": 0.48,
        "Burglary": 2.16,
        "Assault": 3.01,
    },
#this information will give you all the crime statistics data in Hawaii
 "Hawaii": {
        "Homicide": 0.03,
        "Robbery": 0.55,
        "Burglary": 3.21,
        "Assault": 1.52,
    },
#this information will give you all the crime statistics data in Idaho
 "Idaho": {
        "Homicide": 0.02,
        "Robbery": 0.09,
        "Burglary": 1.70,
        "Assault": 1.80,
    },
#this information will give you all the crime statistics data in Illinois
 "Illinois": {
        "Homicide": 0.09,
        "Robbery": 0.80,
        "Burglary": 2.71,
        "Assault": 2.62,
    },
#this information will give you all the crime statistics data in Indiana
 "Indiana": {
        "Homicide": 0.07,
        "Robbery": 0.47,
        "Burglary": 2.18,
        "Assault": 2.22,
    },
#this information will give you all the crime statistics data in Iowa
 "Iowa": {
        "Homicide": 0.03,
        "Robbery": 0.22,
        "Burglary": 2.62,
        "Assault": 2.28,
    },
#this information will give you all the crime statistics data in Kansas
 "Kansas": {
        "Homicide": 0.05,
        "Robbery": 0.36,
        "Burglary": 2.96,
        "Assault": 3.31,
    },
#this information will give you all the crime statistics data in Kentucky
 "Kentucky": {
        "Homicide": 0.09,
        "Robbery": 0.50,
        "Burglary": 2.95,
        "Assault": 1.81,
    },
#this information will give you all the crime statistics data in Louisiana
 "Louisiana": {
        "Homicide": 0.18,
        "Robbery": 0.54,
        "Burglary": 5.88,
        "Assault": 5.56,
    },
#this information will give you all the crime statistics data in Maine
 "Maine": {
        "Homicide": 0.02,
        "Robbery": 0.12,
        "Burglary": 1.27,
        "Assault": 0.63,
    },
#this information will give you all the crime statistics data in Maryland
 "Maryland": {
        "Homicide": 0.10,
        "Robbery": 0.98,
        "Burglary": 2.23,
        "Assault": 2.56,
    },
#this information will give you all the crime statistics data in Massachusetts
 "Massachusetts": {
        "Homicide": 0.02,
        "Robbery": 0.38,
        "Burglary": 1.39,
        "Assault": 2.36,
    },
#this information will give you all the crime statistics data in Michigan
 "Michigan": {
        "Homicide": 0.08,
        "Robbery": 0.61,
        "Burglary": 2.03,
        "Assault": 3.82,
    },
#this information will give you all the crime statistics data in Minnesota
 "Minnesota": {
        "Homicide": 0.04,
        "Robbery": 0.71,
        "Burglary": 2.57,
        "Assault": 1.97,
    },
#this information will give you all the crime statistics data in Mississippi
 "Mississippi": {
        "Homicide": 0.09,
        "Robbery": 0.39,
        "Burglary": 3.55,
        "Assault": 1.68,
    },
#this information will give you all the crime statistics data in Missouri
 "Missouri": {
        "Homicide": 0.10,
        "Robbery": 0.60,
        "Burglary": 3.05,
        "Assault": 4.09,
    },
#this information will give you all the crime statistics data in Montana
 "Montana": {
        "Homicide": 0.05,
        "Robbery": 0.27,
        "Burglary": 2.39,
        "Assault": 3.82,
    },
#this information will give you all the crime statistics data in Nebraska
 "Nebraska": {
        "Homicide": 0.03,
        "Robbery": 0.34,
        "Burglary": 1.91,
        "Assault": 2.15,
    },
#this information will give you all the crime statistics data in Nevada
 "Nevada": {
        "Homicide": 0.07,
        "Robbery": 0.74,
        "Burglary": 4.01,
        "Assault": 2.87,
    },
#this information will give you all the crime statistics data in New Hampshire
 "New Hampshire": {
        "Homicide": 0.01,
        "Robbery": 0.14,
        "Burglary": 0.80,
        "Assault": 0.74,
    },
#this information will give you all the crime statistics data in New Jersey
 "New Jersey": {
        "Homicide": 0.04,
        "Robbery": 0.38,
        "Burglary": 1.19,
        "Assault": 1.10,
    },
#this information will give you all the crime statistics data in New Mexico
 "New Mexico": {
        "Homicide": 0.08,
        "Robbery": 0.88,
        "Burglary": 6.34,
        "Assault": 6.26,
    },
#this information will give you all the crime statistics data in North Carolina
 "North Carolina": {
        "Homicide": 0.10,
        "Robbery": 0.58,
        "Burglary": 3.87,
        "Assault": 3.31,
    },
#this information will give you all the crime statistics data in North Dakota
 "North Dakota": {
        "Homicide": 0.04,
        "Robbery": 0.25,
        "Burglary": 3.90,
        "Assault": 1.80,
    },
#this information will give you all the crime statistics data in Ohio
 "Ohio": {
        "Homicide": 0.08,
        "Robbery": 0.61,
        "Burglary": 2.82,
        "Assault": 2.20,
    },
#this information will give you all the crime statistics data in Oklahoma
 "Oklahoma": {
        "Homicide": 0.07,
        "Robbery": 0.46,
        "Burglary": 5.29,
        "Assault": 3.28,
    },
#this information will give you all the crime statistics data in Oregon
 "Oregon": {
        "Homicide": 0.05,
        "Robbery": 0.62,
        "Burglary": 3.35,
        "Assault": 2.47,
    },
#this information will give you all the crime statistics data in Pennsylvania
 "Pennsylvania": {
        "Homicide": 0.09,
        "Robbery": 0.64,
        "Burglary": 2.02,
        "Assault": 2.28,
    },
#this information will give you all the crime statistics data in Rhode Island
 "Rhode Island": {
        "Homicide": 0.03,
        "Robbery": 0.25,
        "Burglary": 1.41,
        "Assault": 1.32,
    },
#this information will give you all the crime statistics data in South Carolina
 "South Carolina": {
        "Homicide": 0.11,
        "Robbery": 0.51,
        "Burglary": 3.73,
        "Assault": 2.84,
    },
#this information will give you all the crime statistics data in South Dakota
 "South Dakota": {
        "Homicide": 0.03,
        "Robbery": 0.21,
        "Burglary": 2.61,
        "Assault": 3.05,
    },
#this information will give you all the crime statistics data in Tennessee
 "Tennessee": {
        "Homicide": 0.10,
        "Robbery": 0.71,
        "Burglary": 3.29,
        "Assault": 5.51,
    },
#this information will give you all the crime statistics data in Texas
 "Texas": {
        "Homicide": 0.07,
        "Robbery": 0.77,
        "Burglary": 3.20,
        "Assault": 3.18,
    },
#this information will give you all the crime statistics data in Utah
 "Utah": {
        "Homicide": 0.03,
        "Robbery": 0.33,
        "Burglary": 2.27,
        "Assault": 1.60,
    },
#this information will give you all the crime statistics data in Vermont
 "Vermont": {
        "Homicide": 0.02,
        "Robbery": 0.10,
        "Burglary": 1.77,
        "Assault": 1.35,
    },
#this information will give you all the crime statistics data in Virginia
 "Virginia": {
        "Homicide": 0.07,
        "Robbery": 0.34,
        "Burglary": 1.23,
        "Assault": 1.55,
    },
#this information will give you all the crime statistics data in Washington
 "Washington": {
        "Homicide": 0.04,
        "Robbery": 0.74,
        "Burglary": 5.19,
        "Assault": 2.20,
    },
#this information will give you all the crime statistics data in West Virginia 
 "West Virginia": {
        "Homicide": 0.07,
        "Robbery": 0.61,
        "Burglary": 2.88,
        "Assault": 2.84,
    },
#this information will give you all the crime statistics data in Wisconsin
 "Wisconsin": {
        "Homicide": 0.06,
        "Robbery": 0.46,
        "Burglary": 1.73,
        "Assault": 2.30,
    },
#this information will give you all the crime statistics data in Wyoming
 "Wyoming": {
        "Homicide": 0.05,
        "Robbery": 0.14,
        "Burglary": 2.76,
        "Assault": 1.52,
    },
#All the statistics have been tracked now we are going to create our definitions so this information is defined within the code.
def get_crime_statistics(state):
    state = state.capitalize()  # Capitalize the state name
    if state in crime_data:
        return crime_data[state]
    else:
        return None  # State not found in the data
#Now we have the main code that will prompt the user on what they need to do.
while True:
    state = input("Enter a state (or 'exit' to quit): ")
    
    if state.lower() == 'exit':
        break
    
    crime_stats = get_crime_statistics(state)
    
    if crime_stats is not None:
        print(f"Crime statistics for {state}:")
        for crime, count in crime_stats.items():
            print(f"{crime}: {count}")
    else:
        print(f"Crime statistics for {state} not found.")
print("Goodbye!")
#The code has been completed.