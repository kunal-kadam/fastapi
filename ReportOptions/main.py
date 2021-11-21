from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDFillRoundFlatButton,MDRectangleFlatButton


class ProjectApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        screen = MDScreen()
        self.toolbar = MDToolbar(title="Safe Raste")
        self.toolbar.pos_hint = {"top":1}
        screen.add_widget(self.toolbar)

        screen.add_widget(MDFillRoundFlatButton(
            text="Create Report",
            font_size = 17,
            pos_hint= {"center_x": 0.5, "center_y": 0.7},
        ))
        screen.add_widget(MDFillRoundFlatButton(
            text="Update Report",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        ))
        screen.add_widget(MDFillRoundFlatButton(
            text="View Report",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        ))
        screen.add_widget(MDFillRoundFlatButton(
            text="Delete Report",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        ))
        return screen


if __name__ == '__main__':
    ProjectApp().run()

