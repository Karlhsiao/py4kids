'''
    Calculate weekly payment by working hours and hourly rate
'''

STANDARD_HOURS = 40
OVERTIME_FACTOR = 1.5


def process_user_input(working_hours, hourly_rate):
    hrs = float(working_hours)
    r = float(hourly_rate)
    return hrs, r


def input_from_user():
    #working hours in the week, ex. 40
    working_hours = None
    #the hourly rate per hour, ex. 10.5
    hourly_rate = None
    working_hours = input("What's your working hours?:")
    hourly_rate = input("What's the hourly rate?:")
    
    return  working_hours, hourly_rate


def transform_payment(hrs, rate):
    overtime = hrs - STANDARD_HOURS
    overtime_hr = rate * OVERTIME_FACTOR

    payment = None
    if hrs > STANDARD_HOURS:
        payment = (STANDARD_HOURS*rate)+(overtime*overtime_hr)
    else:
        payment = hrs*rate

    return payment


def output_to_user(payment):
    payment = str(payment)
    print("Your payment will be: " + payment)


def test():
    hrs = 40
    rate = 10.5
    payment = transform_payment(hrs, rate)
    assert payment == 498.75, "Please check your code..."


if __name__ == "__main__":    
    hrs, rate = input_from_user()
    hrs, rate = process_user_input(hrs, rate)
    payment = transform_payment(hrs, rate)
    output_to_user(payment)
