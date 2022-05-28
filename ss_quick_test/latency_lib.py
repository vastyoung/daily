import time
import asyncio


async def start_test_async(ip_list):
    task_list = []
    for item in ip_list:
        task_list.append(connect_test(item["ip"], item["port"]))

    res = await asyncio.gather(*task_list)
    return res


async def connect_test(ip, port):
    start = time.time()
    latency = 0

    reader, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=3)
    latency = (time.time() - start) * 1000

    latency = f"{latency:.2f} ms"

    print(f"ip={ip} port={port} latency={latency}")
    return {"ip": ip, "port": port, "latency": latency}
