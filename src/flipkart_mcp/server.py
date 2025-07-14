"""
Main server module for the Flipkart MCP Server.
"""
import sys
import os
import argparse

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


def create_server(transport: str = "stdio", host: str = "localhost", port: int = 8000) -> FastMCP:
    """Create and configure the FastMCP server with all tools, resources, and prompts.
    
    Args:
        transport: Transport type - "stdio" or "streamable-http"
        host: Host to bind to (only used for streamable-http)
        port: Port to bind to (only used for streamable-http)
    """
    
    # Initialize the MCP server with conditional parameters
    if transport == "streamable-http":
        mcp = FastMCP(SERVER_NAME, host=host, port=port)
    else:
        # For stdio transport, don't specify host/port
        mcp = FastMCP(SERVER_NAME)
    
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


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Flipkart MCP Server - Provides access to Flipkart e-commerce API via MCP protocol"
    )
    
    parser.add_argument(
        "--transport",
        choices=["stdio", "streamable-http"],
        default=os.getenv("MCP_TRANSPORT", "stdio"),
        help="Transport type to use (default: stdio, or MCP_TRANSPORT env var)"
    )
    
    parser.add_argument(
        "--host",
        default=os.getenv("MCP_HOST", "localhost"),
        help="Host to bind to for streamable-http transport (default: localhost, or MCP_HOST env var)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("MCP_PORT", "8000")),
        help="Port to bind to for streamable-http transport (default: 8000, or MCP_PORT env var)"
    )
    
    return parser.parse_args()


def main() -> None:
    """Main entry point for the server."""
    args = parse_args()
    
    # Create and configure the server
    server = create_server(
        transport=args.transport,
        host=args.host,
        port=args.port
    )
    
    # Run the server with the specified transport
    if args.transport == "streamable-http":
        print(f"Starting Flipkart MCP Server on {args.host}:{args.port} (streamable-http)")
        server.run(transport="streamable-http")
    else:
        print("Starting Flipkart MCP Server with stdio transport")
        server.run()  # Default to stdio transport


if __name__ == "__main__":
    main() 