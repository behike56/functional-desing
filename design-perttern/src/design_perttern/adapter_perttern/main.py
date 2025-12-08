import json
from pathlib import Path
from bs4 import BeautifulSoup

from experiment import Experiment

from basic.xml_adapter import XMLConfig as XMLConfigBasic
from class_base.xml_adapter import XMLConfig as XMLConfigClassBase


def load_config_json():
    config_path = Path(__file__).with_name("config.json")
    with config_path.open("r", encoding="utf-8") as f:
        config = json.load(f)
    experiment = Experiment(config)
    experiment.run()


def load_config_xml():
    config_path = Path(__file__).with_name("config.xml")
    with config_path.open("r", encoding="utf-8") as f:
        config = f.read()

    bs = BeautifulSoup(config, "xml")
    adapter = XMLConfigBasic(bs)
    experiment = Experiment(adapter)
    experiment.run()


def load_config_xml_class_base():
    config_path = Path(__file__).with_name("config.xml")
    with config_path.open("r", encoding="utf-8") as f:
        config = f.read()
    # bs = BeautifulSoup(config, "xml")
    # bs.get()
    adapter = XMLConfigClassBase(config, "xml")
    experiment = Experiment(adapter)
    experiment.run()


def main():
    load_config_json()
    load_config_xml()
    load_config_xml_class_base()


if __name__ == "__main__":
    main()
