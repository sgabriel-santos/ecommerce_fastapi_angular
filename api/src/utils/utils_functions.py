from datetime import datetime, date, timedelta
import os

def format_input_text(text: str):
    return text.upper()

def get_date_en_format(reference_date: str = '', with_hour: bool=True):
    if not reference_date:
        current_date = str(datetime.now())
        return current_date if with_hour else current_date.split(' ')[0]

    hour = str(datetime.now()).split(' ')[1]
    year, month, day = reference_date.split('-')
    current_date = date(int(year), int(month), int(day))
    return f'{str(current_date)} {hour}'

def format_date_dismissed(reference_date: str):
    date_, hour = reference_date.split(' ')
    year, month, day = date_.split('-')
    current_date = date(int(year), int(month), int(day))
    return f'{str(current_date)}'


def format_hire_date(employees = [], date_import: str = None):
    for employee in employees:
        try:
            date_separeted = employee['hire_date'].split(' ')
            if len(date_separeted) > 1:
                employee['hire_date'] = date_separeted[0]
            else:
                month, day, year = employee['hire_date'].split('/')
                employee['hire_date'] = date_to_two_digits(year, month, day)
        except:
            employee['hire_date'] = date_import if date_import else get_date_en_format(None, False)
    return employees


def date_to_two_digits(year, month, day):
    year, month, day = str(year), str(month), str(day)
    year = '20'+ year if int(year) < 100 else year
    month = '0'+month if int(month) < 10 else month
    day =  '0'+day if int(day) < 10 else day

    return f'{year}-{month}-{day}'

def build_error_empty(errors, isEmpty):
    return {
        "error": errors,
        "isEmpty": isEmpty
    }

def add_errors_history_to_file(errors_history, enterprise, date_import):
    if not errors_history: return
    try:
        current_path = os.getcwd().replace('\\','/')
        file = open(f"{current_path}/Centros de Custo Não encontrados.txt", 'a')
        file.write(f'--- {enterprise} ({date_import}) ---\n')
        for error in errors_history: file.write(error+'\n')
        file.close()
    except:
        print('An error occurred while writing to the file')

def get_previous_dates(date: str, nb_months: int) -> list[str]:
    year,month = date.split('.')
    current_date = datetime(int(year),int(month),1)
    response = []
    response.append(build_date(year, month))
    for i in range(nb_months-1):
        previous_date = current_date - timedelta(current_date.day+1)
        day, month, year = previous_date.day, previous_date.month, previous_date.year
        response.append(build_date(year, month))
        current_date = previous_date
    return response

def get_before_day(date: str):
    year,month,day = date.split("-")
    current_day = datetime(int(year), int(month), int(day))
    previous_day = current_day - timedelta(1)
    return str(previous_day.date())

def build_date(year, month):
    return f"{year}.{'0' if int(month) < 10 else '' }{int(month)}"

def build_year_month(year, month):
    year, month = int(year), int(month)
    year = '20'+str(year) if year < 100 else str(year)
    month = '0'+str(month) if month < 10 else str(month)
    return f'{year}.{month}'

def get_last_year(date: str):
    year,month = date.split('.')
    return build_date(int(year)-1, month)

# return message to hardware
def send_exception_message(msg, light, bip, color):
    return {
        "message": msg,
        "light": light,
        "bip": bip,
        "color": color
    }

def get_month_name_by_position(index = 0) -> str:
    month_name = "month_"
    if index == 0: month_name += "one"
    if index == 1: month_name += "two"
    if index == 2: month_name += "three"
    if index == 3: month_name += "four"
    if index == 4: month_name += "five"
    return month_name

def validation_order_range(order: int, start: int, stop: int) -> bool:
    list_order_range = list(range(start, stop+1))
    return True if order in list_order_range else False

def build_cod_column(data):
    return get_value_or_null(data, 'staff_operator') + data['enterprise'] + data['department_code'] + data['function']

def get_value_or_null(data, key):
    return data[key] if data[key] else 'null'
