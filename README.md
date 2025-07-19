# hass-photoprism
Home assistant integration for photoprism

Sensors for all PhotoPrism entities (albums, pictures, places, ...) 

# Installation:
### Using HACS:
1. Open HACS
2. In top right corner, click on the 3 dots and select "Custom repositories"
3. add this repo, and select type "Integration"
4. search for photoprism in HACS and select download.
5. restart HA
6. Open Settings -> "Devices & services"
7. click "Add integration" and search for photoprism
8. fill in the form and Submit.
9. Restart HA

## Sensors:  
| Entity ID | State | Attributes |
|-----------|-------|------------|
update.photoprism_update | off | auto_update, display_precision, entity_picture, friendly_name, in_progress, installed_version, latest_version, release_summary, release_url, skipped_version, supported_features, title, update_percentage: False, 0, https://brands.home-assistant.io/_/photoprism/icon.png, Photoprism update, False, v1.0.1, v1.0.1, None, https://github.com/ice413/hass-photoprism/releases/v1.0.1, None, 23, None, None
sensor.photoprism_all | 36445 | friendly_name, icon, unit_of_measurement: Photoprism all, mdi:image, Pcs
sensor.photoprism_photos | 35020 | friendly_name, icon, unit_of_measurement: Photoprism photos, mdi:image, Pcs
sensor.photoprism_media | 1425 | friendly_name, icon, unit_of_measurement: Photoprism media, mdi:image, Pcs
sensor.photoprism_animated | 19 | friendly_name, icon, unit_of_measurement: Photoprism animated, mdi:image, Pcs
sensor.photoprism_live | 763 | friendly_name, icon, unit_of_measurement: Photoprism live, mdi:image, Pcs
sensor.photoprism_audio | 0 | friendly_name, icon, unit_of_measurement: Photoprism audio, mdi:image, Pcs
sensor.photoprism_videos | 643 | friendly_name, icon, unit_of_measurement: Photoprism videos, mdi:image, Pcs
sensor.photoprism_documents | 0 | friendly_name, icon, unit_of_measurement: Photoprism documents, mdi:image, Pcs
sensor.photoprism_cameras | 54 | friendly_name, icon, unit_of_measurement: Photoprism cameras, mdi:image, Pcs
sensor.photoprism_lenses | 341 | friendly_name, icon, unit_of_measurement: Photoprism lenses, mdi:image, Pcs
sensor.photoprism_countries | 9 | friendly_name, icon, unit_of_measurement: Photoprism countries, mdi:image, Pcs
sensor.photoprism_hidden | 0 | friendly_name, icon, unit_of_measurement: Photoprism hidden, mdi:image, Pcs
sensor.photoprism_archived | 38 | friendly_name, icon, unit_of_measurement: Photoprism archived, mdi:image, Pcs
sensor.photoprism_favorites | 0 | friendly_name, icon, unit_of_measurement: Photoprism favorites, mdi:image, Pcs
sensor.photoprism_review | 0 | friendly_name, icon, unit_of_measurement: Photoprism review, mdi:image, Pcs
sensor.photoprism_stories | 0 | friendly_name, icon, unit_of_measurement: Photoprism stories, mdi:image, Pcs
sensor.photoprism_private | 0 | friendly_name, icon, unit_of_measurement: Photoprism private, mdi:image, Pcs
sensor.photoprism_albums | 14 | friendly_name, icon, unit_of_measurement: Photoprism albums, mdi:image, Pcs
sensor.photoprism_private_albums | 0 | friendly_name, icon, unit_of_measurement: Photoprism private_albums, mdi:image, Pcs
sensor.photoprism_moments | 34 | friendly_name, icon, unit_of_measurement: Photoprism moments, mdi:image, Pcs
sensor.photoprism_private_moments | 0 | friendly_name, icon, unit_of_measurement: Photoprism private_moments, mdi:image, Pcs
sensor.photoprism_months | 254 | friendly_name, icon, unit_of_measurement: Photoprism months, mdi:image, Pcs
sensor.photoprism_private_months | 0 | friendly_name, icon, unit_of_measurement: Photoprism private_months, mdi:image, Pcs
sensor.photoprism_states | 9 | friendly_name, icon, unit_of_measurement: Photoprism states, mdi:image, Pcs
sensor.photoprism_private_states | 0 | friendly_name, icon, unit_of_measurement: Photoprism private_states, mdi:image, Pcs
sensor.photoprism_folders | 582 | friendly_name, icon, unit_of_measurement: Photoprism folders, mdi:image, Pcs
sensor.photoprism_private_folders | 0 | friendly_name, icon, unit_of_measurement: Photoprism private_folders, mdi:image, Pcs
sensor.photoprism_files | 37236 | friendly_name, icon, unit_of_measurement: Photoprism files, mdi:image, Pcs
sensor.photoprism_people | 35 | friendly_name, icon, unit_of_measurement: Photoprism people, mdi:image, Pcs
sensor.photoprism_places | 274 | friendly_name, icon, unit_of_measurement: Photoprism places, mdi:image, Pcs
sensor.photoprism_labels | 186 | friendly_name, icon, unit_of_measurement: Photoprism labels, mdi:image, Pcs
sensor.photoprism_labelmaxphotos | 6756 | friendly_name, icon, unit_of_measurement: Photoprism labelMaxPhotos, mdi:image, Pcs