from nicegui import ui, app
def content() -> None:
    with ui.card().classes('w-full'):

                with ui.row():
                    ui.icon("o_info").classes('text-xl')
                    ui.restructured_text('''Mediprec

                                            Manejo de pacientes: 
                                            Buscar pacientes - pacientes historial  - pacientes actualizar datos - pacientes eliminar 
                                            Agregar pacientes (tener en cuenta obra social) 
                                            Listar pacientes (total) 
                                            Listar pacientes (por especificidad) 
                                             
                                            Manejo de analisis: 
                                            Analisis de laboratorio redactar - imprimir por ioma - imprimir generico 
                                            Analisis clinicos - imprimir por ioma - imprimir generico 
                                            Analisis (por rango de edades)  - imprimir por ioma - imprimir generico 
                                             
                                            Registro de resultados 
                                            Comparativa de resultados con analisis anteriores 
                                            Registro de observaciones 
                                            Posibles diagnosticos basados en resultados 
                                             
                                            Manejo de recetas: 
                                            Receta de farmacos  - imprimir por ioma - imprimir generico 
                                            Receta de farmacos dosificacion / horarios / duracion del tratamiento - imprimir 
                                             
                                            Tratamientos: 
                                            Observaciones del tratamiento 
                                            Observaciones de efectos secundarios 
                                            Monitoreo de tratamientos 
                                            Programacion para proxima cita (fechas!!) 
                                            Notas clinicas 
                                            
                                            registrar fecha en cada una de las partes. ''')