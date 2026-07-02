import argparse
import sys

from cloudmortem.command_registry import COMMANDS
from cloudmortem.logger import get_logger
from cloudmortem.service import Success, Failure

logger = get_logger()


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cloudmortem",
        description="CloudMortem - Service execution simulator",
    )

    # Backward compatibility flags
    parser.add_argument("--fail", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--version", action="store_true")

    # Subcommands
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--fail", action="store_true")
    run_parser.add_argument("--json", action="store_true")

    subparsers.add_parser("version")
    subparsers.add_parser("inventory")  # <-- FIX: ensure allowed choice exists

    return parser


def emit(message: str) -> None:
    print(message)


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    parser = build_parser()
    args, _ = parser.parse_known_args(argv)

    # Backward compatibility
    if args.version:
        command = "version"
    else:
        command = args.command or "run"

    handler = COMMANDS.get(command)

    if handler is None:
        emit("Unknown command")
        return 2

    if command == "version":
        result, output = handler(args)
        emit(output)
        logger.info(output)
        return 0

    emit("CloudMortemService run started")

    result, output = handler(args)

    emit(output)

    if isinstance(result, Failure):
        return 1

    if isinstance(result, Success):
        return 0

    emit("Unknown result")
    return 2


if __name__ == "__main__":
    sys.exit(main())
