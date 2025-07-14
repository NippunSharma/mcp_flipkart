"""
Tool implementations for the Flipkart MCP Server.
"""

import httpx
from typing import Optional, Dict, Any, Union
from urllib.parse import quote

try:
    from .config import BASE_URL, DEFAULT_TIMEOUT, ERROR_MESSAGES
except ImportError:
    from flipkart_mcp.config import BASE_URL, DEFAULT_TIMEOUT, ERROR_MESSAGES


async def search_products(
    query: str,
    sort: Optional[str] = None,
    page_number: Optional[int] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Search for products on Flipkart marketplace.
    
    Args:
        query: Search query string (e.g., "realme earbuds")
        sort: Sort order - "relevance" (default), "price_low_to_high", "price_high_to_low", "newest_first", "popularity"
        page_number: Page number for pagination (default: 1)
        min_price: Minimum price filter
        max_price: Maximum price filter
        
    Returns:
        Dict containing search results with product information
    """
    # URL encode the query
    encoded_query = quote(query)
    
    # Build the URL
    url = f"{BASE_URL}/search/{encoded_query}"
    
    # Build query parameters
    params: Dict[str, Union[str, int]] = {}
    if sort:
        params["sort"] = sort
    if page_number:
        params["page_number"] = page_number
    if min_price:
        params["min_price"] = min_price
    if max_price:
        params["max_price"] = max_price
    
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Add helpful information about how to get product details
            if "result" in data and isinstance(data["result"], list):
                for product in data["result"]:
                    if "link" in product:
                        # Extract the product link argument from the full URL
                        flipkart_url = product["link"]
                        if flipkart_url.startswith("https://flipkart.com/"):
                            product_link_arg = flipkart_url.replace("https://flipkart.com/", "")
                            product["product_link_argument"] = product_link_arg
            
            return data
            
    except httpx.TimeoutException:
        return {
            "error": ERROR_MESSAGES["timeout_error"],
            "query": query,
            "status": "failed"
        }
    except httpx.HTTPStatusError as e:
        return {
            "error": f"HTTP {e.response.status_code}: {ERROR_MESSAGES['network_error']}",
            "query": query,
            "status": "failed"
        }
    except httpx.RequestError as e:
        return {
            "error": f"{ERROR_MESSAGES['network_error']}: {str(e)}",
            "query": query,
            "status": "failed"
        }
    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)}",
            "query": query,
            "status": "failed"
        }


async def get_product_details(product_link_argument: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific product.
    
    Args:
        product_link_argument: Product link without url prefix
                              (e.g., "realme-buds-air7-52db-anc-12-4mm-driver-52hrs-playback-ip55-45ms-low-latency-bluetooth/p/itm15cefc7cf75ad")
                              This can be obtained from:
                              1. The search results' "product_link_argument" field (automatically extracted)
                              2. The "query_url" parameter from search results (remove the url prefix)
                              3. From a Flipkart product URL directly
        
    Returns:
        Dict containing detailed product information including specs, pricing, reviews, etc.
    """
    # Clean the product link argument (remove any leading/trailing slashes or spaces)
    clean_link = product_link_argument.strip().strip("/")
    
    if clean_link.startswith("0.0.0.0:3000"):
        clean_link = clean_link.replace("0.0.0.0:3000", "")

    # Validate the link format
    if not clean_link or len(clean_link) < 10:
        return {
            "error": ERROR_MESSAGES["invalid_product_link"],
            "product_link_argument": product_link_argument,
            "status": "failed"
        }
    
    # Build the URL
    url = f"{BASE_URL}/product/{clean_link}"
    
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            response = await client.get(url)
            response.raise_for_status()
            
            data = response.json()
            
            # Add some helpful computed information
            if isinstance(data, dict):
                data["flipkart_url"] = f"https://www.flipkart.com/{clean_link}"
                
                # Calculate discount percentage if not provided
                if "discount_percent" not in data and "current_price" in data and "original_price" in data:
                    try:
                        current_price = float(data["current_price"])
                        original_price = float(data["original_price"])
                        if original_price > 0 and current_price >= 0:
                            discount: float = ((original_price - current_price) / original_price) * 100
                            data["calculated_discount_percent"] = round(discount, 2)
                    except (ValueError, TypeError):
                        # Skip discount calculation if prices can't be converted to numbers
                        pass
            
            return data
            
    except httpx.TimeoutException:
        return {
            "error": ERROR_MESSAGES["timeout_error"],
            "product_link_argument": product_link_argument,
            "status": "failed"
        }
    except httpx.HTTPStatusError as e:
        return {
            "error": f"HTTP {e.response.status_code}: {ERROR_MESSAGES['network_error']}",
            "product_link_argument": product_link_argument,
            "status": "failed"
        }
    except httpx.RequestError as e:
        return {
            "error": f"{ERROR_MESSAGES['network_error']}: {str(e)}",
            "product_link_argument": product_link_argument,
            "status": "failed"
        }
    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)}",
            "product_link_argument": product_link_argument,
            "status": "failed"
        }


async def search_by_price_range(
    query: str,
    min_price: int,
    max_price: int,
    sort: str = "price_low_to_high",
    page_number: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Search for products within a specific price range.
    
    Args:
        query: Search query string
        min_price: Minimum price (required)
        max_price: Maximum price (required)
        sort: Sort order (default: "price_low_to_high")
        page_number: Page number for pagination (default: 1)
        
    Returns:
        Dict containing search results filtered by price range
    """
    return await search_products(
        query=query,
        sort=sort,
        page_number=page_number,
        min_price=min_price,
        max_price=max_price,
    ) 