class PageState():
    def __init__(self) -> None:
        self.widgets = {}
        self.pages = {}

    def set_routes(self, routes):
        self.routes = routes

    def add_widget(self, widgets):
        for widget in widgets:
            self.widgets[widget] = widgets[widget]

    def add_page(self, pages):
        for page in pages:
            self.pages[page] = pages[page]