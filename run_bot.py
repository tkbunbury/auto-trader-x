from bot import Bot
from infrastructure.instrument_collection import instrumentCollection


# DISCLAIMER:
# This code is for educational and display purposes only.
# It should not be run as is. The author is not responsible for any financial losses or damages caused by the use of this code.

if __name__ == "__main__":
    instrumentCollection.LoadInstrumentsDB()
    b = Bot()
    b.run()