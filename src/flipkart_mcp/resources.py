"""
Resource implementations for the Flipkart MCP Server.
"""

import httpx

try:
    from .config import BASE_URL, SORT_OPTIONS
except ImportError:
    from flipkart_mcp.config import BASE_URL, SORT_OPTIONS


def get_search_help() -> str:
    """Get help information for using the search functionality."""
    sort_options_text = "\n".join([f"- **{key}**: {value.replace('_', ' ').title()}" for key, value in SORT_OPTIONS.items()])
    
    return f"""
# Flipkart Search Help

## Available Sort Options:
{sort_options_text}

## Search Tips:
- Use specific product names for better results (e.g., "iPhone 15", "Samsung Galaxy S24")
- Add brand names to narrow down results (e.g., "Nike running shoes", "Adidas sneakers")
- Use price filters to find products within your budget
- Try different sort orders to find the best deals or latest products

## Examples:
- Basic search: "wireless earbuds"
- With price filter: "laptop" with min_price=30000, max_price=50000
- With sorting: "mobile phone" sorted by "price_low_to_high"

## Query Parameters:
- **query**: Search term (required)
- **sort**: Sort order (optional, default: "relevance")
- **page_number**: Page number for pagination (optional, default: 1)
- **min_price**: Minimum price filter (optional)
- **max_price**: Maximum price filter (optional)
"""


def get_product_help() -> str:
    """Get help information for retrieving product details."""
    return """
# Flipkart Product Details Help

## How to Get Product Details:
1. First search for products using the search tool
2. From the search results, use the `product_link_argument` field or extract from the `link` field
3. Use this argument with the get_product_details tool

## Product Link Format:
- Remove "https://www.flipkart.com/" from the full URL
- Example: "realme-buds-air7-52db-anc-12-4mm-driver-52hrs-playback-ip55-45ms-low-latency-bluetooth/p/itm15cefc7cf75ad"

## Product Details Include:
- Complete product specifications
- Current and original pricing
- Discount information
- Stock availability
- Customer ratings
- Product images
- Available offers and deals
- Seller information
- Warranty details

## Tips:
- Always validate the product_link_argument before using it
- The link argument should contain "/p/" followed by the product ID
- If the product is not found, check if the link argument is correct
- Use the calculated_discount_percent field for accurate discount information
"""


async def get_api_status() -> str:
    """Check the status of the Flipkart API server."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{BASE_URL}/")
            if response.status_code == 200:
                return f"✅ Flipkart API server is running at {BASE_URL}"
            else:
                return f"⚠️ Flipkart API server responded with status {response.status_code}"
    except httpx.TimeoutException:
        return f"⏱️ Flipkart API server connection timed out at {BASE_URL}"
    except httpx.ConnectError:
        return f"❌ Cannot connect to Flipkart API server at {BASE_URL}"
    except Exception as e:
        return f"❌ Flipkart API server error: {str(e)}"


def get_server_info() -> str:
    """Get information about the MCP server capabilities."""
    return """
# Flipkart MCP Server Information

## Server Capabilities:
- **Tools**: Search products, get product details, search by price range
- **Resources**: Help documentation, API status monitoring
- **Prompts**: Guided shopping workflows

## Available Tools:
1. **search_products**: Search Flipkart marketplace with advanced filtering
2. **get_product_details**: Get comprehensive product information
3. **search_by_price_range**: Convenient price-based search

## Available Resources:
1. **search-help**: Comprehensive search guide
2. **product-help**: Product details usage guide
3. **api-status**: Real-time API server status
4. **server-info**: This information page

## Available Prompts:
1. **find_best_deals**: Find the best deals in any category
2. **compare_products**: Compare two products side by side
3. **track_price_range**: Find products within a specific budget

## Configuration:
- API Base URL: {BASE_URL}
- Default Timeout: {DEFAULT_TIMEOUT}s
- Supported Sort Options: {', '.join(SORT_OPTIONS.keys())}
""" 