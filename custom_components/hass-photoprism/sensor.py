"""Support for monitoring the photoprism instance."""

import logging

import aiophotoprism
from homeassistant.const import CONF_NAME
from homeassistant.exceptions import PlatformNotReady
from homeassistant.helpers.update_coordinator import (CoordinatorEntity,
                                                      DataUpdateCoordinator,
                                                      UpdateFailed)

from .const import DOMAIN, PHOTO_SENSOR_DEFAULT_ICON, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the photoprism sensors."""

    name = config_entry.data[CONF_NAME]
    photoprism = hass.data[DOMAIN][name]

    async def async_update_data():
        try:
            return await photoprism.config()
        except aiophotoprism.exceptions.PhotoprismError as err:
            raise UpdateFailed from err

    try:
        config = await photoprism.config()
        coordinator = DataUpdateCoordinator(
            hass,
            _LOGGER,
            name="sensor",
            update_method=async_update_data,
            update_interval=SCAN_INTERVAL,
        )
        await coordinator.async_refresh()
        dev = [
            PhotoCountSensor(coordinator, name, k, config.version)
            for k, v in config.count.items()
        ]
        async_add_entities(dev)

    except aiophotoprism.exceptions.PhotoprismError as exception:
        raise PlatformNotReady from exception


class PhotoCountSensor(CoordinatorEntity):
    """A photoprism photo count sensor."""

    def __init__(self, coordinator, name, sensor_name, version):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._name = name
        self._sensor_name = sensor_name
        self._version = version

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name} {self._sensor_name}"

    @property
    def unique_id(self):
        """Return the unique id of the entity."""
        return f"{DOMAIN}-{self._name}-{self._sensor_name}"

    @property
    def state(self):
        """Return the state of the sensor."""
        if not self.available:
            return
        return self.coordinator.data.count[self._sensor_name]

    @property
    def icon(self):
        """Return the icon for this sensor."""
        return PHOTO_SENSOR_DEFAULT_ICON

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement for this sensor."""
        return "Pcs"

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, self._name)},
            "name": self._name,
            "manufacturer": "Photoprism Team",
            "sw_version": self._version,
            "entry_type": "service",
        }
