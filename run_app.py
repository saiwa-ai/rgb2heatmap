
import json
import os
import sys
from heatmap_pipeline import app

def load_config(default_path, override_path=None):
    with open(default_path, 'r') as f:
        config = json.load(f)

    if override_path and os.path.exists(override_path):
        with open(override_path, 'r') as f:
            override_config = json.load(f)
        config.update({k: v for k, v in override_config.items() if v is not None})

    return config

if __name__ == "__main__":
    override_config_path = sys.argv[1] if len(sys.argv) > 1 else None

    config = load_config('configs/config.json', override_config_path)

    # To trick the hydra 
    sys.argv = [sys.argv[0]]
    
    result = app.handler(config, "")

    print(json.dumps(result, indent=1))
