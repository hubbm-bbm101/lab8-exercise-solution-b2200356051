import sys
textFile =sys.argv[1]
names = sys.argv[2]

students = {}
with open(textFile, "r", encoding="utf-8") as file:
    for line in (file.readlines()):
        students[line.split(":")[0]] = [(line.split(":")[1].split(",")[0]),((line.split(":")[1].split(",")[1])).strip("\n")]


for student in names.split(","):
    try:
        print("Name: ", student,",", students[student][0],",", students[student][1], "departmant")
    except:
        print(f"No record of {student} found!")