#! /usr/bin/env python3
import os
import jinja2
from furl import furl
from yaml import safe_load, dump
from dotenv import load_dotenv
load_dotenv()


config_path = os.environ.get("SEGWAY_CONFIG_PATH", "")
config_file = os.path.join(config_path, "config.yaml")

SEGWAY_DEST_LOGSCALE_HOST = os.environ.get("SEGWAY_DEST_LOGSCALE_HOST", "")
SEGWAY_DEST_LOGSCALE_PORT = os.environ.get("SEGWAY_DEST_LOGSCALE_PORT", "")
SEGWAY_DEST_LOGSCALE_PROTOCOL = os.environ.get("SEGWAY_DEST_LOGSCALE_PROTOCOL", "")
SEGWAY_DEST_LOGSCALE_TOKEN = os.environ.get("SEGWAY_DEST_LOGSCALE_TOKEN", "")
SEGWAY_DEST_LOGSCALE_INSTANCE_NAME = os.environ.get("SEGWAY_DEST_LOGSCALE_INSTANCE_NAME", "unknown_instance")
if SEGWAY_DEST_LOGSCALE_PORT == "":
    SEGWAY_DEST_LOGSCALE_PORT = None
    
def main():

    logscaleURL = furl().set(
        netloc = SEGWAY_DEST_LOGSCALE_HOST,
        scheme = SEGWAY_DEST_LOGSCALE_PROTOCOL,
        port = SEGWAY_DEST_LOGSCALE_PORT
    )
    url = logscaleURL.origin
    
    plugin_path = os.path.dirname(os.path.abspath(__file__))

    templateLoader = jinja2.FileSystemLoader(searchpath=plugin_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    tm = templateEnv.get_template("dest_logscale.jinja")

    with open(config_file, "r") as file:
        config = safe_load(file)

    for logPath in config['logPaths']:
        if "flow-control" not in logPath['flags']:
            logPath['flags'].append("flow-control")
        if 'tags' not in logPath:
            logPath['tags'] = []
                
    conf = tm.render(
        config=config,
        instance=SEGWAY_DEST_LOGSCALE_INSTANCE_NAME,
        url=url,
        token = SEGWAY_DEST_LOGSCALE_TOKEN
    )
    print(conf)


if __name__ == "__main__":
    main()
