import theme
from nicegui import ui


def file_patient():
    with theme.frame('patients'):
        
        ui.page_title('PACIENTE')
        
        ui.markdown('')
        ui.space()
        
        ui.add_css('''.white
            {color: white;
            text-decoration:none
            }''')
        with ui.card().classes('w-full'):
            ui.label('INFORMACION DEL PACIENTE')
            ui.table(rows=[{'Nombre': 'Antonio', 'Apellido': 'Arriaga', 'DNI' : '33.333.333' ,'Obra Social': 'IOMA' , 'Direccion' : ' Calle 137 y 66' , 'Telefono' : '221 - 654 - 3214'}]).classes('w-full')
        ui.space()
        
        with ui.card().classes('w-full'):
            ui.label('ANALISIS de LABORATORIO SEGUN PERFIL DEL PACIENTE')
        with ui.card().classes('w-full'):
            ui.label('ANALISIS DE LABORATORIO').classes('bolt')
            ui.label(' hemograma completo, hepatograma, colesterol LDL, triglicéridos, glucemia, HbA1c, uricemia, creatininemia')
            ui.label('Examen orina completa y de 24 horas')
            
            with ui.button().classes('px-16'):
                  ui.link('Recetar analisis de Laboratorio', '/').classes('white')
        ui.space()
        
        
        with ui.card().classes('w-full'):
            ui.label('ANALISIS CLINICO SEGUN PERFIL DEL PACIENTE')
        with ui.card().classes('w-full'):
            ui.label('ANALISIS CLINICO').classes('bolt')
            ui.label(' Electrocardiograma')
            ui.label(' Ergometria')
            ui.label(' Placa de Torax')
            ui.label('Examen fisico completo')
            
            with ui.button().classes('px-16'):
                  ui.link('Recetar analisis Clinico', '/').classes('white')
        ui.space()
        
        with ui.card().classes('w-full'):
            ui.label('HISTORIAL CLINICO').classes('bolt')
            ui.label(f'''Se redactara tomando como base el motivo de consulta, a continuación se hará la semiografía completa de
                  todos los síntomas y signos referidos por el paciente, en orden cronológico.
                  Debe constar también la evolución del estado general del paciente anterior a la consulta, sus síntomas y/o
                  internaciones efectuadas, los estudios y tratamientos realizados con anterioridad y sus resultados siempre
                  referidos al motivo de consulta.
                  Continuar la evolución hasta el momento de la consulta''') 
            with ui.row().classes('w-full items-center '):   
                  with ui.button().classes('px-5'):
                        ui.link('Ver historial Clinico COMPLETO', '/').classes('white')
                  with ui.button().classes('px-5'):
                        ui.link('Redactar historial Clinico ', '/').classes('white')
      
        ui.space()
       
        with ui.card().classes('w-full'):       
            with ui.button().classes('px-16'):
                   ui.link('VOLVER', '/').classes('white')
            
        ui.space()
        
        
        