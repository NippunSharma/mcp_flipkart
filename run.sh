#!/bin/bash

set -e

echo "🚀 Starting Flipkart MCP Server Services"
echo "========================================"

# Start services (without rebuilding)
echo "▶️ Starting services..."
docker-compose up -d

echo "⏳ Services starting up..."
echo ""
echo "🌐 Services will be available at:"
echo "   - Flipkart Scraper API: http://localhost:3000"
echo "   - MCP Server: http://localhost:8000"
echo ""
echo "📋 To view logs:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 To stop services:"
echo "   docker-compose down" 