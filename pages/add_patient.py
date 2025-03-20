import theme
from nicegui import ui


def add_patient():
    with theme.frame('add_patient'):
        ui.page_title('AGREGAR PACIENTE')
        
        ui.markdown('## **Agregar Paciente**')
        with ui.row().classes('w-full items-center '):
            ui.label('Nombre del paciente')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
            ui.label('Apellido del paciente')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
            
        with ui.row().classes('w-full items-center '):
            ui.label('DNI del paciente')
            ui.input('Ingrese DNI', validation=lambda value: 'Too short' if len(value) < 10 else None)
            ui.label('Obra Social')
            ui.select({1: 'IOMA', 2: 'Otro', 3: 'No tiene'})
            
        with ui.row().classes('w-full items-center '):
            ui.label('Direccion')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
            ui.label('Telefono')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        
        ui.button('Agregar paciente', on_click=lambda: ui.link('Agregar', '/add_patient/').classes('white'))
        
        with ui.button().classes('px-14'):
            ui.link('VOLVER', '/patients/').classes('px-14; white')