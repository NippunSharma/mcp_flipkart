
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("flipkart-mcp-server")
except PackageNotFoundError:
    # package is not installed
    pass