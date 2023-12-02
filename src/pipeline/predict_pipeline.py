import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            preds_str = ['Normal' if preds[0] == 1 else 'Altered']
            return preds_str

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 season: float,
                 age: float,
                 childish_diseases: int,
                 trauma: int,
                 surgery: int,
                 high_fever: int,
                 alcohol_freq: float,
                 smoking: int,
                 sitting_hrs: float):
        self.season = season
        self.age = age
        self.childish_diseases = childish_diseases
        self.trauma = trauma
        self.surgery = surgery
        self.high_fever = high_fever
        self.alcohol_freq = alcohol_freq
        self.smoking = smoking
        self.sitting_hrs = sitting_hrs

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "season": [self.season],
                "age": [self.age],
                "childish_diseases": [self.childish_diseases],
                "trauma": [self.trauma],
                "surgery": [self.surgery],
                "high_fever": [self.high_fever],
                "alcohol_freq": [self.alcohol_freq],
                "smoking": [self.smoking],
                "sitting_hrs": [self.sitting_hrs]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
