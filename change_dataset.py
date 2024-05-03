import os
import pandas as pd

class ChangeDataset:

    def __init__(self, dataset):
        self.dataset = dataset

    def change_dataset(self):
        # Standardisiere das Datumformat auf 'YYYY-MM-DD'
        self.dataset['order_date'] = pd.to_datetime(self.dataset['order_date'], errors='coerce', dayfirst=True)
        self.dataset['order_date'] = self.dataset['order_date'].dt.strftime('%Y-%m-%d')        
        return self.dataset
    
    def save_changed_dataset(self, path):
        self.dataset.to_csv(path, index=False)
        print(f'Dataset saved to {path}')

    