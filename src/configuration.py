class Config:
    font = { "size": 20, "color": (255, 255, 255), "path": "font/PixelMplus10-Regular.ttf" }
    screen = { "width": 480, "height": 480, "bg_color": (10, 10, 10) }
    field = { "coordinate": (0, 0), "path": "img/field.png" }
    background = { "coordinate": (150, 90), "size": (210, 210), "path": "img/background.jpg" }
    command = {
        "window_coordinate": (210, 10), "window_size": (210, 90),  "window_color": (0, 0, 0),
        "border_width": 10, "border_color": (255, 255, 255),
        "option_coordinates": [
            (235, 20), (335, 20), 
            (235, 60), (335, 60)
        ],
        "cursor_coordinates": [
            (217, 20), (317, 20),
            (217, 60), (317, 60)
        ]
    }
    log = {
        "window_coordinate": (90, 300), "window_size": (300, 150), "window_color": (0, 0, 0),
        "border_width": 10, "border_color": (255, 255, 255),
    }

    spell = {
        "mera": { "label": "メラ", "mp": 2, "damage": 10, "type": "attack" },
        "hoimi": { "label": "ホイミ", "mp": 3, "damage": -20, "type": "heal" }, 
    }
    player = {
        "window_coordinate": (30, 10), "window_size": (120, 130), "window_color": (0, 0, 0),
        "border_width": 10, "border_color": (255, 255, 255),
        "name_coordinate": (40, 20), "level_coordinate": (40, 50), "hp_coordinate": (40, 80), "mp_coordinate": (40, 110),
        "status": {
            "attack": 5,
            "name": "ゆうしゃ",
            "level": 1,
            "hp": 10,
            "mp": 5,
            "spell": {
                "mera": { "label": "メラ", "mp": 2, "damage": 10, "type": "attack" },
                "hoimi": { "label": "ホイミ", "mp": 3, "damage": -20, "type": "heal" }, 
            }
        }
    }
    enemy = {
        "slime": {
            "path": "img/slime.png",
            "size": (90, 90),
            "coordinate": (210, 180),
            "status": {
                "name": "スライム",
                "hp": 20,
                "mp": 0,
                "attack": 10,
                "spell": {}
            },
        }
    }