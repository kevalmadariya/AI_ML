import random
import logging
from mcp.server.fastmcp import FastMCP
import os

# Configure logging to stderr (NOT stdout for STDIO transport)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "temp.txt")


# Initialize FastMCP server
mcp = FastMCP(name="expense-tracker")

@mcp.tool()
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    logger.info(f"Rolling {n_dice} dice")
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    logger.info(f"Adding {a} + {b}")
    return a + b

@mcp.resource("expense://categories", mime_type="text/plain")
def categories():
    # Read fresh each time so you can edit the file without restarting
    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return f.read()
    
def main():
    """Initialize and run the MCP server"""
    logger.info("Starting expense-tracker MCP server")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()