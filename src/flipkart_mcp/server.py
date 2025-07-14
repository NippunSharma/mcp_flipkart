"""
Main server module for the Flipkart MCP Server.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, '..')) # the project root dir.

from mcp.server.fastmcp import FastMCP

# Handle both relative and absolute imports
try:
    from .config import SERVER_NAME, RESOURCE_URIS
    from .tools import search_products, get_product_details, search_by_price_range
    from .resources import get_search_help, get_product_help, get_api_status, get_server_info
    from .prompts import get_search_results, get_product_info, find_best_deals, compare_products, track_price_range, seasonal_deals, gift_recommendations
except ImportError:
    # Fall back to absolute imports when running directly
    from flipkart_mcp.config import SERVER_NAME, RESOURCE_URIS
    from flipkart_mcp.tools import search_products, get_product_details, search_by_price_range
    from flipkart_mcp.resources import get_search_help, get_product_help, get_api_status, get_server_info
    from flipkart_mcp.prompts import get_search_results, get_product_info, find_best_deals, compare_products, track_price_range, seasonal_deals, gift_recommendations


def create_server() -> FastMCP:
    """Create and configure the FastMCP server with all tools, resources, and prompts."""
    
    # Initialize the MCP server
    mcp = FastMCP(SERVER_NAME, host="0.0.0.0", port=8000)
    
    # Register Tools (Model-Controlled)
    mcp.tool()(search_products)
    mcp.tool()(get_product_details)
    mcp.tool()(search_by_price_range)
    
    # Register Resources (Application-Controlled)
    mcp.resource(RESOURCE_URIS["search_help"])(get_search_help)
    mcp.resource(RESOURCE_URIS["product_help"])(get_product_help)
    mcp.resource(RESOURCE_URIS["api_status"])(get_api_status)
    mcp.resource("flipkart://api/server-info")(get_server_info)
    
    # Register Prompts (User-Controlled)
    mcp.prompt(title="Get Search Results")(get_search_results)
    mcp.prompt(title="Get Product Information")(get_product_info)
    mcp.prompt(title="Find Best Deals")(find_best_deals)
    mcp.prompt(title="Compare Products")(compare_products)
    mcp.prompt(title="Track Price Range")(track_price_range)
    mcp.prompt(title="Seasonal Deals Finder")(seasonal_deals)
    mcp.prompt(title="Gift Recommendations")(gift_recommendations)
    
    return mcp


# Create the main server instance
server = create_server()


def main() -> None:
    """Main entry point for the server."""
    server.run(transport="streamable-http")


if __name__ == "__main__":
    main() 