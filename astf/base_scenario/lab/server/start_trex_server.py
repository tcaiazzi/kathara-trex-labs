from trex.examples.astf import astf_path
from trex.astf.api import *

import logging

logging.basicConfig(level=logging.INFO)

SERVER_IP = "127.0.0.1"
PROFILE_NAME = "test.py"
DURATION = -1

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

    c.stop()

except ASTFError as e:
    print(e)

finally:
    logging.info(f"Disconnecting from trex server...")
    c.disconnect()
