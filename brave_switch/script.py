#!/usr/bin/python
import json

images = [
    "beautiful_wal.webp",
    "bluemoonfall.webp",
    "colibri_bird.webp",
    "color_lion.webp",
    "cosmonaut-space-suit-multicolored.webp",
    "echo.webp",
    "elven-sancuary.webp",
    "ethernet_lion.webp",
    "fantasy-landscape1.webp",
    "fantasy-landscape2.webp",
    "fantasy-landscape4.webp",
    "fantasy-waterfall.webp",
    "galaxy-2560x1600.webp",
    "journey_in_middle_earth.webp",
    "koi-fishes-1920x1080.webp",
    "mikael-gustafsson-forest.webp",
    "moon_landscape.webp",
    "moon_sunset_landscape.webp",
    "mystery-3840x2160.webp",
    "pirate.webp",
    "river_rocks_planet.webp",
    "stary-night.webp",
    "styled_lion.webp",
    "sundown_landscape.webp",
    "wallpaper.webp"
]

def get_wallpaper_item(index, image_name):
    return {
        "name": f"ntp-2021-{index}",
        "source": f"{ image_name }",
        "author": "me",
        "link": "https://community.brave.com/",
        "originalUrl": "Contributor sent the hi-res version through email",
        "license": "used with permission"
    }
    

wallpapers = [get_wallpaper_item(i, img) for i, img in enumerate(images)]

photos = {
    "schemaVersion": 1,
    "images": wallpapers,
}

with open("photos.json", "w") as fd:
    json.dump(photos, fd)