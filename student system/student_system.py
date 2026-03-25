class Student():

    def __init__(self, name, age, note):

        self.name = name
        self.age = age
        self.note = note


    def set_name(self, name):

        self.name = name

    def get_name(self):

        return self.name
    
    def set_age(self, age):

        self.age = age

    def get_age(self):

        return self.age
    
    def set_note(self, note):

        self.note = note
    
    def get_note(self):

        return self.note
    

def main():

    students = []

    while True:

        print("\n")
        print("1. Add a new student.")
        print("2. Change the grade of an existing student.")
        print("3. See informations of an student")
        print("4. List of students")
        print("5. Leave the program.")
        print("\n")
        choose = input("Choose one option")

        if choose == '1':

            name = input("Digit the student name: ")

            age = input("Digit the student age: ")

            note = input("Digit the student grade: ")

            new_student = Student(name, age, note)

            students.append(new_student)

            print(f"student {name} added with success.")

        
        elif choose == '2':

            name = ("Digit the name of the student you want to change the note: ")

            for student in students:

                if student.get_name() == name:

                    new_note = float(input("Digit the new note: "))

                    student.set_note(new_note)

                    print("Note chaged with success.")

                    break
                
                else:
                    print("Student not founded.")

        elif choose == '3':

                name = input("Digit the name of the student you want to see the informations.")

                for student in students:

                    if student.get_name() == name:

                        print(f"Name: {name} | Age: {age} | Grade: {note}")

                        break

                    else:
                        print("Student not founded.")

        elif choose == '4':

            for student in students:

                print(f"Name: {student.get_name()} | Age: {student.get_age()} | Grade: {student.get_note()}")


        elif choose == '5':

            print("You leave the program.")

            break
            
        else:
            print("Invalid option.")


main()