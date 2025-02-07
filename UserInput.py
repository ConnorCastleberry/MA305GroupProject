# This is the user input section of the code
# Max Wilson made this portion
# Last updated: 4/5/22

import numpy as np
import matplotlib.pyplot as plt

def userInput():
    optionPick = input("Would you like to review vaccine(s) percentages (1), hospitalizations per state (2), "
                       "or current percentage of those COVID-19? (3)")
    match optionPick:
        case "1":
            vaccineType = input("Please enter the name of the vaccine you would like to review (Moderna, J&J or Pfizer): ")
            print("Vaccine Type: " + vaccineType)
            if vaccineType == ("Moderna", "Pfizer", "J&J"):
                dateRange = input("Please enter a date range for the following data you have requested: ")
                print("Date Range: " + dateRange)
                print("Would you like to compare another vaccine against the one you have chosen? ")
                compareVaccine = input("Please enter yes or no: ")
                print("Answer: ", compareVaccine)
                if compareVaccine == "Yes" or compareVaccine == "yes":
                    vaccineType2 = input("Please enter the other vaccine you'd like to compare: ")
                    print("You will be comparing " + vaccineType + vaccineType2)
                    if vaccineType == "Moderna" and vaccineType2 == "J&J":
                        # pull info of both from excel sheet through the date range
                    elif vaccineType == "Moderna" and vaccineType2 == "Pfizer":
                        # moderna and pfizer info
                    elif vaccineType == "J&J" and vaccineType2 == "Pfizer":
                        # Pfizer and J&J
                    # display graph and save info to new CSV
                    else:
                        print("You cannot compare the same vaccine type. Please try again. ")
                        print(vaccineType)
                        print(vaccineType2)
                        print(dateRange)
                else:
                    if vaccineType == "Moderna":
                        # pull info from excel sheet about moderna through the given date range
                    elif vaccineType == "J&J":
                        # pull info on J&J through the given date range
                    elif vaccineType == "Pfizer":
                        # pull info on Pfizer through the given date range
                        # display graph and save info to new CSV
            else:
                print("Please enter a valid vaccine name. ")
                # restart portion of code
            return vaccineType, dateRange, compareVaccine, vaccineType2, None, None
        case "2":
            hospitalStateNumbers = input("Please enter which state you would like to review: ")
            print("State chosen: ", hospitalStateNumbers)
            hstateNums(hospitalStateNumbers)
        case "3":
            dateRange = input("Please enter a date: ")
            print("Date Range: " + dateRange)
            print("The total average percentage of the population that had COVID-19 for the following dates are: " + avg())
            print("See the graph below for a more detailed breakdown by month.")
            # display graph of data
            # make x and y arrays
            # figure out how to map the date range to an array
            # plt.plot(x, y, color='red', marker='o', markerface='blue', markersize=12)
            plt.ylim(1, 100)
            plt.xlim('January', 'December')  # month
            plt.xlabel('Month')
            plt.ylabel('Percentage of population with covid')
            plt.title('Percentage of population with COVID-19 per Month')
            plt.show()

            #save info to new CSV

def avg(num):
    sum = 0
    for t in num:
        sum = sum + t
    average = sum / len(num)
    return average


def hstateNums(hospitalStateNumbers):
    # pull info from excel depending on state
    # maybe make an array and have it go through each row until it find the correct one
