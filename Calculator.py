from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Set the app size
Window.size = (500, 700)

Builder.load_file('Calculator.kv')


class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text = "0"

    # Create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # Test for error first
        if 'Error' in prior:
            prior = ''

        # determin if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def dot(self):
        prior = self.ids.calc_input.text
        # Split out text box by +
        num_list = prior.split('+')
        # add a point at then end of the text box
        if "+" in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # Create Function to remove last character
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last character
        prior = prior[:-1]
        # Output back to the text box
        self.ids.calc_input.text = prior

    # Create Function to make text box pos/neg
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there's a -sign in text box
        if prior[0] == "-":
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create addition function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        if prior[-1] in "+,-,*,/":
            pass
        else:
            # slap a plus sing to the text box
            self.ids.calc_input.text = f"{prior}{sign}"

    # Create equals to function
    def equals(self):
        prior = self.ids.calc_input.text
        # Error Handling
        try:
            answer = eval(prior)
            # Evaluate the math from the text box
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'
        '''
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            # loop
            for number in num_list:
                answer = answer + float(number)

            self.ids.calc_input.text = str(answer)
        '''


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
