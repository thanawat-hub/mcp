1.Google Sheet มีสูตรหรือ script แจ้งเตือนเมื่อมีการเปลี่ยนแปลง (เช่น ผ่าน Google Apps Script)
2.Google Apps Script ยิง HTTP POST มาที่ MCP Webhook Endpoint
3.MCP รับข้อมูล → เรียก @mcp.tool() เพื่อประมวลผล logic เช่น:
    สินค้าคงเหลือน้อย → แจ้งเตือน
    สินค้าหมด → สร้าง task ให้ restock
    หรือแม้แต่เขียนข้อมูลต่อไปยัง API อื่น ๆ เช่น POS หรือระบบ ERP


# MCP ที่ใช้แบบ transport='stdio' จะยังรับ webhook HTTP ไม่ได้
# คุณต้องเปิด MCP ผ่าน FastAPI หรือ Flask เพื่อให้ Google Sheet POST เข้าได้
```commandline at root path 
#for mcp
uvicorn mcp_webhook.webhook_server:app --host 127.0.0.1 --port 8000 --reload
#for api
uvicorn mcp_webhook.main_webhook:app --host 127.0.0.1 --port 8001 --reload
```

