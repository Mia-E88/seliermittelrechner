from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SilageApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Eingabefelder für Vorname, Name und Telefonnummer
        self.firstname_input = TextInput(hint_text='Vorname')
        layout.add_widget(self.firstname_input)

        self.lastname_input = TextInput(hint_text='Name')
        layout.add_widget(self.lastname_input)

        self.phone_input = TextInput(hint_text='Telefonnummer')
        layout.add_widget(self.phone_input)

        # Eingabefelder für Hektarzahl und Ertrag pro Hektar
        self.hectare_input = TextInput(hint_text='Hektarzahl')
        layout.add_widget(self.hectare_input)

        self.yield_input = TextInput(hint_text='Ertrag pro Hektar (in Tonnen)')
        layout.add_widget(self.yield_input)

        # Anzeige für das Ergebnis der Siliermittel-Berechnung
        self.result_label = Label(text="Benötigte Menge an Siliermittel:")
        layout.add_widget(self.result_label)

        # Berechnungsknopf
        calculate_button = Button(text='Berechnen')
        calculate_button.bind(on_press=self.calculate_silage)
        layout.add_widget(calculate_button)

        return layout

    def calculate_silage(self, instance):
        try:
            # Erfassen der Eingabedaten
            firstname = self.firstname_input.text
            lastname = self.lastname_input.text
            phone = self.phone_input.text
            hectare = float(self.hectare_input.text)
            yield_per_hectare = float(self.yield_input.text)

            # Berechnung der Gesamtertragsmenge und der benötigten Siliermittel-Pakete
            total_yield = hectare * yield_per_hectare
            silage_needed = total_yield / 100  # 1 Pack für 100 Tonnen

            # Ergebnisanzeige
            self.result_label.text = (f"{firstname} {lastname}, Telefonnummer: {phone}\n"
                                      f"Benötigte Menge an Siliermittel: {silage_needed:.2f} Packs")
        except ValueError:
            self.result_label.text = "Bitte geben Sie gültige Zahlen ein."

if __name__ == "__main__":
    SilageApp().run()
