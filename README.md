# Flipkart MCP Server

A **Model Context Protocol (MCP) server** that provides seamless access to Flipkart's e-commerce platform through a standardized, AI-friendly interface.
Demo Video: [Click Here]([url](https://youtu.be/SgwkgKiALtA)) 

## 🚀 Quick Start

### 🐳 Docker (Recommended)

```bash
# Build and start all services (scraper API + MCP server)
./build.sh

# Or use Docker Compose directly
docker-compose up --build -d
```

See [DOCKER_README.md](DOCKER_README.md) for detailed Docker setup instructions.

### 📦 Manual Installation

```bash
# Install dependencies
uv add mcp[cli] httpx

# Run with stdio transport (default, recommended for Claude Desktop)
uv run src/flipkart_mcp/server.py

# Run with HTTP transport (for testing/debugging)
uv run src/flipkart_mcp/server.py --transport streamable-http --port 8000

# Install in Claude Desktop
uv run mcp install src/flipkart_mcp/server.py --name "Flipkart Shopping Assistant"
```

## 🎯 Features

### 🔧 Tools (Model-Controlled)
- **Search Products**: Advanced marketplace search with filters and sorting
- **Get Product Details**: Comprehensive product information including specs and pricing
- **Search by Price Range**: Budget-focused product discovery

### 📚 Resources (Application-Controlled)
- **Help Documentation**: Comprehensive guides for search and product features
- **API Status**: Real-time monitoring of backend service health
- **Server Info**: Complete server capabilities and configuration

### 🎭 Prompts (User-Controlled)
- **Get Search Results**: General search with clear result presentation
- **Get Product Information**: Detailed product analysis using query_url from search results
- **Find Best Deals**: Guided workflow for discovering optimal product deals
- **Compare Products**: Side-by-side product comparison analysis
- **Track Price Range**: Budget-conscious shopping assistance
- **Seasonal Deals**: Time-sensitive offer discovery
- **Gift Recommendations**: Occasion-based product suggestions

## 📁 Project Structure

```
mcp_flipkart/
├── src/flipkart_mcp/        # Main package
│   ├── __init__.py          # Package initialization
│   ├── server.py            # MCP server setup and configuration
│   ├── tools.py             # Tool implementations
│   ├── resources.py         # Resource implementations
│   ├── prompts.py           # Prompt implementations
│   └── config.py            # Configuration constants
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.10+**
- **uv** (recommended) or pip
- **Flipkart API Server** running on `localhost:3000`

### Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd mcp_flipkart

# Install dependencies
uv add mcp[cli] httpx

# Run examples
python examples/usage_examples.py
```

## 🔗 Integration

### Claude Desktop
```bash
uv run mcp install src/flipkart_mcp/server.py --name "Flipkart Shopping Assistant"
```

### Direct Usage
```bash
python src/flipkart_mcp/server.py

or

uv run src/flipkart_mcp/server.py
```

## 📈 API Overview

### Core Endpoints
- `/search/{query}` - Product search with advanced filtering
- `/product/{product_link}` - Detailed product information

### MCP Primitives
- **3 Tools** for product search and details
- **4 Resources** for help and status information  
- **7 Prompts** for guided shopping workflows

## 🔗 Related

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Desktop](https://claude.ai/download)
