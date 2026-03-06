# Grade Calculator Script
try:
    while True:
        # Ask for student's name
        name = input("Enter the student's name (or 'Exit' to quit): ")
        if name.lower() == 'exit':
            break

        # Ask for 3 subject marks
        mark1 = float(input("Enter mark for subject 1: "))
        mark2 = float(input("Enter mark for subject 2: "))
        mark3 = float(input("Enter mark for subject 3: "))

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        # Assign grade based on average
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print("------------------------------")
        print(f"Name   : {name}")
        print(f"Average: {average:.2f}")
        print(f"Grade  : {grade}")
        print("------------------------------")
except:
    print("Please enter valid numeric values for the marks.")