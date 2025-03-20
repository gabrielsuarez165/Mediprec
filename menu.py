from nicegui import ui


def menu() -> None:
    ui.link('Home', '/').classes(replace='text-black')
    ui.link('Pacientes', '/patients/').classes(replace='text-black')
