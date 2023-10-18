from shiny import App, ui

app_ui = ui.page_fluid(
    ui.head_content(ui.include_css("stylesheet.css")), ui.h2("Hello, world!")
)


def server(input, output, session):
    ...


app = App(app_ui, server)
