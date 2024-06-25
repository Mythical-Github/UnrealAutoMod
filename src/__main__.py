import cli
import log


if __name__ == "__main__":
    try:
        cli.cli_logic()
    except Exception as error_message:
        log.log_message(error_message)
