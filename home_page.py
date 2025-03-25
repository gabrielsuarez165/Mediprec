from nicegui import ui
import pages.add_patient
import pages.lala
from pathlib import Path
import pages.perfiles
import pages.search_patient

def content() -> None:
    ui.markdown('')
    with ui.tabs() as tabs:
        search = ui.tab('search','Buscar Paciente', icon='search')
        add = ui.tab('add', 'Agregar Paciente', icon='alarm')
        perfiles = ui.tab('perfiles', 'Perfiles', icon='movie')
        lala = ui.tab('lala', 'CopyRigth' , icon='alarm' )    
    with ui.tab_panels(tabs, value='search').classes('w-full'):
        with ui.tab_panel(search):
            pages.search_patient.content()               
        with ui.tab_panel(add):
            pages.add_patient.content()         
        with ui.tab_panel(lala):
            pages.lala.content()                                
        with ui.tab_panel(perfiles):
            pages.perfiles.content()