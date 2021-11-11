import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys

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

def create_student_objects(data):
    """
    This function is responsible for creating student objects for easy data gathering
    """
    students = []

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

        # get the intial classes from the row
        if data["Reg_Jul15_Course__1"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__1"])
        if data["Reg_Jul15_Course__2"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__2"])
        if data["Reg_Jul15_Course__3"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__3"])
        if data["Reg_Jul15_Course__4"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__4"])
        if data["Reg_Jul15_Course__5"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__5"])
        if data["Reg_Jul15_Course__6"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__6"])
        if data["Reg_Jul15_Course__7"] != "NaN": initial_classes.append(data["Reg_Jul15_Course__7"])

        # get the registered classes from the row
        if data["Reg_15days_after_start_of_term_Course_1"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_1"])
        if data["Reg_15days_after_start_of_term_Course_2"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_2"])
        if data["Reg_15days_after_start_of_term_Course_3"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_3"])
        if data["Reg_15days_after_start_of_term_Course_4"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_4"])
        if data["Reg_15days_after_start_of_term_Course_5"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_5"])
        if data["Reg_15days_after_start_of_term_Course_6"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_6"])
        if data["Reg_15days_after_start_of_term_Course_7"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_7"])
        if data["Reg_15days_after_start_of_term_Course_8"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_8"])
        if data["Reg_15days_after_start_of_term_Course_9"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_9"])
        if data["Reg_15days_after_start_of_term_Course_10"] != "NaN" : registered_classes.append(data["Reg_15days_after_start_of_term_Course_10"])

        # create a student object
        student = Student()

        # set the students unique id
        student.set_student_id(data["Student_key"])

        # add revelant course information to the student object
        student.add_classes(initial_classes, registered_classes)

        # add the student to a list of student objects
        students.append(student)

    # return all of the students for analysis
    return students

def create_class_registration_objects(data):
    registration_list = []
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

        registration_list.append(reg)

    return registration_list

def main(files):
    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames)
    registration = create_class_registration_objects(data_frames)
    

if __name__ == "__main__":

    if len(sys.argv) > 2:
        files = sys.argv[1:]
        main(files)

    else:
        main(["../../../../data/Registration Data/Freshmen Registration Changes _ per student layout.csv","../../../../data/Registration Data/Freshmen Registration with Change Status.csv"])
        