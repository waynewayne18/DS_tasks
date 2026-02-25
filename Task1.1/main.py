import re
from operator import index
import pandas as pd
import csv

marks = pd.read_csv("activity1_1_marks.csv", header = None)
modules = pd.read_csv("cs_modules.csv", header = None)

failed = 0
final_score = 0

def mark_decider(row_index):
    module_to_code = {
        "UFCFHS-30-1": "Principles of Programming",
        "UFCFFS-30-1": "Foundations of Computing",
        "UFCFES-30-1": "Web Development&Database",
        "UFCFDS-15-1": "Computer Systems Architecture",
        "UFCFGS-15-1": "Artificial Intelligence I",
        "UFCFWK-15-2": "Operating Systems",
        "UFCFYR-15-2": "Advanced Algorithms",
        "UFCF7S-30-2": "Systems Development",
        "UFCF8S-30-2": "Advanced SW Development",
        "UFCF9S-15-2": "Artificial Intelligence II",
        "UFCFVK-15-2": "Internet of Things",
        "UFCFAS-15-2": "Machine Learning",
        "UFCFBS-15-2": "Embedded Systems Programming",
        "UFCFCS-30-2": "Digital Design",
        "UFCFXK-30-3": "Digital Systems Project",
        "UFCFTR-30-3": "Distributed&Enterprise SW Development",
        "UFCFE6-15-3": "Professional Experience",
        "UFCFU3-15-3": "Advanced Databases",
        "UFCFWR-15-3": "Advanced Systems Programming",
        "UFCF7H-15-3": "Mobile Applications",
        "UFCFUR-15-3": "Advanced Artificial Intelligence",
        "UFCFVR-15-3": "Communications and Protocols",
        "UFCFEL-15-3": "Security Data Analytics & Visualisation",
        "UFCFXR-15-3": "Autonomous Agents and Multi-Agent Systems"
}
    y2_acumulated_creds = 0 #acumulated creds in top modules, year 2
    y3_acumulated_creds = 0
    y2_avg_mark = 0 
    y3_avg_mark = 0
    total_mark = 0
    year2_modules = [] 
    row_marks = marks.iloc[row_index, 2::2]
    row_unit = marks.iloc[row_index, 1::2]
    #instead of working through index makes code more modular in case new module gets added or removed.
    for i in range(0, len(row_marks)): #going through all marks 
        if row_marks.iloc[i] < 40:
            failed == 1

        if int(re.search(r"-(\d+)$", row_unit.iloc[i]).group(1)) == 2: #regex for year
            #credits : marks
            year2_modules.append([int(re.search(r"-(\d+)-", row_unit.iloc[i]).group(1)), row_marks.iloc[i]])

        elif re.search(r"-(\d+)$", row_unit.iloc[i]).group(1) == "3":
            y3_acumulated_creds += int(re.search(r"-(\d+)-", row_unit.iloc[i]).group(1)) #different regex for creds
            y3_avg_mark += (int(re.search(r"-(\d+)-", row_unit.iloc[i]).group(1)) * row_marks.iloc[i])
        with open('output.txt', 'a') as file:
            file.write(module_to_code[row_unit.iloc[i]] + ", " +  row_unit.iloc[i] + ", mark: " + str(row_marks.iloc[i]) + "\n")

    sorted_year2_modules = sorted(year2_modules, key=lambda item: item[1], reverse=True)
    for creds, mark in sorted_year2_modules:
        y2_acumulated_creds += creds
        if y2_acumulated_creds <= 100: #best credits as long as under or 100
            y2_avg_mark += (creds * mark)
        if y2_acumulated_creds > 100:
            break

    y2_avg_mark = y2_avg_mark / (y2_acumulated_creds - creds)
    y3_avg_mark = y3_avg_mark / y3_acumulated_creds
    total_mark = ((y3_avg_mark * 3) + y2_avg_mark) / 4
    y2_avg_mark = 0
    y3_avg_mark = 0
    return total_mark, failed

for i in range(0,len(marks)):
    with open('output.txt', 'a') as file:
        file.write("Student number " + str(i) + ":" + "\n")
    final_score, failed = mark_decider(i)
    with open('output.txt', 'a') as file:
        file.write("Final score is " + str(final_score)+ "\n")

        if final_score < 40:
            file.write("Student failed\n")
            file.write("Reason: Final score is less than 40\n")

        elif failed == 1:
            file.write("Student failed\n")
            file.write("Reason: Student has at least one module mark less than 40\n")
            failed = 0

        elif final_score >= 40 and final_score < 50:
            file.write("Student passed with a 3rd class\n")

        elif final_score >= 50 and final_score < 60:
            file.write("Student passed with a 2:2\n")
        
        elif final_score >= 60 and final_score < 70:
            file.write("Student passed with a 2:1!\n")
        
        elif final_score >= 70:
            file.write("Student passed with a 1st!\n")
        
        file.write("----------------------------------------------------------------------------- \n")

 