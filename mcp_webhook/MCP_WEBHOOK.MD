1.Google Apps Script ยิง HTTP POST มาที่ Webhook Endpoint port 8000 ตาม example.apps_script

2.MCP รับข้อมูล → เรียก @mcp.tool() เพื่อประมวลผล logic เช่น:
    สินค้าคงเหลือน้อย → แจ้งเตือน
    สินค้าหมด → สร้าง task ให้ restock
    หรือแม้แต่เขียนข้อมูลต่อไปยัง API อื่น ๆ เช่น POS หรือระบบ ERP

ง่ายๆคือ

Apps Script ยิง Webhook = ฝั่ง Google เป็นผู้ส่งข้อมูล
FastAPI ทำหน้าที่เป็น Webhook Receiver
โดย set trigger ให้ยิง “อัตโนมัติ” เช่น onEdit หรือตั้งว่าทุก every 10 นาที  (debug ผ่าน ngrok ได้)

ต้องเปิด MCP ผูก FastAPI ผ่าน stdio เพื่อให้เชื่อม claude desktop
และเปิด server uvicorn เพื่อเป็น webhook รอให้ Google Sheet POST เข้ามา แล้วทำอย่างอื่นได้
```commandline at root path 
#for mcp stdio
uvicorn mcp_webhook.webhook_server:app --host 127.0.0.1 --port 8000 --reload
#for api webhook
uvicorn mcp_webhook.main_webhook:app --host 127.0.0.1 --port 8001 --reload
```

