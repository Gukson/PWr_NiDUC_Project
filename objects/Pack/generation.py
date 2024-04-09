import random
import pandas as pd

class Generation:
    def __init__(self, file_path):
        self.female_names = ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Krystyna', 'Barbara', 'Ewa', 'Elżbieta', 'Zofia',
                             'Teresa', 'Magdalena', 'Joanna', 'Danuta', 'Jadwiga', 'Halina', 'Irena', 'Monika', 'Helena', 'Beata',
                             'Aleksandra', 'Jolanta', 'Patrycja', 'Natalia', 'Agata', 'Klaudia', 'Wanda', 'Karolina', 'Marzena', 'Justyna',
                             'Kinga', 'Aneta', 'Renata', 'Gabriela', 'Blanka', 'Edyta', 'Alicja', 'Ola', 'Nadia', 'Dorota', 'Grażyna',
                             'Marcelina', 'Marta', 'Dominika', 'Karina', 'Paulina', 'Ewelina', 'Sylwia', 'Urszula', 'Inga', 'Ilona',
                             'Lidia', 'Izabela', 'Weronika', 'Emilia', 'Anita', 'Łucja', 'Nina', 'Kamila', 'Aldona', 'Emilka', 'Agnes',
                             'Sandra', 'Ania', 'Oliwia', 'Nikola', 'Olga', 'Julia', 'Małgosia', 'Natalie', 'Edyta', 'Martyna', 'Iga',
                             'Zuzanna', 'Łucja', 'Asia', 'Amelia', 'Dominika', 'Monia', 'Liliana', 'Wiktoria', 'Renata', 'Klaudyna',
                             'Jowita', 'Małgosia', 'Nela', 'Kasia', 'Hanna', 'Nadia', 'Justina']

        self.male_names = ['Jan', 'Andrzej', 'Piotr', 'Krzysztof', 'Stanisław', 'Tomasz', 'Paweł', 'Józef', 'Marek', 'Michał',
                           'Grzegorz', 'Jerzy', 'Tadeusz', 'Adam', 'Zbigniew', 'Henryk', 'Ryszard', 'Kazimierz', 'Mariusz', 'Dariusz',
                           'Wojciech', 'Leszek', 'Jacek', 'Edward', 'Maciej', 'Mirosław', 'Sławomir', 'Roman', 'Władysław', 'Robert',
                           'Antoni', 'Mateusz', 'Zdzisław', 'Janusz', 'Bogdan', 'Marcin', 'Jakub', 'Rafał', 'Marian', 'Mirosław',
                           'Wiesław', 'Artur', 'Janusz', 'Sebastian', 'Kamil', 'Daniel', 'Arkadiusz', 'Eugeniusz', 'Damian', 'Patryk',
                           'Karol', 'Dawid', 'Norbert', 'Filip', 'Hubert', 'Konrad', 'Kamil', 'Adrian', 'Szymon', 'Marcel', 'Radosław',
                           'Waldemar', 'Igor', 'Bartosz', 'Zenon', 'Łukasz', 'Adrian', 'Dominik', 'Karol', 'Wiktor', 'Bartłomiej',
                           'Kacper', 'Zygmunt', 'Radosław', 'Kacper', 'Tadeusz', 'Bogusław', 'Dawid', 'Krystian', 'Jarek', 'Krzysztof',
                           'Błażej', 'Filip', 'Ignacy', 'Wiktor', 'Kajetan', 'Konstanty', 'Bartek', 'Dariusz', 'Stefan', 'Tomasz',
                           'Stanisław', 'Patryk', 'Paweł', 'Piotrek']

        self.female_last_names = ['Nowak', 'Kowalska', 'Wiśniewska', 'Dąbrowska', 'Lewandowska', 'Wójcik', 'Kamińska', 'Kowalczyk', 'Zielińska', 'Szymańska',
                                   'Woźniak', 'Kozłowska', 'Jankowska', 'Wojciechowska', 'Kwiatkowska', 'Kaczmarek', 'Mazur', 'Krawczyk', 'Piotrowska', 'Grabowska',
                                   'Nowakowska', 'Pawłowska', 'Michalska', 'Nowicka', 'Adamczyk', 'Dudek', 'Zając', 'Wieczorek', 'Jabłońska', 'Król',
                                   'Majewska', 'Olszewska', 'Jaworska', 'Wróbel', 'Malinowska', 'Pawlak', 'Witkowska', 'Walczak', 'Stępień', 'Górska',
                                   'Rutkowska', 'Michalak', 'Sikora', 'Ostrowska', 'Baran', 'Duda', 'Szewczyk', 'Tomaszewska', 'Pietrzak', 'Marciniak',
                                   'Wróblewska', 'Zalewska', 'Jakubowska', 'Jasińska', 'Zawadzka', 'Sadowska', 'Bąk', 'Chmielewska', 'Włodarczyk', 'Borkowska',
                                   'Czarnecka', 'Sawicka', 'Sokołowska', 'Urbańska', 'Kubiak', 'Maciejewska', 'Szczepańska', 'Kucharska', 'Wilk', 'Kalinowska',
                                   'Lis', 'Mazurek', 'Wysocka', 'Adamska', 'Kaźmierczak', 'Wasilewska', 'Sobczak', 'Czerwińska', 'Andrzejewska', 'Cieślak',
                                   'Głowacka', 'Zakrzewska', 'Kołodziej', 'Sikorska', 'Krajewska', 'Gajewska', 'Szymczak', 'Szulc', 'Baranowska', 'Lipińska']

        self.male_last_names = ['Nowak', 'Kowalski', 'Wiśniewski', 'Dąbrowski', 'Lewandowski', 'Wójcik', 'Kamiński', 'Kowalczyk', 'Zieliński', 'Szymański',
                                 'Woźniak', 'Kozłowski', 'Jankowski', 'Wojciechowski', 'Kwiatkowski', 'Kaczmarek', 'Mazur', 'Krawczyk', 'Piotrowski', 'Grabowski',
                                 'Nowakowski', 'Pawłowski', 'Michalski', 'Nowicki', 'Adamczyk', 'Dudek', 'Zając', 'Wieczorek', 'Jabłoński', 'Król',
                                 'Majewski', 'Olszewski', 'Jaworski', 'Wróbel', 'Malinowski', 'Pawlak', 'Witkowski', 'Walczak', 'Stępień', 'Górski',
                                 'Rutkowski', 'Michalak', 'Sikora', 'Ostrowski', 'Baran', 'Duda', 'Szewczyk', 'Tomaszewski', 'Pietrzak', 'Marciniak',
                                 'Wróblewski', 'Zalewski', 'Jakubowski', 'Jasiński', 'Zawadzki', 'Sadowski', 'Bąk', 'Chmielewski', 'Włodarczyk', 'Borkowski',
                                 'Czarnecki', 'Sawicki', 'Sokołowski', 'Urbański', 'Kubiak', 'Maciejewski', 'Szczepański', 'Kucharski', 'Wilk', 'Kalinowski',
                                 'Lis', 'Mazurek', 'Wysocki', 'Adamski', 'Kaźmierczak', 'Wasilewski', 'Sobczak', 'Czerwiński', 'Andrzejewski', 'Cieślak',
                                 'Głowacki', 'Zakrzewski', 'Kołodziej', 'Sikorski', 'Krajewski', 'Gajewski', 'Szymczak', 'Szulc', 'Baranowski', 'Lipiński']
        
        self.postal_codes = self.load_postal_codes(file_path)

    def load_postal_codes(self, file_path):
        postal_codes = {}
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            city = row['Gmina'] 
            postal_code = row['Kod']
            postal_codes[city] = postal_code
        return postal_codes

    def generate_name(self, gender='male'):
        if gender == 'male':
            first_name = random.choice(self.male_names)
            last_name = random.choice(self.male_last_names)
        else:
            first_name = random.choice(self.female_names)
            last_name = random.choice(self.female_last_names)
        return f'{first_name} {last_name}'
    def generate_city_and_postal_code(self):
        city = random.choice(list(self.postal_codes.keys()))
        postal_code = self.postal_codes[city]
        return city, postal_code

    #TODO add flags generating
