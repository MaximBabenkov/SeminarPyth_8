from datetime import datetime as dt

def action_logger(data):
    time = dt.now().strftime('%D: %H:%M:%S')
    with open('journal.csv', 'a') as file:
        result = file.write(f'{time} {data}\n')
    return result


