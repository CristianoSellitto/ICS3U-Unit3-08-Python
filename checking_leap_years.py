#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if the chosen year is a leap year or not


def main():
    # Finds if a the chosen year is a leap year or not

    year = input("Enter a year: ")
    try:
        year_int = int(year)
        if year_int > 0:
            if year_int % 4 == 0:
                if year_int % 100 == 0:
                    if year_int % 400 == 0:
                        print("\n{} is a leap year.".format(year_int))
                    else:
                        print("\n{} is a common year.".format(year_int))
                else:
                    print("\n{} is a leap year.".format(year_int))
            else:
                print("\n{} is a common year.".format(year_int))
        else:
            print("\n{} is not in the common era.".format(year_int))
    except ValueError:
        print("\nError: {} is not an integer.".format(year))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
