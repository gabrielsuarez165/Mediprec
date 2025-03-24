from contextlib import contextmanager

from menu import menu

from nicegui import ui


@contextmanager
def frame(navtitle: str):
 
    ui.colors(primary='#1692ca', secondary='#53B689', accent='#111B1E', positive='#53B689')
 
    with ui.column().classes('absolute-center h-screen no-wrap p-9 w-full'):
        yield
    
    with ui.header().classes(replace='row items-center h-16') as header:
            ui.label("").tailwind("pr-6")
            ui.image('assets/images/logo.png').classes("w-14")
            ui.label("").tailwind("px-0.5")
            ui.label('MEDIPREC').style('color: white; font-size: 225%;').tailwind("px-2.5 pl-4", "font-bold", "text-white-800")
            ui.space()

    with ui.footer(value=True) as footer:
         ui.label('Cualquier consulta se puede comunicar con nosotros al XXX - XXX XXXX')

            
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')