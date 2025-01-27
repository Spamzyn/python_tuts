from pywebio.input import input, FLOAT
from pywebio.output import put_text

class Calculation:
    def BMIcalculator(self, Height, Mass):
        # Calculate BMI
        BMI = Mass / (Height * Height)
        
        # Classify BMI using ranges
        for t1, t2 in [
            (16, "severely underweight"),
            (18.5, "underweight"),
            (25, "normal"),
            (30, "overweight"),
            (35, "moderately obese"),
            (float("inf"), "severely obese"),
        ]:
            if BMI <= t1:
                put_text(f"Your BMI is {BMI:.2f} and you are {t2}.")
                break

# Get user input
Height = input("Enter Height (in meters):", type=FLOAT)
Mass = input("Enter Weight (in Kg):", type=FLOAT)

# Create an object and calculate BMI
obj = Calculation()
obj.BMIcalculator(Height, Mass)

