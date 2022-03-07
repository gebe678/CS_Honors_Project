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
        data_frames.append(pd.read_csv(file, encoding = "unicode_escape"))

    return data_frames

def create_class_registration_objects(data):
    registration_dict = {}
    competency_dict = {}
    year_list = [np.int64(201709), np.int64(201809), np.int64(201909), np.int64(202009), np.int64(202109)]
    registration_classes = data[1]

    not_found_class_list = []

    for i in range(2,len(data)):
        competency_data = data[i]

        for (columnName, columnValues) in competency_data.iteritems():
            competency_data[columnName].fillna("NONE", inplace=True)

        for j in range(len(competency_data.index)):

            comp_data = competency_data.loc[j]
            crn_number = np.int64(comp_data["Course"].split(" ")[0])
            competency = comp_data["Competency/GenEd"]
            key = crn_number,year_list[i - 2]

            competency_dict[key] = competency
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

        if (reg.get_crn_key(),reg.get_term_code()) in competency_dict:
            reg.set_competency(competency_dict[reg.get_crn_key(), reg.get_term_code()])
        else:
            reg.set_competency("NOT FOUND")

            if "Course crn_key: " + str(reg.get_crn_key()) + " term code " + str(reg.get_term_code()) + " Subject Dist: " + str(reg.get_subject_code()) + " NOT FOUND" not in not_found_class_list:
                not_found_class_list.append("Course crn_key: " + str(reg.get_crn_key()) + " term code " + str(reg.get_term_code()) + " Subject Dist: " + str(reg.get_subject_code()) + " NOT FOUND")

        if reg not in registration_dict:
            registration_dict[reg.get_crn_key(),reg.get_term_code()] = reg

    for item in not_found_class_list:
        print(item)

    return registration_dict

def create_student_objects(data, startyear, endyear):
    """
    This function is responsible for creating student objects for easy data gathering
    """
    students = []
    classes = create_class_registration_objects(data)

    startyear = str(startyear) + "09"
    endyear = str(endyear) + "09"

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

        # check to make sure the term is greater equal to the start term and less than the end term
        if str(data["Term"]) >= startyear and str(data["Term"]) <= endyear:

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

            # remove all classes that have less than 2 credit hours from the initial classes
            for course in initial_classes:
                if str(course.get_credit_hours()).isdigit() and int(course.get_credit_hours()) < 4 and course in initial_classes:
                    initial_classes.remove(course)
            
            # remove all classes that have less than 2 credit hours from the registered classes
            for course in registered_classes:
                if course.get_credit_hours != "NaN" and int(course.get_credit_hours()) < 4 and course in registered_classes:
                    registered_classes.remove(course)

            # add revelant course information to the student object
            student.add_classes(initial_classes, registered_classes)

            # add the student to a list of student objects
            students.append(student)

    # return all of the students for analysis
    return students

def calculate_class_percentages(files, startyear, endyear):
    """
    This function calculates the percentage of students who dropped a class and the percentage of classes students kept with and without the rcc classes
    """
    # if the endyear is smaller than the start year flip them
    if endyear < startyear:
        s = endyear
        endyear = startyear
        startyear = s

    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames, startyear, endyear)

    # every entry is a student and each number represents the number of classes dropped
    dropped_classes_list  = []
    kept_classes_list_rcc = []
    kept_classes_list_no_rcc = []
    faculity_chosen_class_percentage = []
    faculity_chosen_class_percentage_no_rcc = []
    students_dropped_classes = 0
    total_students = len(students)

    for student in students:
        # calcualte number of dropped classes
        dropped_classes = student.calculate_dropped_classes()

        # calculate number of kept classes percentage with rcc
        kept_classes_rcc = student.calculate_kept_class_percentage(True)

        # calculate number of kept classes percentage without rcc
        kept_classes_no_rcc = student.calculate_kept_class_percentage(False)

        # calculate number of faculity chosen class percentage with rcc
        faculity_chosen_class = student.calculate_faculity_chosen_classes(True)

        # calculate number of faculity chosen class percentage without rcc
        faculity_chosen_class_no_rcc = student.calculate_faculity_chosen_classes(False)

        dropped_classes_list.append(dropped_classes)
        kept_classes_list_rcc.append(kept_classes_rcc)
        kept_classes_list_no_rcc.append(kept_classes_no_rcc)
        faculity_chosen_class_percentage.append(faculity_chosen_class)
        faculity_chosen_class_percentage_no_rcc.append(faculity_chosen_class_no_rcc)

        if dropped_classes > 0:
            students_dropped_classes += 1
    
    print("For years: ", startyear, "-", endyear)
    print("dropped class percentage: ", students_dropped_classes / total_students)
    print("dropped class percentage numbers: ", "num students dropped classes: ", students_dropped_classes, " total students: ", total_students)
    print("kept classes percentage with RCC ", statistics.mean(kept_classes_list_rcc))
    print("kept classes percentage without RCC ", statistics.mean(kept_classes_list_no_rcc))
    print("Faculity chosen class percentage with RCC: ", statistics.mean(faculity_chosen_class_percentage))
    print("Faculity chosen class percentage without RCC: ", statistics.mean(faculity_chosen_class_percentage_no_rcc))

    # create histograms for the data
    # kept class list percentage histogram
    # plt.figure(0)
    # plt.hist(kept_classes_list_rcc, bins=20)
    # plt.xlabel("Percentage of kept classes with RCC")
    # plt.ylabel("Number of students")
    # if startyear != endyear:
    #     plt.title("Percentage of kept classes with RCC for: " + str(startyear) + "-" + str(endyear))
    # else:
    #     plt.title("Percentage of kept classes with RCC for: " + str(startyear))

    # #plt.legend(loc="upper left", prop={"size": "10"})
    # if startyear == endyear:
    #     plt.ylim(0,300)
    # plt.show()

    # # pre schedule change histogram
    # plt.figure(1)
    # plt.hist(kept_classes_list_no_rcc, bins=20)
    # plt.xlabel("Percentage of kept classes without RCC")
    # plt.ylabel("Number of students")
    # if startyear != endyear:
    #     plt.title("Percentage of kept classes without RCC for: " + str(startyear) + "-" + str(endyear))
    # else:
    #     plt.title("Percentage of kept classes without RCC for: " + str(startyear))

    # #plt.legend(loc="upper left", prop={"size": "10"})
    # if startyear == endyear:
    #     plt.ylim(0,300)
    # plt.show()

    # # pre schedule change histogram
    # plt.figure(2)
    # plt.hist(faculity_chosen_class_percentage, bins=20)
    # plt.xlabel("Percentage of faculity chosen classes")
    # plt.ylabel("Number of students")
    # if startyear != endyear:
    #     plt.title("Percentage of faculity chosen classes for: " + str(startyear) + "-" + str(endyear))
    # else:
    #     plt.title("Percentage of faculity chosen classes for: " + str(startyear))

    # #plt.legend(loc="upper left", prop={"size": "10"})
    # if startyear == endyear:
    #     plt.ylim(0,300)
    # plt.show()
    

# This function is responsible for calculating the number of credit hours a student was registered for
# before and after registration
def calculate_credit_hours(files, startyear, endyear):

    # if the endyear is smaller than the start year flip them
    if endyear < startyear:
        s = endyear
        endyear = startyear
        startyear = s

    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames, startyear, endyear)

    credit_hours_pre = []
    credit_hours_post = []

    for student in students:
        credit_hours_pre.append(student.calculate_credit_hours_pre())
        credit_hours_post.append(student.calculate_credit_hours_post())

    # pre schedule change histogram
    plt.figure(0)
    counts, edges, bars = plt.hist([credit_hours_pre, credit_hours_post], bins=20, histtype="bar", label=["credit hours pre registration", "credit hours post registration"])
    plt.xlabel("Number of Credit Hours")
    plt.ylabel("Number of students")
    if startyear != endyear:
        plt.title("Number of Credit Hours Pre and Post Schedule Change for: " + str(startyear) + "-" + str(endyear))
    else:
        plt.title("Number of Credit Hours Pre and Post Schedule Change for: " + str(startyear))
    #plt.savefig("credit_hours_pre_hist.pdf", bbox_inches="tight")

    # post schedule change histogram
    # plt.figure(0)
    # plt.hist(credit_hours_post, bins=20, histtype="bar")
    # plt.xlabel("Number of Credit Hours")
    # plt.ylabel("Frequency")
    #if startyear != endyear:
    #     plt.title("Number of Credit Hours Post Schedule Change for: " + str(startyear) + "-" + str(endyear))
    # else:
    #     plt.title("Number of Credit Hours Post Schedule Change for: " + str(startyear))
    for bar in bars:
        plt.bar_label(bar, fontsize=5)
    plt.legend(loc="upper left", prop={"size": "10"})
    if startyear == endyear:
        plt.ylim(0,360)
    plt.show()
    #plt.savefig("credit_hours_post_hist.pdf", bbox_inches="tight")

    print("credit hour graph saved")

# This function is responsible for calculating the number of dropped classes for every student
def calculate_dropped_classes(files, startyear, endyear):

    # if the endyear is smaller than the start year flip them
    if endyear < startyear:
        s = endyear
        endyear = startyear
        startyear = s

    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames, startyear, endyear)

    dropped_class_ratio = []

    for student in students:
        registered_classes = student.get_registered_classes()
        dropped_classes = student.calculate_dropped_classes()

        if registered_classes > 0:
            dropped_class_ratio.append((dropped_classes / registered_classes) * 100)

    plt.figure(0)
    counts, edges, bars = plt.hist(dropped_class_ratio, bins=20)
    plt.bar_label(bars)
    plt.xlabel("Percentage of dropped classes")
    plt.ylabel("Number of students")
    if startyear != endyear:
        plt.title("Number of dropped classes for: " + str(startyear) + "-" + str(endyear))
    else:
        plt.title("Number of dropped classes for: " + str(startyear))

    #plt.legend(loc="upper left", prop={"size": "10"})
    if startyear == endyear:
        plt.ylim(0,400)
    plt.show()
    #plt.savefig("num_dropped_classes_per_student_hist.pdf")

def calculate_dropped_class_subject_distribution(files, startyear, endyear):
    # if the endyear is smaller than the start year flip them
    if endyear < startyear:
        s = endyear
        endyear = startyear
        startyear = s

    dropped_classes = []
    added_classes = []
    dropped_classes_dict = {}
    added_classes_dict = {}
    yaxis_dropped = []
    yaxis_added = []
    labels = []

    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames, startyear, endyear)

    for student in students:
        dropped_classes += student.get_dropped_class_subject_code()
        added_classes += student.get_added_class_subject_code()

    for code in dropped_classes:
        if code not in labels:
            labels.append(code)

        if code not in dropped_classes_dict:
            dropped_classes_dict[code] = 0
            added_classes_dict[code] = 0

        dropped_classes_dict[code] += 1

    for code in added_classes:
        if code not in labels:
            labels.append(code)

        if code not in added_classes_dict:
            dropped_classes_dict[code] = 0
            added_classes_dict[code] = 0

        added_classes_dict[code] += 1

    labels.sort()

    for label in labels:
        yaxis_dropped.append(dropped_classes_dict[label])
        yaxis_added.append(added_classes_dict[label])

    # we have 61 different subject codes what is the best way to display them all?
    plt.figure(figsize=(12,5))
    dropped_bars = plt.bar(np.arange(len(labels)) - 0.2, yaxis_dropped, 0.4, label = "Dropped Classes")
    added_bars = plt.bar(np.arange(len(labels)) + 0.2, yaxis_added, 0.4, label= "Added Classes")

    plt.xticks(np.arange(len(labels)), labels, rotation=90)
    plt.xlabel("Subject Code")
    plt.ylabel("Number of Students")
    if startyear != endyear:
        plt.title("Subject Distribution For: " + str(startyear) + "-" + str(endyear))
    else:
        plt.title("Subject Distribution For: " + str(startyear))
    plt.legend()
    
    for bar in dropped_bars:
        yval = bar.get_height()
        plt.text(bar.get_x() - .1, yval + .2, yval, fontsize=6)

    for bar in added_bars:
        yval = bar.get_height()
        plt.text(bar.get_x() - .1, yval + .2, yval, fontsize = 6)

    plt.show()


def calculate_dropped_class_competency(files, startyear, endyear):
    # if the endyear is smaller than the start year flip them
    if endyear < startyear:
        s = endyear
        endyear = startyear
        startyear = s

    dropped_classes = []
    added_classes = []
    dropped_classes_dict = {}
    added_classes_dict = {}
    yaxis_dropped = []
    yaxis_added = []
    labels = []

    data_frames = read_csv_data(files)
    students = create_student_objects(data_frames, startyear, endyear)

    for student in students:
        dropped_classes += student.get_dropped_class_competency()
        added_classes += student.get_added_class_competency()

    for code in dropped_classes:
        if code not in labels:
            labels.append(code)

        if code not in dropped_classes_dict:
            dropped_classes_dict[code] = 0
            added_classes_dict[code] = 0

        dropped_classes_dict[code] += 1

    for code in added_classes:
        if code not in labels:
            labels.append(code)

        if code not in added_classes_dict:
            dropped_classes_dict[code] = 0
            added_classes_dict[code] = 0

        added_classes_dict[code] += 1

    for label in labels:
        yaxis_dropped.append(dropped_classes_dict[label])
        yaxis_added.append(added_classes_dict[label])

    # we have 61 different subject codes what is the best way to display them all?
    plt.figure(figsize=(12,5))
    dropped_bars = plt.bar(np.arange(len(labels)) - 0.2, yaxis_dropped, 0.4, label = "Dropped Classes")
    added_bars = plt.bar(np.arange(len(labels)) + 0.2, yaxis_added, 0.4, label= "Added Classes")

    plt.xticks(np.arange(len(labels)), labels, rotation=90)
    plt.xlabel("Competency")
    plt.ylabel("Number of Students")
    if startyear != endyear:
        plt.title("Competency Distribution For: " + str(startyear) + "-" + str(endyear))
    else:
        plt.title("Competency Distribution For: " + str(startyear))
    plt.legend()
    
    for bar in dropped_bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .2, yval, fontsize=6)

    for bar in added_bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .2, yval, fontsize = 6)

    plt.show()

def run_class_percentages(files, startyear = 2017, endyear = 2020):
    calculate_class_percentages(files, startyear, endyear)

def run_credit_hours(files, startyear = 2017, endyear = 2017):
    calculate_credit_hours(files, startyear, endyear)

def run_dropped_classes(files, startyear = 2017, endyear = 2017):
    calculate_dropped_classes(files, startyear, endyear)

def run_dropped_class_subject_distribution(files, startyear = 2018, endyear = 2018):
    calculate_dropped_class_subject_distribution(files, startyear, endyear)

def run_dropped_class_competency(files, startyear = 2017, endyear = 2017):
    calculate_dropped_class_competency(files, startyear, endyear)

def main(files):
    #run_class_percentages(files, 2017, 2020)
    #run_credit_hours(files)
    #run_dropped_classes(files)
    #run_dropped_class_subject_distribution(files)
    run_dropped_class_competency(files)

if __name__ == "__main__":

    if len(sys.argv) > 2:
        files = sys.argv[1:]
        main(files)

    else:
        files = []
        input_file_path = open("file_paths.txt", "r")
        
        for input_files in input_file_path:
            files.append(input_files.strip())

        print(files)
        main(files)
        