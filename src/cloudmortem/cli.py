import argparse
import sys

from cloudmortem.command_registry import COMMANDS
from cloudmortem.logger import get_logger

logger = get_logger()


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cloudmortem", description="CloudMortem - Service execution simulator"
    )

    # backward compatibility flags (tests depend on these)
    parser.add_argument("--fail", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--version", action="store_true")

    # subcommands (future-ready)
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--fail", action="store_true")
    run_parser.add_argument("--json", action="store_true")

    subparsers.add_parser("version")

    return parser


def emit(message: str) -> None:
    print(message)


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    parser = build_parser()
    args, _ = parser.parse_known_args(argv)

    command = args.command or "run"

    handler = COMMANDS.get(command)

    if not handler:
        emit("Unknown command")
        return 2

    if command == "version":
        output, code = handler(args)
        emit(output)
        logger.info(output)
        return code

    emit("CloudMortemService run started")

    result, output = handler(args)

    emit(output)

    if getattr(result, "status", None) == "error":
        return 1

    if getattr(result, "status", None) == "success":
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
