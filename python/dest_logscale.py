#! /usr/bin/env python3
import os
import jinja2
from yaml import safe_load, dump

config_path = os.environ.get("SEGWAY_CONFIG_PATH", "")
config_file = os.path.join(config_path, "config.yaml")


def main():
    plugin_path = os.path.dirname(os.path.abspath(__file__))

    templateLoader = jinja2.FileSystemLoader(searchpath=plugin_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    tm = templateEnv.get_template("dest_logscale.jinja")

    with open(config_file, "r") as file:
        config = safe_load(file)

    conf = tm.render(
        config=config,
        instance=os.environ.get("SEGWAY_DEST_LOGSCALE_INSTANCE", "unknown_instance"),
        url=os.environ.get("SEGWAY_DEST_LOGSCALE_URL", "unknown_url"),
    )
    print(conf)


if __name__ == "__main__":
    main()
