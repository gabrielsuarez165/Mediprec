import theme
from nicegui import ui


def list_patients():
    with theme.frame('list_patients'):
        ui.page_title('LISTAR PACIENTES')
        
        ui.markdown('## **Listado de Pacientes**')
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        
        ui.table(rows=[
            {'Nombre': 'Antonio', 'Apellido': 'Arriaga', 'DNI': 35000},
            {'Nombre': 'Jorge', 'Apellido': 'Mondeo', 'DNI': 32000},
            {'Nombre': 'Santino', 'Apellido': 'Boster', 'DNI': 72000},
        ])
    
        with ui.button().classes('px-14'):
            ui.link('VOLVER', '/patients/').classes('white')