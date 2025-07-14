"""
Configuration constants for the Flipkart MCP Server.
"""
import os

# API Configuration
BASE_URL = os.getenv("FLIPKART_API_BASE_URL", "http://localhost:3000")

# Server Configuration
SERVER_NAME = "Flipkart API Server"
SERVER_VERSION = "0.1.0"

# HTTP Configuration
DEFAULT_TIMEOUT = 30.0
MAX_RETRIES = 3

# Search Configuration
SORT_OPTIONS = {
    "relevance": "relevance",
    "price_low_to_high": "price_low_to_high", 
    "price_high_to_low": "price_high_to_low",
    "newest_first": "newest_first",
    "popularity": "popularity",
}

# Resource URIs
RESOURCE_URIS = {
    "search_help": "flipkart://api/search-help",
    "product_help": "flipkart://api/product-help",
    "api_status": "flipkart://api/status",
}

# Error Messages
ERROR_MESSAGES = {
    "api_server_down": "Flipkart API server is not accessible",
    "invalid_product_link": "Invalid product link argument provided",
    "network_error": "Network error occurred while connecting to API",
    "timeout_error": "Request timed out while connecting to API",
    "json_error": "Invalid JSON response from API",
} 