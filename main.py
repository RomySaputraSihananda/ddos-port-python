import os;
import utils;

if(__name__ == '__main__'):
    os.system('clear');
    
    while True:    
        choise = utils.display();
        match(choise):
            case 1:
                utils.single_port();
            case 2:
                utils.all_port();
            case 99:
                break;
            case _:
                print('Wrong Choise ;(');
    
    utils.footer();