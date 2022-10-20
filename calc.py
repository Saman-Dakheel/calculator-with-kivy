from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 600)
Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def number_pressed(self, number):
        proir = self.ids.calc_input.text
        if proir == '0':
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{number}'
        else:
            self.ids.calc_input.text = f'{proir}{number}'

    def remove(self):
        proir = self.ids.calc_input.text
        proir = proir[:-1]
        self.ids.calc_input.text = proir

    def sign(self, selected_sign):
        proir = self.ids.calc_input.text
        self.ids.calc_input.text = f'{proir}{selected_sign}'

    def equals(self):
        proir = self.ids.calc_input.text
        try:
            answer = eval(proir)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'

    def negative(self):
        proir = self.ids.calc_input.text
        if '-' in proir:
            self.ids.calc_input.text = f'{proir.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{proir}'

    def dot(self):
        proir = self.ids.calc_input.text

        if '+' in proir and '.' not in proir:
            proir = f'{proir}.'
            self.ids.calc_input.text = proir
        elif '.' in proir:
            pass
        else:
            proir = f'{proir}.'
            self.ids.calc_input.text = proir

    def percentage(self):
        proir = self.ids.calc_input.text
        answer = int(proir)/ 100
        self.ids.calc_input.text = str(answer)


class Calculator(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Calculator().run()
