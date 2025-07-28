from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import logging
logging.basicConfig(level=logging.DEBUG)

mcp = FastMCP("project_blog")

mock_api_url = "https://688246f466a7eb81224e1540.mockapi.io/blogs"

@mcp.tool()
def get_blogs():
    response = httpx.get(mock_api_url)
    return response.json()

@mcp.tool()
def search_blogs(query: str):
    response = httpx.get(mock_api_url, params={"title": query})
    return response.json()

@mcp.tool()
def add_blog(title: str, body: str):
    response = httpx.post(mock_api_url, json={"title": title, "body": body})
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server...")
    mcp.run(transport='stdio')
    print("MCP server is running.")
