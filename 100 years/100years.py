import datetime


def main():
    name = input("Enter your Name: ")

    age = input("Enter your age: ")
    age = int(age)

    time = year() - age + 100

    print(name + ", you will be 100 years old in the year " + str(time))


def year():

    today = datetime.date.today()

    return today.year


# year()
main()
