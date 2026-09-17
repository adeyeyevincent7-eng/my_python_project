from datetime import datetime

entry = input("Enter your journal entry: ")

with open("journal.txt", "a") as file:
    time = datetime.now()
    file.write(f"{time}: {entry}\n")

print("\nPrevious journal entries:")

with open("journal.txt", "r") as file:
    print(file.read())