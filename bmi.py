#Body Mass Index
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    Get the BMI category based on the BMI value.

    :param bmi: BMI value
    :return: BMI category (Underweight, Normal, Overweight, Obese)
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {bmi_category}")

if __name__ == "__main__":
    main()