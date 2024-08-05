from python_logging import log
import cli


if __name__ == "__main__":
    try:
        cli.cli_logic()
    except Exception as error_message:
        log.log_message(str(error_message))
