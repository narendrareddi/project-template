import logging
import os
from datetime import datetime

# Generate a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory
log_path = os.path.join(os.getcwd(), "logs")

# Create the log directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Full path to the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# Logger instance if needed (optional)
logger = logging.getLogger(__name__)
