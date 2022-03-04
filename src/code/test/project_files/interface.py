import tkinter as tk

from numpy import row_stack
import driver

def getFiles():
    files = []
    input_file_path = open("file_paths.txt", "r")
        
    for input_files in input_file_path:
        files.append(input_files.strip())

    return files

def runClassPercentages(startyear, endyear):
    files = getFiles()
    driver.run_class_percentages(files, startyear, endyear)

def runCreditHours(startyear, endyear):
    files = getFiles()
    driver.run_credit_hours(files, startyear, endyear)

def runDroppedClasses(startyear, endyear):
    files = getFiles()
    driver.run_dropped_classes(files, startyear, endyear)

def runDroppedClassSubjectDistribution(startyear, endyear):
    files = getFiles()
    driver.run_dropped_class_subject_distribution(files, startyear, endyear)

def runDroppedClassCompetency(startyear, endyear):
    files = getFiles()
    driver.run_dropped_class_competency(files, startyear, endyear)

# main function
def main():
    # create the window
    window = tk.Tk()
    window.title("CS Honors Project")

    # create frame for the year
    yearFrame = tk.Frame(master=window)
    buttonFrame = tk.Frame(master=window)

    yearFrame.grid(row=0, column=0)
    buttonFrame.grid(row=0, column=1)

    # create an option menu for the first dropdown
    startYearVar = tk.IntVar(window)
    startYearChoices = {2017, 2018, 2019, 2020, 2021}
    startYearVar.set(2017)

    # create an option menu for the second dropdown
    endYearVar = tk.IntVar(window)
    endYearChoices = {2017, 2018, 2019, 2020, 2021}
    endYearVar.set(2018)
    
    # get the start year from the user
    startYearLabel = tk.Label(master=yearFrame, text="Select a start year:")
    startYearLabel.grid(row=0, column=0)
    # create the popup menu
    startYear = tk.OptionMenu(yearFrame, startYearVar, *startYearChoices)
    startYear.grid(row =0, column=1)

    # get the end year from the user
    endYearLabel = tk.Label(master=yearFrame, text="Enter an end year:")
    endYearLabel.grid(row=1, column=0)
    #create the popup menu
    endYear = tk.OptionMenu(yearFrame, endYearVar, *endYearChoices)
    endYear.grid(row=1, column=1)

    # create the class percentage button button
    classPercentageButton = tk.Button(master=buttonFrame, text="Calculate Class Percentages", width=30, command=lambda: runClassPercentages(startYearVar.get(), endYearVar.get()))
    classPercentageButton.grid(row=0, column=0)
    #classPercentageButton.bind("<Button-1>", runClassPercentages)

    # create the credit hour button
    creditHourButton = tk.Button(master=buttonFrame, text="Calculate Credit Hours", width=30, command=lambda: runCreditHours(startYearVar.get(), endYearVar.get()))
    creditHourButton.grid(row=1, column=0)
    #creditHourButton.bind("<Button-1>", runCreditHours)

    # create the dropped class button
    droppedClassesButton = tk.Button(master=buttonFrame, text="Calculate Dropped Classes", width=30, command=lambda: runDroppedClasses(startYearVar.get(), endYearVar.get()))
    droppedClassesButton.grid(row=2, column=0)
    #droppedClassesButton.bind("<Button-1>", runDroppedClasses)

    class_subject_distribution_button = tk.Button(master=buttonFrame, text="Calculate Subject Distributions", width=30, command=lambda: runDroppedClassSubjectDistribution(startYearVar.get(), endYearVar.get()))
    class_subject_distribution_button.grid(row=3, column=0)

    class_competency_distribution_button = tk.Button(master=buttonFrame, text="Calculate Competency Distributions", width=30, command=lambda: runDroppedClassCompetency(startYearVar.get(), endYearVar.get()))
    class_competency_distribution_button.grid(row=4, column=0)
    # run the event loop
    window.mainloop()

if __name__ == "__main__":
    main()