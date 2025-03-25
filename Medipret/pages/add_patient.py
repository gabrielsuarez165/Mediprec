from nicegui import ui


def content()-> None:
    with ui.card().classes('w-full'):  
        ui.markdown('## **Agregar Paciente**').classes('justify')
    ui.space()
    with ui.card().classes('w-full'):   
        with ui.row().classes('w-full items-center '):
            ui.label('Nombre del paciente')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
            ui.label('Apellido del paciente')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
                    
        with ui.row().classes('w-full items-center '):
            ui.label('DNI del paciente')
            ui.input('Ingrese DNI', validation=lambda value: 'Too short' if len(value) < 10 else None)
            ui.label('Obra Social').classes('w-1/8')
            ui.select({1: 'IOMA', 2: 'Otro', 3: 'No tiene'})
            ui.label('Perfil').classes('w-1/8')
            ui.select({1: '15 a 30', 2: '30 a 45', 3: '45 a 60'})
                    
        with ui.row().classes('w-full items-center '):
            ui.label('Direccion')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
            ui.label('Telefono')
            ui.input('', validation=lambda value: 'Too short' if len(value) < 10 else None).classes('w-1/4')
                
        ui.add_css('''.white
                {color: white;
                   text-decoration:none
                }''')
        with ui.button().classes('w-full'):
            ui.link('Agregar paciente', '/add_patient/').classes('white')
                     
    with ui.button().classes('w-full'):
        ui.link('VOLVER', '/').classes('white')