import logging 
import os 
from datetime import datetime

# Folder where logs will be stored
LOG_DIR = "logs"
# Create the folder if it doesn't exist 
os.makedirs(LOG_DIR, exist_ok=True)

# Create a unique log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Full path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logger Configuration
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level = logging.INFO
)

# Create logger object 
logger = logging.getLogger("smartgridLogger")