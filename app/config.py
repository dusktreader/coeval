import pathlib
import typing

import pendulum
import toml
from attrs import define
from cattrs import structure, unstructure


CACHE_DIR = pathlib.Path.home() / ".cache" / "coeval"
CONFIG_FILE = CACHE_DIR / "config.toml"


@define
class CoevalConfig:
    default_format: str = "YYYY-MM-DD HH:mm:ss"

    @classmethod
    def load_from_file(cls):
        config_dict = toml.loads(CONFIG_FILE.read_text())
        return structure(config_dict, cls)

    def write_to_file(self):
        config_dict = unstructure(self)
        CONFIG_FILE.write_text(toml.dumps(config_dict))
