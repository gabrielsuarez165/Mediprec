from nicegui import ui
from pages.patients import patients
from pages.add_patient import add_patient
from pages.search_patient import search_patient
from pages.modify_patient import modify_patient
from pages.delete_patient import delete_patient
from pages.file_patient import file_patient
from pages.list_patients import list_patients

def create() -> None:
    
    ui.page('/patients/')(patients)
    
    ui.page('/search_patient/')(search_patient)
    
    ui.page('/add_patient/')(add_patient)
    
    ui.page('/modify_patient/')(modify_patient)
    
    ui.page('/delete_patient/')(delete_patient)
    
    ui.page('/file_patient/')(file_patient)
    
    ui.page('/list_patients/')(list_patients)
    
    
if __name__ == '__main__':
    create()