import datetime

def validate(date_text):
    try:
        inputDate = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        if (is_spring(inputDate)):
            print(f'{inputDate} Está dentro de la estacion PRIMAVERA')
        if (is_summer(inputDate)):
            print(f'{inputDate} Está dentro de la estacion VERANO')
        if (is_autumn(inputDate)):
            print(f'{inputDate} Está dentro de la estacion OTOÑO')
        if (is_winter(inputDate)):
            print(f'{inputDate} Está dentro de la estacion INVIERNO')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def is_spring(inputDate):
    startDate = datetime.datetime.strptime(str(inputDate.year) + "-03-21", '%Y-%m-%d')
    endDate = datetime.datetime.strptime(str(inputDate.year) + "-06-20", '%Y-%m-%d')
    return startDate <= inputDate <= endDate

def is_summer(inputDate):
    startDate = datetime.datetime.strptime(str(inputDate.year) + "-06-21", '%Y-%m-%d')
    endDate = datetime.datetime.strptime(str(inputDate.year) + "-09-20", '%Y-%m-%d')
    return startDate <= inputDate <= endDate

def is_autumn(inputDate):
    startDate = datetime.datetime.strptime(str(inputDate.year) + "-09-21", '%Y-%m-%d')
    endDate = datetime.datetime.strptime(str(inputDate.year) + "-12-20", '%Y-%m-%d')
    return startDate <= inputDate <= endDate

def is_winter(inputDate):
    if (1 <= inputDate.month <= 3):
        startDate = datetime.datetime.strptime(str(inputDate.year - 1) + "-12-21", '%Y-%m-%d')
        endDate = datetime.datetime.strptime(str(inputDate.year) + "-03-20", '%Y-%m-%d')
    else:
        startDate = datetime.datetime.strptime(str(inputDate.year) + "-12-21", '%Y-%m-%d')
        endDate = datetime.datetime.strptime(str(inputDate.year + 1) + "-03-20", '%Y-%m-%d')

    return startDate <= inputDate <= endDate


inputDate = input("Digite la fecha de la estacion del año que deseas consultar, en formato YYYY-MM-DD: ")
validate(inputDate)