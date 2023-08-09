import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.xlsx'):
            self.data = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format")

    def summarize_numeric_variables(self):
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        numeric_data = self.data.select_dtypes(include=['number'])
        summary = numeric_data.describe()
        return summary
data_analyzer = DataAnalyzer('Titanic-Dataset.csv')  
data_analyzer.load_data()
summary = data_analyzer.summarize_numeric_variables()
print(summary)
