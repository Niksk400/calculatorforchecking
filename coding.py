# Function to generate URL for a calculator
def generate_calculator_url(base_url, num1, num2, operation):
    """
    base_url: URL of the calculator service
    num1: First number
    num2: Second number
    operation: 'add', 'subtract', 'multiply', 'divide'
    """
    url = f"{base_url}?num1={num1}&num2={num2}&operation={operation}"
    return url

# Example usage:
base_url = "https://mycalculator.com/calculate"  # Example calculator URL
num1 = 25
num2 = 5
operation = "add"  # or 'subtract', 'multiply', 'divide'

# Generate the URL
url = generate_calculator_url(base_url, num1, num2, operation)
print("Generated Calculator URL:")
print(url)
