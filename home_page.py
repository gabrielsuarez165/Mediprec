from nicegui import ui
import pages.add_patient
import pages.lala
from pathlib import Path

import pages.perfiles
def content() -> None:
        ui.add_css('''.white
                {color: white;
                text-decoration:none
                }''')
        ui.markdown('''




            ''')
        with ui.tabs() as tabs:
            search = ui.tab('search','Buscar Paciente', icon='search')
            add = ui.tab('add', 'Agregar Paciente', icon='alarm')
            perfiles = ui.tab('perfiles', 'Perfiles', icon='movie')
            lala = ui.tab('lala', 'CopyRigth' , icon='alarm' )
            
        with ui.tab_panels(tabs, value='search').classes('w-full'):
                    with ui.tab_panel(search):
                        ui.label('Buscar Paciente').classes('text-h4')
                        with ui.card().classes('w-full'):
                            with ui.column().classes('w-full items-center'):
                                with ui.row().classes('w-full items-center '):
                                    with ui.button().classes('px-6'):
                                        ui.link('buscar paciente', '/file_patient/').classes('white')
                                    ui.label('Nombre y Apellido del paciente')
                                    ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
                                    ui.label('DNI del paciente')
                                    ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/8')
                    
                    with ui.tab_panel(add):
                        with ui.card().classes('w-full'):
                            pages.add_patient.content()
                            
                    with ui.tab_panel(lala):
                        ui.label('CopyRigth').classes('text-h4')
                        with ui.card().classes('w-full'):
                            pages.lala.content()
                                        
                    with ui.tab_panel(perfiles):
                        ui.label('Perfiles segun edad').classes('text-h4')
                        with ui.card().classes('w-full'):
                            pages.perfiles.content()
                          
                    with ui.button().classes('px-16'):
                        ui.link('VOLVER', '/').classes('white')