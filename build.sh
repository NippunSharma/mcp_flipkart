#!/bin/bash

set -e

echo "🚀 Building Flipkart MCP Server with Docker Compose"
echo "=================================================="

# Build and start all services
echo "📦 Building and starting services..."
docker-compose up --build -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be ready..."
docker-compose logs -f flipkart-scraper-api &
docker-compose logs -f mcp-server &

# Wait for scraper API to be healthy
echo "🔍 Waiting for Flipkart Scraper API to be healthy..."
timeout 120 bash -c 'until docker-compose ps flipkart-scraper-api | grep -q "healthy"; do sleep 2; done' || {
    echo "❌ Flipkart Scraper API failed to start"
    docker-compose logs flipkart-scraper-api
    exit 1
}

# Wait for MCP server to be healthy  
echo "🔍 Waiting for MCP Server to be ready..."
timeout 60 bash -c 'until curl -s http://localhost:8000/health > /dev/null 2>&1; do sleep 2; done' || {
    echo "❌ MCP Server failed to start"
    docker-compose logs mcp-server
    exit 1
}

echo "✅ All services are ready!"
echo ""
echo "🌐 Services available at:"
echo "   - Flipkart Scraper API: http://localhost:3000"
echo "   - MCP Server: http://localhost:8000"
echo ""
echo "📋 To view logs:"
echo "   docker-compose logs -f flipkart-scraper-api"
echo "   docker-compose logs -f mcp-server"
echo ""
echo "🛑 To stop services:"
echo "   docker-compose down" 