# Created By: Sophie Student
# Date: May 5, 2021
# Modified By: Jedidiah
# This program asks the user for the subtotal and the tax
# percentage. It then calculates and displays the HST
# and the total.
import constants


def main():
    # get user input
    print("Please enter the subtotal just below")
    subtotal = float(input(":$"))
    # calculate the tax amount and the total with tax
    tax = subtotal * constants.TAX_RATE_ONTARIO / 100
    total = subtotal + tax

    # display the tax amount and the total with tax
    print("")
    print("You have entered a subtotal of exactly ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()

