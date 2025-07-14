# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml .
COPY README.md .

# Copy source code
COPY src/ ./src/

# Install Python dependencies
RUN uv pip install --system -e .

# Create a non-root user
RUN useradd --create-home --shell /bin/bash app
RUN chown -R app:app /app
USER app

# Expose port
EXPOSE 8000

# Health check removed - FastMCP doesn't have a standard health endpoint
# The service health is monitored through the MCP protocol itself

# Run the MCP server
CMD ["python", "-m", "flipkart_mcp.server"] 