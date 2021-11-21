from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDFloatLayout:
    MDCard:
        size_hint: .45, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        Carousel:
            id: slide
            MDFloatLayout:
                MDTextField:
                    hint_text: "First Name"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Last Name"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .2}
                    on_release: app.next()
            MDFloatLayout:
                MDTextField:
                    hint_text: "Do you own a Vehicle?"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Are you the Driver?"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .2}
                    on_release: app.previous()
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .2}
                    on_release: app.next()
            MDFloatLayout:
                MDTextField:
                    hint_text: "Email Address"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Phone Number"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .2}
                    on_release: app.previous()
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .2}
                    on_release: app.next()
            MDFloatLayout:
                MDTextField:
                    hint_text: "Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                    password: True
                MDTextField:
                    hint_text: "Confirm Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                    password: True
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .2}
                    on_release: app.previous()
                MDRaisedButton:
                    text: "SUBMIT"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .2}               
    MDLabel:
        text: "SignUp Form"
        bold: True
        pos_hint: {"center_x": .87, "center_y": .75}
        font_style: "H4"
    MDProgressBar:
        size_hint_x: .36
        pos_hint: {"center_x": .50, "center_y": .65}
"""


class ProjectApp(MDApp):
    def build(self):
        kv = Builder.load_string(KV)
        return kv

    def next(self):
        self.root.ids.slide.load_next(mode="next")

    def previous(self):
        self.root.ids.slide.load_previous()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ProjectApp().run()

