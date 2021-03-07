"""Constants for the Photoprism integration."""
from datetime import timedelta

DOMAIN = "photoprism"
DEFAULT_NAME = "Photoprism"

DEFAULT_VERIFY_SSL = True

DEFAULT_URL = "http://127.0.0.1:2342"

RECONNECT_INTERVAL = timedelta(seconds=10)
SCAN_INTERVAL = timedelta(seconds=30)

PHOTO_SENSOR_DEFAULT_ICON = "mdi:image"
