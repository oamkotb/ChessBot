import logging

'''
SETUP LOGGER
'''

# Logging formatter
class LoggingFormatter(logging.Formatter):
    # Colors
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    GRAY = "\x1b[38m"
    
    # Styles
    RESET = "\x1b[0m"
    BOLD = "\x1b[1m"

    COLORS = {
        logging.DEBUG: GRAY + BOLD,
        logging.INFO: BLUE + BOLD,
        logging.WARNING: YELLOW + BOLD,
        logging.ERROR: RED,
        logging.CRITICAL: RED + BOLD
    }
    
    def format(self, record: str):
        log_color: str = self.COLORS(record.levelno)
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.BLACK + self.BOLD)
        format = format.replace("(reset)", self.RESET)
        format = format.replace("(green)", self.GREEN)
        format = format.replace("(green)", self.GREEN + self.BOLD)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)

logger: logging.Logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO)

# Console handler
console_handler: logging.StreamHandler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())

# File handler
file_handler: logging.FileHandler = logging.FileHandler(filename = "discord.log", encoding = "utf-8", mode = "w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)
