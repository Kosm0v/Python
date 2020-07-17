def divisible_by(numbers, divisor):
    return list(filter(lambda x: not x%divisor,numbers))