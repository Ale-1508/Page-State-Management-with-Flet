import flet
from flet import *

from pages.page1 import Page1
from pages.page2 import Page2

from state import PageState

# main
def main(page: Page):
    
    page.title = "Title"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window_width = 360
    page.window_height = 360

    page_state = PageState()
    page1 = Page1(page_state)
    page2 = Page2(page_state)

    pages = {'page' : page, 'homepage' : page1, 'others' : page2, }

    page_state.add_page(pages)
    print(page_state.pages)


    page.add(page1)
    page.update()



if __name__ == '__main__':
    flet.app(target=main)