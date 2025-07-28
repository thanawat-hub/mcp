# main.py
from mcp_webhook.main_mcp_server import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, reload=True)

# must run at root
# uvicorn mcp_webhook.main_webhook:app --host 127.0.0.1 --port 8001 --reload
# ใช้ ngrok เปิด ท่อ เพื่อให้เปิดเป็น server webhook รับค่าต่างๆ มาจาก google script
# ngrok http 8001
