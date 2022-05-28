import asyncio
import json
from latency_lib import start_test_async
from argparse import ArgumentParser

arg_parser = ArgumentParser(description="latency test")

arg_parser.add_argument(
    '-f', '--input-file',
    action='store',
    default='./ip_list.json',
    help="path to ip_list.json"
)

args = arg_parser.parse_args()


def main():
    with open(args.input_file, "rt") as f:
        data = json.load(f)
        ip_list = data["ip_list"]

    asyncio.run(start_test_async(ip_list))


if __name__ == "__main__":
    main()
