from fastapi import FastAPI, Request
from mcp.server.fastmcp import FastMCP

import logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
mcp = FastMCP("project_blog_webhook", app=app)


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service.sheet_service import get_sheet

# แล้วรันแบบเดิม
# uvicorn mcp_webhook.main_mcp_server:app --host 127.0.0.1 --port 8000 --reload

@mcp.tool()
def get_low_stock_products():
    sheet = get_sheet()
    data = sheet.get_all_records()

    # ดึงเฉพาะสินค้าที่ stock <= 3
    low_stock = [row for row in data if int(row["stock"]) <= 3]
    return low_stock


@mcp.tool()
def update_stock(product_name: str, new_stock: int):
    sheet = get_sheet()  # <- ตอนนี้เป็น worksheet แล้ว
    records = sheet.get_all_records()

    for idx, row in enumerate(records):
        if row["product_name"] == product_name:
            cell = f"B{idx + 2}"  # B คือตำแหน่ง stock
            sheet.update(cell, [[new_stock]])  # ต้องเป็น list of list
            return f"✅ Updated {product_name} stock to {new_stock}"

    return f"❌ Not found product: {product_name}"
@app.post("/update_stock_by_api")
async def update_stock_by_api(request: Request):
    payload = await request.json()
    print("received:", payload)

    result = update_stock(
        payload["product_name"], payload["stock"]
    )
    return {"status": "ok", "result": result}

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server...")
    mcp.run(transport='stdio')
    print("MCP server is running.")

# uvicorn mcp_webhook.main_mcp_server:app --host 127.0.0.1 --port 8000 --reload