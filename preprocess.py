import numpy as np
import pandas as pd
import re


class CarDataPreprocessor:
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def remove_missing(self):
        self.df = self.df.dropna(how="any")

    def extract_torque_rpm(self):
        torque_rpm = []

        for item in self.df["torque"]:
            res = item.replace(".", "").replace(",", "")
            nums = [int(s) for s in re.findall(r"\d+", res)]
            torque_rpm.append(max(nums))

        self.df["torque_rpm"] = torque_rpm

    def extract_mileage(self):

        def extract(x):
            match = re.search(r"\d+\.?\d*", x)
            if match:
                return float(match.group())
            return np.nan

        self.df["mileage_value"] = self.df["mileage"].apply(extract)

    def extract_engine(self):

        def extract(x):
            match = re.search(r"\d+", x)
            if match:
                return int(match.group())
            return np.nan

        self.df["engine_value"] = self.df["engine"].apply(extract)

    def extract_max_power(self):

        def extract(x):
            match = re.search(r"\d+\.?\d*", x)
            if match:
                return float(match.group())
            return np.nan

        self.df["max_power_value"] = self.df["max_power"].apply(extract)

    def drop_old_columns(self):
        self.df = self.df.drop(["mileage", "engine", "max_power", "torque"], axis=1)

    def encode_categorical(self):

        self.df["transmission"] = self.df["transmission"].apply(
            lambda x: 1 if x == "Manual" else 0
        )

        def seller_map(x):
            if x == "Individual":
                return 1
            elif x == "Dealer":
                return 0
            return -1

        self.df["seller_type"] = self.df["seller_type"].apply(seller_map)

        def fuel_map(x):
            if x == "Petrol":
                return 1
            elif x == "Diesel":
                return 0
            return -1

        self.df["fuel"] = self.df["fuel"].apply(fuel_map)

    def encode_owner(self):

        owners = pd.get_dummies(self.df["owner"])
        self.df = pd.concat([self.df, owners], axis=1)

    def process(self):
        """Runs full preprocessing pipeline"""
        self.remove_missing()
        self.extract_torque_rpm()
        self.extract_mileage()
        self.extract_engine()
        self.extract_max_power()
        self.drop_old_columns()
        self.encode_categorical()
        self.encode_owner()

        return self.df
