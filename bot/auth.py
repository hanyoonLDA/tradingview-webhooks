import hashlib
from dotenv import load_dotenv
load_dotenv(dotenv_path='config.env')

"""
Planning to add more here eventually, for now will be used for handling keys.
"""

# Set this to something unique.
pin = str(os.getenv("USER_PIN"))


# Generate unique token from pin.  This adds a marginal amount of security.
def get_token():
    token = hashlib.sha224(pin.encode('utf-8'))
    return token.hexdigest()
