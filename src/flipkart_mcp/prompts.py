"""
Prompt implementations for the Flipkart MCP Server.
"""


def get_search_results(query: str) -> str:
    """Get search results for a specific query."""
    return f"""Please search for "{query}" on Flipkart and provide me with the search results.

Use the search_products tool with:
- query: "{query}"
- You can optionally specify sort, page_number, min_price, or max_price if needed

The search results will include:
- Product names and descriptions
- Prices (current and original)
- Ratings and reviews
- Product links
- Available offers
- query_url parameter (which can be used to get detailed product information)

Please present the results in a clear, organized format showing the key information for each product."""


def get_product_info(product_link_or_query_url: str) -> str:
    """Get detailed information about a specific product using its link or query_url."""
    return f"""Please get detailed information about the product using this link: "{product_link_or_query_url}"

Instructions:
1. If the link starts with "0.0.0.0:3000" or any other base url, remove this prefix to get the product_link_argument
2. Use the get_product_details tool with the cleaned product_link_argument
3. The query_url parameter from search results can be used directly after removing the base url prefix

The detailed product information will include:
- Complete product specifications
- Detailed pricing information (current price, original price, discounts)
- Customer ratings and reviews
- Available offers and deals
- Product images and descriptions
- Seller information
- Shipping and return policies
- Stock availability

Present the information in a comprehensive format covering all the important details a customer would need to make a purchasing decision."""


def find_best_deals(category: str) -> str:
    """Find the best deals in a product category."""
    return f"""I want to find the best deals for {category}. Please:

1. Search for products in the "{category}" category
2. Sort results by price (low to high) to find budget options
3. Also search with popularity sort to find highly-rated products
4. For promising products, get detailed information to check:
   - Discount percentages
   - Original vs current prices
   - Customer ratings
   - Available offers

Focus on products with high ratings (4+ stars) and good discounts (>20%). Present the findings in a clear comparison format.

## Search Strategy:
- Use search_products with query="{category}" and sort="price_low_to_high"
- Also try search_products with query="{category}" and sort="popularity"
- For top results, use get_product_details to get comprehensive information
- Compare discount percentages and customer ratings

## Evaluation Criteria:
- Rating: 4.0+ stars preferred
- Discount: >20% preferred
- Price: Consider value for money
- Seller: Higher seller rating preferred
- Stock: In-stock products only

Present results in a table format with key metrics for easy comparison."""


def compare_products(product1: str, product2: str) -> str:
    """Compare two products to help make a purchasing decision."""
    return f"""Please help me compare "{product1}" and "{product2}". 

For each product:
1. Search to find the best-rated versions
2. Get detailed product information
3. Compare key aspects:
   - Price and available discounts
   - Technical specifications
   - Customer ratings and reviews
   - Seller reputation
   - Warranty terms
   - Available offers

Present a side-by-side comparison highlighting the pros and cons of each product to help make an informed decision.

## Comparison Steps:
1. Search for "{product1}" using search_products
2. Search for "{product2}" using search_products  
3. Select the best-rated version of each product
4. Get detailed information using get_product_details for both
5. Create a detailed comparison table

## Comparison Areas:
- **Price**: Current price, original price, discount percentage
- **Specifications**: Key technical specs and features
- **Ratings**: Overall rating, number of reviews
- **Seller**: Seller name, seller rating, F-Assured status
- **Offers**: Available bank offers, special deals
- **Warranty**: Warranty terms and service type
- **Stock**: Availability status

## Decision Framework:
- Which offers better value for money?
- Which has better customer satisfaction?
- Which has better after-sales support?
- Which is more suitable for the intended use case?

Provide a clear recommendation with reasoning."""


def track_price_range(product_name: str, budget: int) -> str:
    """Find products within a specific budget range."""
    return f"""I'm looking for "{product_name}" within a budget of ₹{budget}. Please:

1. Search for the product with max_price set to {budget}
2. Sort results by price (low to high) to maximize value
3. For products within budget, get detailed information
4. Identify the best value options considering:
   - Features vs price ratio
   - Brand reputation
   - Customer ratings
   - Warranty coverage
   - Current offers and discounts

Recommend the top 3 options that provide the best value within the budget.

## Search Strategy:
- Use search_by_price_range with query="{product_name}", min_price=0, max_price={budget}
- Sort by "price_low_to_high" to find the best deals first
- Get detailed information for the top 5-7 results
- Analyze value proposition for each

## Evaluation Criteria:
- **Price**: Must be ≤ ₹{budget}
- **Value**: Features offered relative to price
- **Quality**: Brand reputation and build quality
- **Ratings**: Customer satisfaction (prefer 4+ stars)
- **Warranty**: Coverage and service quality
- **Offers**: Additional savings available

## Output Format:
### Budget Analysis: ₹{budget}
1. **Option 1**: [Product Name]
   - Price: ₹[amount] (savings: ₹[amount])
   - Key Features: [list main features]
   - Rating: [rating]/5 ([number] reviews)
   - Why it's good value: [explanation]

2. **Option 2**: [Product Name]
   - [Similar format]

3. **Option 3**: [Product Name]
   - [Similar format]

### Recommendation:
Based on the analysis, recommend the best option with clear reasoning."""


def seasonal_deals(season: str, category: str) -> str:
    """Find seasonal deals and offers in a specific category."""
    return f"""Help me find the best {season} deals for {category}. Please:

1. Search for products in the "{category}" category
2. Look for seasonal discounts and special offers
3. Compare current prices with historical pricing trends
4. Identify limited-time offers and flash sales
5. Check for seasonal-specific product variants

Focus on products with significant seasonal discounts and time-limited offers.

## Search Strategy:
- Search for "{category}" with different sort options
- Look for products with high discount percentages
- Check for seasonal keywords in product descriptions
- Identify F-Assured products for guaranteed quality

## Deal Analysis:
- **Discount Depth**: Look for >30% seasonal discounts
- **Offer Types**: Bank offers, exchange offers, EMI options
- **Seasonal Variants**: Special {season} editions or colors
- **Bundle Deals**: Combo offers and package deals
- **Flash Sales**: Time-limited promotional pricing

## Timing Considerations:
- Current {season} season relevance
- Upcoming festivals and shopping events
- End-of-season clearance opportunities
- New product launch timings

Present the best seasonal deals with urgency indicators and deal expiration information."""


def gift_recommendations(occasion: str, budget: int, recipient: str) -> str:
    """Find gift recommendations for specific occasions and recipients."""
    return f"""I need gift recommendations for {occasion} with a budget of ₹{budget} for {recipient}. Please:

1. Search for appropriate gift categories based on the occasion and recipient
2. Filter products within the specified budget
3. Focus on highly-rated products with good reviews
4. Consider gift-appropriate features (packaging, warranty, etc.)
5. Look for products with good return/exchange policies

Provide personalized recommendations based on the occasion and recipient profile.

## Gift Selection Criteria:
- **Budget**: ₹{budget} (allow 10% flexibility)
- **Occasion**: {occasion} appropriateness
- **Recipient**: {recipient} preferences and needs
- **Quality**: High ratings and positive reviews
- **Presentation**: Gift-worthy packaging and appearance
- **Reliability**: Trusted brands and sellers

## Search Strategy:
- Identify relevant product categories for {recipient}
- Use price filtering to stay within budget
- Sort by ratings and popularity
- Check for gift-specific features (gift wrapping, etc.)

## Recommendation Format:
### Gift Options for {recipient} - {occasion}
1. **[Product Name]** - ₹[price]
   - Why it's perfect: [relevance to occasion/recipient]
   - Key features: [main selling points]
   - Rating: [rating]/5
   - Gift appeal: [packaging, brand value, etc.]

2. **[Product Name]** - ₹[price]
   - [Similar format]

3. **[Product Name]** - ₹[price]
   - [Similar format]

### Final Recommendation:
Choose the most suitable option with reasoning based on the specific occasion and recipient.""" 