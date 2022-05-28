from fastapi import FastAPI, Request
from latency_lib import start_test_async

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello world"}


@app.post("/latency_test")
async def latency_test(request: Request):
    data = await request.json()
    ip_list = data["ip_list"]
    res = await start_test_async(ip_list)
    return {"res": res}
