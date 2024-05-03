import pandas as pd
from change_dataset import ChangeDataset
from check_dataset import CheckDataset

def main():
    input_path = 'dataset/pizza_sales.csv'
    output_path = 'dataset/pizza_sales_updated.csv'
    check_dataset = 'dataset/pizza_sales_updated.csv'
    
    #process_change_dataset(input_path, output_path)
    process_check_dataset(check_dataset)

# Definiere eine Funktion oder Methode, um den Datensatz zu laden, zu ändern und zu speichern
def process_change_dataset(input_path, output_path):
    dataset = pd.read_csv(input_path)
    
    # Erstelle eine Instanz der ChangeDataset-Klasse
    changer = ChangeDataset(dataset)
    
    # Ändere das Datumformat
    updated_dataset = changer.change_dataset()
    #print(updated_dataset.head())
    
    # Speichere das geänderte DataFrame in einer CSV-Datei
    changer.save_changed_dataset(output_path)


def process_check_dataset(check_dataset):
    dataset = pd.read_csv(check_dataset)
    
    # Erstelle eine Instanz der CheckDataset-Klasse
    checker = CheckDataset(dataset)
    
    # Überprüfe den Datensatz auf fehlende Werte
    missing_values = checker.check_dataset()
    return missing_values

if __name__ == '__main__':
    main()