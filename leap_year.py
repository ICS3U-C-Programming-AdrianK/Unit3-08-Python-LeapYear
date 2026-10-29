#! /usr/bin/env python3
# Created by : Adrian Student
# Date : 28 OCT 2026
# This program asks the user for a year and then determine
# if that year is a leap year or not then display result to user


def main():
    # Get a year from the user
    year_str = input("Enter a year : ")

    # check if the year is a leap year
    try:
        year_int = int(year_str)

        if year_int % 4 == 0:
            if year_int % 100 == 0:
                if year_int % 400 == 0:
                    print("{} is a leap year".format(year_str))
                else:
                    print("{} is not a leap year".format(year_str))
            else:
                print("{} is not a leap year".format(year_str))
        else:
            print("{} is not a leap year".format(year_str))
    except ValueError:
        print("{} is not a valid year".format(year_str))
    finally:
        print("Thank you for playing !!")


if __name__ == "__main__":
    main()
