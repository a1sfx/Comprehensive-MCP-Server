"""Comprehensive MCP Server with multiple tools, resources, and prompts"""

import math
import random
from datetime import datetime
from typing import Dict, List
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession

# Create MCP server
mcp = FastMCP("Comprehensive Demo Server")

# ============ MATH TOOLS ============

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Calculate base raised to exponent"""
    return base ** exponent

@mcp.tool()
def square_root(n: float) -> float:
    """Calculate square root of a number"""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)

# ============ STRING TOOLS ============

@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse a string"""
    return text[::-1]

@mcp.tool()
def uppercase(text: str) -> str:
    """Convert text to uppercase"""
    return text.upper()

@mcp.tool()
def lowercase(text: str) -> str:
    """Convert text to lowercase"""
    return text.lower()

@mcp.tool()
def count_words(text: str) -> int:
    """Count words in text"""
    return len(text.split())

@mcp.tool()
def count_chars(text: str, include_spaces: bool = True) -> int:
    """Count characters in text"""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))

# ============ UTILITY TOOLS ============

@mcp.tool()
def get_timestamp() -> str:
    """Get current timestamp"""
    return datetime.now().isoformat()

@mcp.tool()
def random_number(min_val: int = 0, max_val: int = 100) -> int:
    """Generate random number between min and max"""
    return random.randint(min_val, max_val)

@mcp.tool()
def random_choice(items: List[str]) -> str:
    """Pick random item from list"""
    if not items:
        raise ValueError("List cannot be empty")
    return random.choice(items)

@mcp.tool()
async def echo_with_progress(
    message: str, 
    steps: int = 3,
    ctx: Context[ServerSession, None] = None
) -> str:
    """Echo message with progress reporting"""
    if ctx:
        await ctx.info(f"Starting echo with {steps} steps")
        
        for i in range(steps):
            progress = (i + 1) / steps
            await ctx.report_progress(
                progress=progress,
                total=1.0,
                message=f"Step {i + 1}/{steps}"
            )
        
        await ctx.debug("Echo completed")
    
    return f"Echo: {message}"

# ============ DATA TOOLS ============

@mcp.tool()
def create_dict(keys: List[str], values: List[str]) -> Dict[str, str]:
    """Create dictionary from keys and values"""
    if len(keys) != len(values):
        raise ValueError("Keys and values must have same length")
    return dict(zip(keys, values))

@mcp.tool()
def list_length(items: List) -> int:
    """Get length of list"""
    return len(items)

@mcp.tool()
def sum_list(numbers: List[float]) -> float:
    """Sum all numbers in list"""
    return sum(numbers)

@mcp.tool()
def average_list(numbers: List[float]) -> float:
    """Calculate average of numbers in list"""
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

# ============ RESOURCES ============

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get personalized greeting"""
    return f"Hello, {name}! Welcome to the MCP server!"

@mcp.resource("info://server")
def get_server_info() -> str:
    """Get server information"""
    return """MCP Demo Server v1.0
    
Features:
- Math operations (add, subtract, multiply, divide, power, sqrt, factorial)
- String operations (reverse, uppercase, lowercase, word/char count)  
- Utility tools (timestamp, random numbers, random choice)
- Data tools (dict creation, list operations)
- Progress reporting
- Multiple resources and prompts
    """

@mcp.resource("quote://{category}")
def get_quote(category: str) -> str:
    """Get quote by category"""
    quotes = {
        "motivation": "The only way to do great work is to love what you do. - Steve Jobs",
        "wisdom": "The only true wisdom is in knowing you know nothing. - Socrates",
        "success": "Success is not final, failure is not fatal. - Winston Churchill",
        "life": "Life is what happens when you're busy making other plans. - John Lennon"
    }
    return quotes.get(category.lower(), "No quote found for this category")

# ============ PROMPTS ============

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
        "enthusiastic": "Please write an enthusiastic, energetic greeting"
    }
    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

@mcp.prompt()
def code_review(language: str, code: str) -> str:
    """Generate code review prompt"""
    return f"""Please review this {language} code:

```{language}
{code}
```

Provide:
1. Code quality assessment
2. Potential bugs or issues
3. Performance considerations  
4. Best practices recommendations
5. Refactoring suggestions
"""

@mcp.prompt()
def explain_concept(topic: str, level: str = "beginner") -> str:
    """Generate explanation prompt"""
    levels = {
        "beginner": "like I'm 5 years old",
        "intermediate": "with some technical detail",
        "advanced": "with deep technical insights"
    }
    return f"Explain {topic} {levels.get(level, levels['beginner'])}."

@mcp.prompt()
def debug_assistant(error: str, context: str = "") -> str:
    """Generate debugging prompt"""
    prompt = f"I'm seeing this error: {error}"
    if context:
        prompt += f"\n\nContext: {context}"
    prompt += "\n\nPlease help me debug this issue."
    return prompt

# Run server with STDIO transport (for Claude Desktop)
if __name__ == "__main__":
    mcp.run()
