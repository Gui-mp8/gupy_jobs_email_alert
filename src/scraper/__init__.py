import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the desired log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a logger object
logger = logging.getLogger(__name__)

logging.info(f'STARTING: {__name__} aplication')