from contextlib import contextmanager

from menu import menu

from nicegui import ui


@contextmanager
def frame(navtitle: str):
 
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    
    with ui.column().classes('absolute-center h-screen no-wrap p-9 w-full'):
        yield
        
    with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.label('MEDIPREC - tecnologia en la medicina').classes('font-bold')

    with ui.footer(value=False) as footer:
        ui.label('Cualquier consulta se puede comunicar con nosotros al XXX - XXX XXXX')
        
    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        ui.label('Menu')
        with ui.column():
            menu()
            
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')