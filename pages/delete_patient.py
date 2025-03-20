import theme
from nicegui import ui


def delete_patient():
    with theme.frame('delete_patient'):
        ui.page_title('ELIMINAR PACIENTE')
        
        ui.markdown('## **Eliminar Paciente por Nombre y Apellido o por DNI**')
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        
        ui.input('Ingrese Nombre y Apellido o un DNI', validation=lambda value: 'Too short' if len(value) < 5 else None).classes('w-3/4')
        
        ui.button('Eliminar paciente', on_click=lambda: ui.link('Eliminar', '/delete_patient/').classes(replace='text-black'))
    
        with ui.button().classes('px-14'):
            ui.link('VOLVER', '/patients/').classes('white')