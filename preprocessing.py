class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def handle_missing_values(self, strategy='mean'):
        if strategy == 'mean':
            self.data.fillna(self.data.mean(), inplace=True)
        elif strategy == 'median':
            self.data.fillna(self.data.median(), inplace=True)
        elif strategy == 'mode':
            self.data.fillna(self.data.mode().iloc[0], inplace=True)
        else:
            raise ValueError('Unsupported strategy')

    def feature_normalization(self):
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        self.data = scaler.fit_transform(self.data)
        return self.data


class ModelTrainer:
    def __init__(self, model, training_data, labels):
        self.model = model
        self.training_data = training_data
        self.labels = labels

    def train_model(self):
        self.model.fit(self.training_data, self.labels)
        return self.model

    def evaluate_model(self, test_data, test_labels):
        return self.model.score(test_data, test_labels)