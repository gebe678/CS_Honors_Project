import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import statistics

from student import Student
from class_registration import Registration

def read_csv_data(files):
    """
    This function is responsible for getting all of the data to be modeled as dataframes.
    """
    data_frames = []

    # go through all of the files and create dataframes from the csv's
    for file in files:
        data_frames.append(pd.read_csv(file))

    return data_frames

def create_class_registration_objects(data):
    registration_dict = {}
    registration_classes = data[1]

    # replace the nan values in the dataframe with NaN (type string)
    for (columnName, columnValues) in registration_classes.iteritems():
        registration_classes[columnName].fillna("NaN", inplace=True)

    for i in range(len(registration_classes.index)):

        data = registration_classes.loc[i]
        
        reg = Registration()

        reg.set_term_code(data["Term_Code"])
        reg.set_crn_key(data["CRN_Key"])
        reg.set_subject_code(data["SUBJ_CODE"])
        reg.set_course_number(data["CRSE_NUMB"])
        reg.set_section_number(data["Section Number"])
        reg.set_credit_hours(data["CREDIT_HRS"])

        if reg not in registration_dict:
            registration_dict[reg.get_crn_key(),reg.get_term_code()] = reg

    return registration_dict

def create_student_objects(data):
    """
    This function is responsible for creating student objects for easy data gathering
    """
    students = []
    classes = create_class_registration_objects(data)

    student_course_data = data[0]

    # change the nan values to NaN string type to remove them
    for (columnName, columnValues) in student_course_data.iteritems():
        student_course_data[columnName].fillna("NaN", inplace=True)

    # loop through every row in the dataframe
    for i in range(len(student_course_data.index)):

        # save the current row into a data variable
        data = student_course_data.loc[i]
        initial_classes = []
        registered_classes = []

        # create a student object
        student = Student()

        # set the students unique id
        student.set_student_id(data["Student_key"])
        student.set_term(data["Term"])

        # get the intial classes from the row
        if data["Reg_Jul15_Course__1"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__1"],student.get_term()])
        if data["Reg_Jul15_Course__2"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__2"],student.get_term()])
        if data["Reg_Jul15_Course__3"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__3"],student.get_term()])
        if data["Reg_Jul15_Course__4"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__4"],student.get_term()])
        if data["Reg_Jul15_Course__5"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__5"],student.get_term()])
        if data["Reg_Jul15_Course__6"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__6"],student.get_term()])
        if data["Reg_Jul15_Course__7"] != "NaN": initial_classes.append(classes[data["Reg_Jul15_Course__7"],student.get_term()])

        # get the registered classes from the row
        if data["Reg_15days_after_start_of_term_Course_1"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_1"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_2"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_2"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_3"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_3"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_4"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_4"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_5"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_5"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_6"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_6"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_7"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_7"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_8"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_8"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_9"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_9"],student.get_term()])
        if data["Reg_15days_after_start_of_term_Course_10"] != "NaN" : registered_classes.append(classes[data["Reg_15days_after_start_of_term_Course_10"],student.get_term()])

        # add revelant course information to the student object
        student.add_classes(initial_classes, registered_classes)

        # add the student to a list of student objects
        students.append(student)

    # return all of the students for analysis
    return students

def calculate_class_percentages(files):
    """
    This function calculates the percentage of students who dropped a class and the percentage of classes students kept with and without the rcc classes
    """
    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames)

    # every entry is a student and each number represents the number of classes dropped
    dropped_classes_list  = []
    kept_classes_list_rcc = []
    kept_classes_list_no_rcc = []
    faculity_chosen_class_percentage = []
    students_dropped_classes = 0
    total_students = len(students)

    for student in students:
        # calcualte number of dropped classes
        dropped_classes = student.calculate_dropped_classes()

        # calculate number of kept classes percentage with rcc
        kept_classes_rcc = student.calculate_kept_class_percentage(True)

        # calculate number of kept classes percentage without rcc
        kept_classes_no_rcc = student.calculate_kept_class_percentage(False)

        dropped_classes_list.append(dropped_classes)
        kept_classes_list_rcc.append(kept_classes_rcc)
        kept_classes_list_no_rcc.append(kept_classes_no_rcc)
        faculity_chosen_class_percentage.append(student.calculate_faculity_chosen_classes())
        
        if dropped_classes > 0:
            students_dropped_classes += 1
    
    print("dropped class percentage: ", students_dropped_classes / total_students)
    print("kept classes percentage with RCC ", statistics.mean(kept_classes_list_rcc))
    print("kept classes percentage without RCC ", statistics.mean(kept_classes_list_no_rcc))
    print("Faculity chosen class percentage: ", statistics.mean(faculity_chosen_class_percentage))

# This function is responsible for calculating the number of credit hours a student was registered for
# before and after registration
def calculate_credit_hours(files):
    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames)

    credit_hours_pre = []
    credit_hours_post = []

    for student in students:
        credit_hours_pre.append(student.calculate_credit_hours_pre())
        credit_hours_post.append(student.calculate_credit_hours_post())

    # pre schedule change histogram
    plt.figure(0)
    plt.hist(credit_hours_pre, bins=20)
    plt.xlabel("Number of Credit Hours")
    plt.ylabel("Frequency")
    plt.title("Number of Credit Hours Pre Schedule Change")
    plt.savefig("credit_hours_pre_hist.pdf", bbox_inches="tight")

    # post schedule change histogram
    plt.figure(1)
    plt.hist(credit_hours_post, bins=20)
    plt.xlabel("Number of Credit Hours")
    plt.ylabel("Frequency")
    plt.title("Number of Credit Hours Post Schedule Change")
    plt.savefig("credit_hours_post_hist.pdf", bbox_inches="tight")

    print("credit hour graph saved")

# This function is responsible for calculating the number of dropped classes for every student
def calculate_dropped_classes(files):
    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames)

    dropped_class_ratio = []

    for student in students:
        registered_classes = student.get_registered_classes()
        dropped_classes = student.calculate_dropped_classes()

        if registered_classes > 0:
            dropped_class_ratio.append(dropped_classes / registered_classes)

    plt.figure(0)
    plt.hist(dropped_class_ratio, bins=20)
    plt.xlabel("Number of dropped classes")
    plt.ylabel("Frequency")
    plt.title("Number of dropped classes")
    plt.savefig("num_dropped_classes_per_student_hist.pdf")

    print("dropped classes graph saved")

def run_class_percentages(files, startyear, endyear):
    print(startyear, " ", endyear)
    calculate_class_percentages(files)

def run_credit_hours(files, startyear, endyear):
    print(startyear, " ", endyear)
    calculate_credit_hours(files)

def run_dropped_classes(files, startyear, endyear):
    print(startyear, " ", endyear)
    calculate_dropped_classes(files)

def main(files):
    #calculate_class_percentages(files)
    #calculate_credit_hours(files)
    #calculate_dropped_classes(files)
    run_dropped_classes(files)

if __name__ == "__main__":

    if len(sys.argv) > 2:
        files = sys.argv[1:]
        main(files)

    else:
        main(["../../../../data/Registration Data/Freshmen Registration Changes _ per student layout.csv","../../../../data/Registration Data/Freshmen Registration with Change Status.csv"])
        