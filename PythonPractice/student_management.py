import json

FILE_NAME = "data.json"

def loadData():
    with open(FILE_NAME, "r") as f:
      data = json.load(f)
    return data

data = loadData()

def saveData(data):
    with open(FILE_NAME, "w") as f:
      data = json.dump(data, f, indent = 4)
 
def createData():
    studentID = input("Please Enter Student ID: ")

    for student in data:
      if str(student["ID"]) == studentID:
       print("The student already Exist")
       return

    name = input("Please Enter Student Name: ")
    age = int(input("Please Enter Student Age: "))

    student = {
    "ID": studentID,
    "name": name,
    "age": age
}
    data.append(student)
    saveData(data)

    print("You have Succesfully created the student Record! ")

def readData():
    if len(data) == 0:
        print("No students found!")
        return

    print("\n1. Display All Students")
    print("2. Search Student By ID")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        for student in data:
            print("----------------------")
            print("ID:", student["ID"])
            print("Name:", student["name"])
            print("Age:", student["age"])

    elif choice == "2":
        studentID = input("Enter Student ID: ")

        for student in data:
            if student["ID"] == studentID:
                print("----------------------")
                print("ID:", student["ID"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                return

        print("Student not found!")

    else:
        print("Invalid Choice!")


def updateData():
    studentID = input("Enter Student ID to Update: ")

    for student in data:
        if str(student["ID"]) == studentID:

            print("Student Found!")
            print("Current Name:", student["name"])
            print("Current Age:", student["age"])

            name = input("Enter New Name: ")
            age = input("Enter New Age: ")

            student["name"] = name
            student["age"] = age

            saveData(data)

            print("Student Updated Successfully!")
            return

    print("Student not found!")

def deleteData():
    studentID = input("Enter Student ID to Delete: ")

    for student in data:
        if str(student["ID"]) == studentID:

            data.remove(student)
            saveData(data)

            print("Student Deleted Successfully!")
            return

    print("Student not found!")

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Create Student")
    print("2. Update Student")
    print("3. Read Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        createData()

    elif choice == "2":
        updateData()

    elif choice == "3":
        readData()

    elif choice == "4":
        deleteData()

    elif choice == "5":
        print("Program Closed!")
        break

    else:
        print("Invalid Operation! Please Try Again.")
