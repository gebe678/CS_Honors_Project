import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filelocation = "../../../data/example csv/annual-enterprise-survey-2020-financial-year-provisional-csv.csv"
filelocation = "../../../data/html_files/College of Liberal Arts Schedule of Classes Fall 2018.csv"

def read_csv(file = filelocation):

    with open(file , newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = " ")

        for row in reader:
            print(row)

def read_csv_pandas(file = filelocation):
    
    df = pd.read_csv(file)
    departments = list(df["Department"])
    status = list(df["Status"])
    course_title = list(df["Course Title"])
    instructor = list(df["Instructor"])

    for i in range(len(departments)):
        print(departments[i] + " " + status[i] + " " + course_title[i] + " " + instructor[i])

    # dictionary that holds an instructors name as the key and the number of classes they teach as the value
    instructor_to_classes = {}
    for i in range(len(instructor)):

        if instructor[i] not in instructor_to_classes:
            instructor_to_classes[instructor[i]] = 1
        else:
            instructor_to_classes[instructor[i]] += 1

    figure = plt.figure()
    ax = figure.add_axes([0,0,1,1])
    labels = list(instructor_to_classes.keys())
    num_classes = []
    for i in labels:
        num_classes.append(instructor_to_classes[i])

    ax.bar(labels, num_classes)
    plt.show()

    # data = list(df["Value"])
    # for i in range(len(data)):
    #     data[i] = data[i].replace(",", "")
    #     data[i] = float(data[i])

    # data.sort()
    # print(data)
    
    # plt.plot(data)
    # plt.show()

if __name__ == "__main__":

    read_csv_pandas()