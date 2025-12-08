from config_access import Config


class Experiment:
    def __init__(self, config: Config) -> None:
        self.config = config

    def load_data(self) -> None:
        """
        Load the data from the config.
        """
        data_path = self.config.get("data_path")
        if data_path is None:
            raise ValueError("Data path not found in config")
        print(f"Loading data from {data_path}")

    def load_model(self) -> None:
        """
        Load the model from the config.
        """
        model_path = self.config.get("model_path")
        if model_path is None:
            raise ValueError("Model path not found in config")
        print(f"Loading model from {model_path}")

    def run(self) -> None:
        """
        Run the experiment.
        """
        self.load_data()
        self.load_model()
