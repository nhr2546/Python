from page_objects import PageObject, PageElement
class FramePage(PageObject):
    def check_page(self):
        return "Frame" in self.w.title
