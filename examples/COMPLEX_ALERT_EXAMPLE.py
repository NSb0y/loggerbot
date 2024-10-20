from loggerbot import TelegramLoggingBot
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

print("Debug: Starting COMPLEX_ALLERT_EXAMPLE.py")

# Use environment variables
TELEGRAM_BOT_TOKEN = "APIKEY"
TELEGRAM_CHAT_ID = ["USER_CHAT_ID"]

logger.debug(f"Chat ID: {TELEGRAM_CHAT_ID}")

if not TELEGRAM_CHAT_ID or not all(chat_id.isdigit() for chat_id in TELEGRAM_CHAT_ID):
    logger.error("Invalid TELEGRAM_CHAT_ID. Please provide a valid numeric chat ID.")
    print("Error: Invalid TELEGRAM_CHAT_ID. Please provide a valid numeric chat ID.")
else:
    try:
        # Initialize the logging bot
        LOGBOT = TelegramLoggingBot(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
        logger.info("TelegramLoggingBot initialized successfully")

        # Example usage
        logger.debug("Sending warning message")
        LOGBOT.warning("This is a warning message")
        
        logger.debug("Sending alert message")
        LOGBOT.alert("This is an alert message")
        
        logger.debug("Sending complete message")
        LOGBOT.complete("Task completed successfully")
        
        logger.debug("Sending info message")
        LOGBOT.info("This is an informational message")
        
        logger.debug("Sending error message")
        LOGBOT.error("An <i>error</i> <code>occurred for test</code>")

        # Wait for all messages to be sent
        LOGBOT.message_queue.join()
        logger.info("All messages have been sent")

    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        print("error")

print("Debug: Finished COMPLEX_ALLERT_EXAMPLE.py")
