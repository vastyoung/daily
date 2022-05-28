import asyncio
import sys
from latency_lib import start_test_async


def main():
    ip_list = []

    for item in sys.argv[1:]:
        ip, port = item.split(":")
        ip_list.append({"ip": ip, "port": port})
    asyncio.run(start_test_async(ip_list))


if __name__ == "__main__":
    main()
