"""The Photoprism integration."""
import logging
import aiophotoprism
import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (CONF_NAME, CONF_PASSWORD, CONF_URL,
                                 CONF_USERNAME, CONF_VERIFY_SSL)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, SERVICE_INDEX

PLATFORMS = ["sensor"]

_LOGGER = logging.getLogger(__name__)


SERVICE_INDEX_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_NAME): cv.string,
    }
)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Photoprism component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Photoprism from a config entry."""
    data = entry.data

    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    name = data[CONF_NAME]

    client = aiophotoprism.Photoprism(
        data[CONF_USERNAME],
        data[CONF_PASSWORD],
        url=data[CONF_URL],
        verify_ssl=data[CONF_VERIFY_SSL],
    )

    hass.data[DOMAIN][name] = client

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    async def async_index(service):
        name = service.data[CONF_NAME]
        client = hass.data[DOMAIN][name]
        return await client.index()

    hass.services.async_register(
        DOMAIN, SERVICE_INDEX, async_index, schema=SERVICE_INDEX_SCHEMA
    )

    return True


async def async_unload_entry(hass, config_entry) -> bool:
    """Unload Transmission Entry from config_entry."""
    client = hass.data[DOMAIN].pop(config_entry.entry_id)
    client.close()

    for platform in PLATFORMS:
        await hass.config_entries.async_forward_entry_unload(config_entry, platform)

    if not hass.data[DOMAIN]:
        hass.services.async_remove(DOMAIN, SERVICE_INDEX)

    return True
