with open("sales.txt", "r") as file:
    lines = file.readlines()
# Skip the header (first line)
for line in lines[1:]:
    line = line.strip()
product, price, quantity = line.split(",")
price = int(price)
quantity = int(quantity)
total_value = price * quantity
print(f"{product}: ₦{total_value:,}")
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
