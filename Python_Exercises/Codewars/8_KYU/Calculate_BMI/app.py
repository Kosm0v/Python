def bmi(weight, height):
    bmi = round(weight/(height**2) , 2)
    # if(bmi <= 18.5): return "Underweight"
    # elif(18.5 < bmi <= 25.0): return "Normal"
    # elif(25.0 < bmi <= 30.0): return "Overweight"
    # else: return "Obese"

    #clever
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi > 30) + (bmi > 25) + (bmi > 18.5)]