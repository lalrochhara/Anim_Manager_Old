if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = ""
    OWNER_ID = "1501128718" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_NAME = "SenuGamerBoy"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = https://<appname>.herokuapp.com/
    ENV = ANYTHING
    DEV_USERS = "1391755824"

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    PORT = None
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = "5c5adc2bc1832de6943e3f4467e84c39"
    CASH_API_KEY = "-xyz"
    GBAN_LOGS = [] # Gban log channel, include the hyphen too: ex: -123456 . Get ID From @AnimXinfo_Robot


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
