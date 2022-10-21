import toml

from app.config import CoevalConfig


def test_load_from_file(tmp_path, mocker):
    dummy_cache_file = tmp_path / "dummy-config.toml"
    config_dict = {
        "default_format": "YYYY-MM-DD",
    }
    dummy_cache_file.write_text(toml.dumps(config_dict))
    mocker.patch("app.config.CONFIG_FILE", new=dummy_cache_file)

    config_instance = CoevalConfig.load_from_file()
    assert config_instance.default_format == "YYYY-MM-DD"
