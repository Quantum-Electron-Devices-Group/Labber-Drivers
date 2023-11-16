from pathlib import Path
import json
from zhinst.labber.driver.base_instrument import BaseDevice

SETTINGSFILE = "settings.json"


class Driver(BaseDevice):
    """Labber driver for the Zurich Instruments DataServer."""

    def __init__(self, *args, **kwargs):
        settings_file = Path(__file__).parent / SETTINGSFILE
        with settings_file.open("r") as file:
            settings = json.loads(file.read())
        super().__init__(*args, settings=settings, **kwargs)
