# Logging: Personalización
import logging
from pathlib import Path


class SinInfoFilter(logging.Filter):
    """Filtro que descarta los mensajes de nivel INFO."""

    def filter(self, record: logging.LogRecord) -> bool:
        # Devolver False descarta el registro; True lo deja pasar
        return record.levelno not in [logging.INFO, logging.ERROR, logging.CRITICAL]


# Formato común para ambos handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
formatter2 = logging.Formatter(
    "%(message)s"
)
sin_info = SinInfoFilter()

# Handler de consola: nivel DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
console_handler.addFilter(sin_info)

# Handler de archivo: nivel WARNING
log_file = Path(__file__).parent / "app.log"
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter2)

# Logger: debe estar en DEBUG para que los mensajes lleguen a los handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


if __name__ == "__main__":
    logger.debug("Mensaje DEBUG -> solo consola")
    logger.info("Mensaje INFO -> no aparece en ningún sitio (filtrado)")
    logger.warning("Mensaje WARNING -> consola y archivo")
    logger.error("Mensaje ERROR -> consola y archivo")
    logger.critical("Mensaje CRITICAL -> consola y archivo")
