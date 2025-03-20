import theme
from nicegui import ui


def patients():
    with theme.frame('patients'):
        
        ui.page_title('PACIENTES')
        
        ui.markdown('# **Registro de Pacientes**')
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        
        with ui.button().classes('px-6'):
            ui.link('buscar paciente', '/search_patient/').classes('white')
       
        with ui.button().classes('px-5'):
            ui.link('agregar paciente', '/add_patient/').classes('white')
            
        with ui.button().classes('px-4'):
              ui.link('modificar paciente', '/modify_patient/').classes('white')
       
        with ui.button().classes('px-5'):
              ui.link('eliminar paciente', '/delete_patient/').classes('white')
              
        with ui.button().classes('px-6'):
              ui.link('listar pacientes', '/list_patients/').classes('white')
              
        with ui.button().classes('px-16'):
            ui.link('VOLVER', '/').classes('white')
            
            
            
