import os
import yaml

DEFAULTS = {
    "blur_threshold": 100.0,
    "min_pixels": 2_000_000,
    "check_commons": True,
    "request_delay_seconds": 1.0,
}


def load_config(path="config.yaml"):
    cfg = dict(DEFAULTS)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            cfg.update(yaml.safe_load(f) or {})
    return cfg