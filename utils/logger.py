import logging

def setup_logger():
    """Настраивает логгер для бота"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S"
    )
    return logging.getLogger("vk_bot")

# Создаём логгер
logger = setup_logger()