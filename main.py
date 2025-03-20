import all_pages
import home_page
import theme

from nicegui import app, ui

@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()

all_pages.create()


ui.run(title='MEDIPREC')