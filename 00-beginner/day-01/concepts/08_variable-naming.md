# Rules for Variable naming in Python

1. **Start with a letter or underscore**: Variable names must begin with a letter (a-z, A-Z) or an underscore (_).
2. **Followed by letters, digits, or underscores**: After the first character, variable names can contain letters, digits (0-9), and underscores.
3. **Case-sensitive**: Variable names in Python are case-sensitive (`myVar` and `myvar` are different variables).
4. **No reserved words**: Variable names cannot be a Python keyword (e.g., `if`, `else`, `while`, etc.).

## Popular Conventions

1. **Snake_case**: Use underscores to separate words (e.g., `my_variable`).
2. **CamelCase**: Capitalize the first letter of each word except the first (e.g., `myVariable`).
3. **Uppercase for constants**: Use all uppercase letters with underscores for constants (e.g., `MAX_VALUE`).
4. **Descriptive names**: Choose meaningful and descriptive names that convey the purpose of the variable (e.g., `total_price` instead of `tp`).

## Examples

```python
# Valid variable names
user_name = "Alice"
userAge = 30
_user_id = 1234
MAX_LIMIT = 100

# Invalid variable names
2nd_user = "Bob"  # Starts with a digit
user-name = "Charlie"  # Contains a hyphen
class = "Physics"  # Uses a reserved word
```
