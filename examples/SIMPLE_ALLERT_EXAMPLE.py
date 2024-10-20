from loggerbot import TelegramLoggingBot

# Use environment variables
TELEGRAM_BOT_TOKEN = "APIKEY"
TELEGRAM_CHAT_ID = ["USER_CHAT_ID"]


if not TELEGRAM_CHAT_ID or not all(chat_id.isdigit() for chat_id in TELEGRAM_CHAT_ID):
    print("Error: Invalid TELEGRAM_CHAT_ID. Please provide a valid numeric chat ID.")
else:
    try:
        # Initialize the logging bot
        LOGBOT = TelegramLoggingBot(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)

        # Example usage
        LOGBOT.warning("This is a warning message")
        
        LOGBOT.alert("This is an alert message")
        
        LOGBOT.complete("Task completed successfully")
        
        LOGBOT.info("This is an informational message")
        
        LOGBOT.error("An <i>error</i> <code>occurred for test</code>")

        # Wait for all messages to be sent
        LOGBOT.message_queue.join()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

