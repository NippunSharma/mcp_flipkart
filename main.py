#!/usr/bin/env python3
"""
Main entry point for the Flipkart MCP Server.

This script provides a convenient way to run the server directly.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from flipkart_mcp.server import main

if __name__ == "__main__":
    main() 