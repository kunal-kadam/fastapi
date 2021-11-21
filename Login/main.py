from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Window.size = (350, 600)


class LoginPage(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager


if __name__ == "__main__":
    LoginPage().run()






# MDLabel:
#             text: "OR"
#             pos_hint: {"center_x": .5, "center_y": .2}
#             font_name: "Poppins-Regular"
#             font_size: "14sp"
#             halign: "center"
#         MDFlatLayout:
#             md_bg_color: 238/255, 238/255, 238/255, 1
#             size_hint: .68, .08
#             pos_hint: {"center_x": .5, "center_y": .1}
#             radius: [23]
#             MDIconButton:
#                 icon: "google"
#                 user_font_size: "20sp"
#                 pos_hint: {"center_x": .1, "center_y": .5}
#                 theme_text_color: "Custom"
#                 text_color: 0, 0, 0, 1
#             MDLabel:
#                 text: "Sign in with Google"
#                 pos_hint: {"center_x": .7, "center_y": .5}
#                 font_name: "Poppins-Regular"