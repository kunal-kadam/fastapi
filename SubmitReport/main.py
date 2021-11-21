from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.filemanager import MDFileManager


class ProjectApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        screen = MDScreen()
        self.toolbar = MDToolbar(title="Safe Raste")
        self.toolbar.pos_hint = {"top":1}
        screen.add_widget(self.toolbar)

        self.input = MDTextField(
            hint_text = "Violation Type",
            halign="center",
            size_hint = (0.3,1),
            font_size = 16,
            pos_hint = {"center_x": 0.3,"center_y":0.8},
        )
        screen.add_widget(self.input)
        self.input = MDTextField(
            hint_text="Place",
            halign="center",
            size_hint=(0.3, 1),
            font_size=16,
            pos_hint={"center_x": 0.3, "center_y": 0.65},
        )
        screen.add_widget(self.input)
        self.input = MDTextField(
            hint_text="License Plate No.",
            halign="center",
            size_hint=(0.3, 1),
            font_size=16,
            pos_hint={"center_x": 0.71, "center_y": 0.8},
        )
        screen.add_widget(self.input)
        self.input = MDTextField(
            hint_text="Time",
            halign="center",
            size_hint=(0.3, 1),
            font_size=16,
            pos_hint={"center_x": 0.71, "center_y": 0.65},
        )
        screen.add_widget(self.input)
        self.input = MDTextField(
            hint_text="Attach Image (optional)",
            halign="center",
            size_hint=(0.7, 1),
            font_size=16,
            pos_hint={"center_x": 0.5, "center_y": 0.45},
        )
        screen.add_widget(self.input)
        screen.add_widget(MDFillRoundFlatButton(
            text="Submit Report",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.3},
        ))



        return screen



if __name__ == '__main__':
    ProjectApp().run()

