Maths=int(input("Enter the marks obtained in Maths: "))
Science=int(input("Enter the marks obtained in Science: "))
Hindi=int(input("Enter the marks obtained in Hindi: "))
English=int(input("Enter the marks obtained in English: "))

Total_Marks=Maths+Science+Hindi+English
Percentage=(Total_Marks/400)*100
print("The percentage of the student is:", Percentage)
print(f'The total marks obtained by the student is: {Total_Marks}')