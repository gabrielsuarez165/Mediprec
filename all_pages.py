from nicegui import ui
from pages.file_patient import file_patient

def create() -> None:    
    ui.page('/file_patient/')(file_patient)    
    
if __name__ == '__main__':
    create()