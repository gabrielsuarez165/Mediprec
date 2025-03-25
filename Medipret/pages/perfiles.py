from nicegui import ui, app

def content()-> None:
    with ui.card().classes('w-full'):  
        ui.markdown('## **Perfiles de Paciente segun Edad**')
    ui.space()
    with ui.card().classes('w-full'):                             
        with ui.tabs() as tabs:
            ui.tab('h', label='15 a 30', icon='account_circle')
            ui.tab('a', label='30 a 45', icon='account_circle')
            ui.tab('c', label='45 a 60', icon='account_circle')
        with ui.tab_panels(tabs, value='h').classes('w-full'):
            with ui.tab_panel('h'):
                ui.label('Pacientes de 15 a 30 años')
                with ui.card().classes('w-full'):
                    with ui.column().classes('w-full'):
                        ui.label('Examen clínico físico completo')
                        ui.label(' hemograma completo, hepatograma, colesterol LDL, triglicéridos, glucemia, HbA1c, uricemia, creatininemia')
                        ui.label('Examen orina completa y de 24 horas')
                        ui.label('electrocardiograma y  ergometría')
                        ui.label('Radiografía de tórax')         
                                                        
            with ui.tab_panel('a'):
                ui.label('Pacientes de 30 a 45 añoss')
                with ui.card().classes('w-full'):
                    with ui.column().classes('w-full'):
                        ui.label('Examen clínico físico completo')
                        ui.label(' hemograma completo, hepatograma, colesterol LDL, triglicéridos, glucemia, HbA1c, uricemia, creatininemia')
                        ui.label('Examen orina completa y de 24 horas')
                        ui.label('electrocardiograma y  ergometría')
                        ui.label('Radiografía de tórax')
                                        
            with ui.tab_panel('c'):
                ui.label('Pacientes de 45 a 60 añoss')
                with ui.card().classes('w-full'):
                    with ui.column().classes('w-full'):
                        ui.label('Examen clínico físico completo')
                        ui.label(' hemograma completo, hepatograma, colesterol LDL, triglicéridos, glucemia, HbA1c, uricemia, creatininemia')
                        ui.label('Examen orina completa y de 24 horas')
                        ui.label('electrocardiograma y  ergometría')
                        ui.label('Radiografía de tórax')
                                
    with ui.button().classes('w-full'):
            ui.link('VOLVER', '/').classes('white')