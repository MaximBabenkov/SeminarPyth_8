import logger
import model
import view
import operation

def button_click() -> int:
    view.view_data('Calculator')           
    logger.action_logger('start')      
    val_a = view.input_value('value: ')
    my_sign = view.input_sign('sign: ')    
    val_b = view.input_value('value: ')
    model.init(val_a, val_b)
    match my_sign:
        case '+':   
            res = operation.summ(val_a, val_b)
        case '-':   
            res = operation.diff(val_a, val_b)   
        case '*':   
            res = operation.mult(val_a, val_b)
        case '/':   
            res = operation.div(val_a, val_b)
        case _:
            res = 'None'    
    view.view_data(f'result: {res}')
    logger.action_logger(f'{val_a}{my_sign}{val_b}={res}')           
    logger.action_logger('finish')
