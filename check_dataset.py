import pandas as pd

class CheckDataset:

    def __init__(self, dataset):
        self.dataset = dataset


    def check_dataset(self):
        # - Überprüfe jede zeile auf korrektes Format
        # - Pizza ID von 1 bis 48622 hochzählt, stehend für jede Zeile
        # - 
        for colm in self.dataset.columns:
            if colm == 'pizza_id':
                # check numerisch
                is_numeric = pd.to_numeric(self.dataset[colm], errors='coerce').notnull().all()
                if is_numeric:
                    print(f'Alle Werte in der Spalte {colm} sind numerisch.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind numerisch.')

                # check alle IDs vorhanden
                for i in range(1, len(self.dataset.index)):
                    if i != self.dataset['pizza_id'].values[i-1]:
                        print(f'Pizza ID {i} fehlt')
                print(f'Alle Pizza ID in {colm} sin korrekt')

            elif colm == 'order_id':
                # Überprüfe, ob alle Werte numerisch sind
                is_numeric = pd.to_numeric(self.dataset[colm], errors='coerce').notnull().all()
                if is_numeric:
                    print(f'Alle Werte in der Spalte {colm} sind numerisch.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind numerisch.')

            elif colm == 'pizza_name_id':
                # Überprüfe, ob alle Werte strings sind mit mind. 1 unterstrich
                is_string = self.dataset[colm].str.contains('_').all()
                if is_string:
                    print(f'Alle Werte in der Spalte {colm} sind Strings.')
                else:
                    print(is_string)
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind Strings.')

            elif colm == 'quantity':
                # Überprüfe, ob alle Werte numerisch sind
                is_numeric = pd.to_numeric(self.dataset[colm], errors='coerce').notnull().all()
                if is_numeric:
                    print(f'Alle Werte in der Spalte {colm} sind numerisch.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind numerisch.')

            elif colm == 'order_date':
                # Überprüfe, ob alle Werte das richtige Datumsformat haben
                is_date = pd.to_datetime(self.dataset[colm], errors='coerce').notnull().all()
                if is_date:
                    print(f'Alle Werte in der Spalte {colm} sind Datumsangaben.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind Datumsangaben.')

            elif colm == 'order_time':
                # Überprüfe, ob alle Werte das richtige Zeitformat haben
                is_time = pd.to_datetime(self.dataset[colm], format='%H:%M:%S', errors='coerce').notnull().all()
                if is_time:
                    print(f'Alle Werte in der Spalte {colm} sind Zeitangaben.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind Zeitangaben.')

            elif colm == 'unit_price':
                # Überprüfe, ob alle Werte numerisch sind
                is_numeric = pd.to_numeric(self.dataset[colm], errors='coerce').notnull().all()
                if is_numeric:
                    print(f'Alle Werte in der Spalte {colm} sind numerisch.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind numerisch.')

            elif colm == 'total_price':
                # Überprüfe, ob alle Werte numerisch sind
                is_numeric = pd.to_numeric(self.dataset[colm], errors='coerce').notnull().all()
                if is_numeric:
                    print(f'Alle Werte in der Spalte {colm} sind numerisch.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind numerisch.')

            elif colm == 'pizza_size':
                # Überprüfe ob alle Werte in der Spalte 'pizza_size' entweder 'S', 'M', 'L', 'XL' oder 'XXL' sind
                is_size = self.dataset[colm].isin(['S', 'M', 'L', 'XL', 'XXL']).all()
                if is_size:
                    print(f'Alle Werte in der Spalte {colm} sind korrekt.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind korrekt.')

            elif colm == 'pizza_category':
                # Überprüfe auf die verschiedenen categroies
                is_category = self.dataset[colm].isin(['Classic', 'Veggie', 'Chicken', 'Supreme']).all()
                if is_category:
                    print(f'Alle Werte in der Spalte {colm} sind korrekt.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind korrekt.')

            elif colm == 'pizza_ingrediants':
                # Überprüfe, ob alle Werte strings mit komma sind
                is_string = self.dataset[colm].str.contains(',').all()
                if is_string:
                    print(f'Alle Werte in der Spalte {colm} sind Strings.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind Strings.')

            elif colm == 'pizza_name':
                # Überprüfe, ob name immer mit 'The' beginnt
                is_string_with_the = self.dataset[colm].str.startswith('The').all()
                if is_string_with_the:
                    print(f'Alle Werte in der Spalte {colm} sind korrekt.')
                else:
                    print(f'Fehler: Nicht alle Werte in der Spalte {colm} sind korrekt.')

                
                

         
        
