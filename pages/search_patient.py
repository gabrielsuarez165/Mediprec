import theme
from nicegui import ui


def search_patient():
    with theme.frame('search_patient'):
        ui.page_title('BUSCAR PACIENTE')
        
        ui.markdown('## **Buscar Paciente por Nombre y Apellido o por DNI**')
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
                
        var = ui.input('Ingrese Nombre y Apellido o un DNI', validation=lambda value: 'Too short' if len(value) < 5 else None).classes('w-full')
        
        ui.label().bind_text_from(var, 'value')
        
        with ui.button().classes('px-6'):
            ui.link('buscar paciente', '/file_patient/').classes('white')
                   
        with ui.button().classes('px-14'):
            ui.link('VOLVER', '/patients/').classes('white')