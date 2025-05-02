import os
from pathlib import Path
import yaml
from .parameters import settings
config_file = os.path.join(settings.boavizta_api_data_dir, 'config.yml')
config = yaml.safe_load(Path(config_file).read_text())