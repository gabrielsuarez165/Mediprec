from nicegui import ui

def content()-> None:
    with ui.card().classes('w-full'):
        ui.markdown('## **Buscar Paciente por Nombre y Apellido o por DNI**')
    ui.space()
    with ui.card().classes('w-full'):
        with ui.row():  
            ui.label('Nombre y Apellido del paciente')
        ui.input(placeholder='start typing').props('rounded outlined dense').classes('w-3/4')
        with ui.row():  
            ui.label('DNI del paciente')
        ui.input(placeholder='start typing').props('rounded outlined dense').classes('w-3/4')
    with ui.button().classes('w-full'):
        ui.link('buscar paciente', '/file_patient/').classes('white')
    