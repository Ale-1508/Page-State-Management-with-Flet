from flet import *

class Page2(UserControl):
    state = {}

    def __init__(self, page_state):
        super().__init__()
        self.state = page_state

    def handle_click(self, e):
        self.state.pages['page'].controls[0] = self.state.pages['homepage']
        self.state.pages['page'].update()


    def build(self):
        return Container(
            bgcolor='red',
            height=100,
            width=100,
            on_click=self.handle_click
        )