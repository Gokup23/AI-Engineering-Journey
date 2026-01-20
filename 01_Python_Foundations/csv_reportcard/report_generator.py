import csv

def generate_reportcard():
    try:
        with open("student_marks.csv", 'r') as infile:
            reader = csv.DictReader(infile)
            with open("output_file.csv", 'w') as outfile:
                fieldnames = ['Name', 'Math', 'Science', 'English', 'Total', 'Average', 'Grade']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    name = row['Name']
                    try:
                        math = int(row['Math'])
                    except ValueError:
                        math = 0
                    try:
                        science = int(row['Science'])
                    except ValueError:
                        science = 0
                    try:
                        english = int(row['English'])
                    except ValueError:
                        english = 0
                    total = math + science + english
                    average = total / 3
                    if average >= 90:
                        grade = 'A'
                    elif average >= 80:
                        grade = 'B'
                    elif average >= 70:
                        grade = 'C'
                    elif average >= 60:
                        grade = 'D'
                    else:
                        grade = 'F'
                    
                    writer.writerow({
                        'Name': name,
                        'Math': math,
                        'Science': science,
                        'English': english,
                        'Total': total,
                        'Average': f"{average:.2f}",
                        'Grade': grade
                    })
                
    except FileNotFoundError:
        print(f"Error: The file  was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Easter_egg: 1 percent better every day!")

if __name__ == "__main__":
    generate_reportcard()