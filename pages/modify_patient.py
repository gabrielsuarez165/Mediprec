import theme
from nicegui import ui


def modify_patient():
    with theme.frame('modify_patient'):
        
        ui.page_title('MODIFICAR PACIENTE')
        
        ui.markdown('## **Modificar Paciente por Nombre y Apellido o por DNI**')
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        
        ui.input('Ingrese Nombre y Apellido o un DNI', validation=lambda value: 'Too short' if len(value) < 5 else None).classes('w-3/4')
        
        ui.button('Modificar paciente', on_click=lambda: ui.link('Modificar', '/modify_patient/').classes(replace='text-black'))
    
        with ui.button().classes('px-16'):
            ui.link('VOLVER', '/patients/').classes('white')