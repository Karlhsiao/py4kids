from enum import IntEnum, unique

@unique
class BMI_CATEGORY(IntEnum): 
    VERY_SEVERELY_UNDERWEIGHT = 0
    SEVERELY_UNDERWEIGHT = 1
    UNDERWEIGHT = 2
    NORMAL = 3
    OVERWEIGHT_SLIGHTLY = 4
    MODERATELY_OBESE = 5
    SEVERELY_OBESE = 6
    VERY_SEVERELY_OBESE = 7
    MORBIDLY_OBESE = 8
    SUPER_OBESE = 9
    HYPER_OBESE = 10


def process_user_input(weight, height):
    w = float(weight)
    h = float(height)
    return w, h


def input_from_user():
    weight = None
    height = None
    weight = input('Please enter your weight(kg):')
    height = input('Please enter your height(m):')
    return  weight, height


def transform_calc_bmi(w, h):
    bmi = None
    bmi = w/(h*h)
    return bmi


def output_to_user(w, h, bmi, cat):
    w = str(w)
    h = str(h)
    bmi = str(bmi)
    cat = str(cat)
    print("Your weight:" + w + ",Your height:" + h + ",Your BMI:" + bmi +",Category:" + cat)


def classify(bmi):
    category = None
    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 23:
        category = "Normal Range"

    else:
        category = "Overweight"
 
    return category


if __name__ == "__main__":
    weight, height = input_from_user()
    w, h = process_user_input(weight, height)
    bmi = transform_calc_bmi(w, h)
    cat = classify(bmi)
    output_to_user(w, h, bmi, cat)
