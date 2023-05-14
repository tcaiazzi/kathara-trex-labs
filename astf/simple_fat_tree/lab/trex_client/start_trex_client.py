import os

from trex.astf.trex_astf_client import ASTFClient
from trex.astf.trex_astf_exceptions import ASTFError
from trex.examples.astf import astf_path


import logging

logging.basicConfig(level=logging.INFO)

SERVER_IP = "127.0.0.1"
PROFILE_NAME = "http_simple.py"
DURATION = 60

if __name__ == '__main__':
    logging.info(f"Connecting to trex server: {SERVER_IP}")
    c = ASTFClient(server=SERVER_IP)
    # connect to server
    c.connect()

    try:
        c.reset()

        # load ASTF profile
        profile_path = os.path.join(astf_path.get_profiles_path(), PROFILE_NAME)

        logging.info(f"Loading profile: {profile_path}")
        c.load_profile(profile_path)

        logging.info(f"Starting traffic...")
        # infinite duration, need to call stop
        c.start(mult=1, duration=DURATION)

        c.wait_on_traffic()

        logging.info(f"Stopping traffic...")
        # stop traffic
        c.stop()

    except ASTFError as e:
        print(e)

    finally:
        logging.info(f"Disconnecting from trex server...")
        c.disconnect()
