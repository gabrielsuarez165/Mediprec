import theme
from nicegui import ui


def file_patient():
    with theme.frame('patients'):
        
        ui.page_title('PACIENTE')
        
        ui.markdown(f'# **ANTONIO ARRIAGA - DNI 33.333.333**')
        #ui.label().bind_text_from(var)
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        
        ui.table(rows=[{'Nombre': 'Antonio', 'Apellido': 'Arriaga', 'DNI' : '33.333.333' ,'Obra Social': 'IOMA' , 'Direccion' : ' Calle 137 y 66' , 'Telefono' : '221 - 654 - 3214'}])
        
        with ui.button().classes('px-16'):
            ui.link('Recetar analisis de Laboratorio', '/').classes('white')
       
        with ui.button().classes('px-18'):
            ui.link('Recetar analisis Clinico', '/').classes('white')
            
        with ui.button().classes('px-4'):
              ui.link('Registrar analisis de Laboratorio', '/').classes('white')
       
        with ui.button().classes('px-5'):
              ui.link('Registrar analisis Clinico', '/').classes('white')
              
        with ui.button().classes('px-5'):
              ui.link('Ver historial Clinico', '/').classes('white')

        with ui.button().classes('px-5'):
              ui.link('Ver historial de Laboratorio', '/').classes('white')

        with ui.button().classes('px-5'):
              ui.link('Recetar farmacos', '/').classes('white')
        
        with ui.button().classes('px-5'):
              ui.link('Registrar tratamiento medico', '/').classes('white')
        
        with ui.button().classes('px-5'):
              ui.link('Registrar monitoreo clinico', '/').classes('white')
              
        with ui.button().classes('px-16'):
            ui.link('VOLVER', '/').classes('white')