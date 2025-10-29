# RW Math

A simple Python mathematical operations module for demonstration and learning purposes.

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](htmlcov/index.html)

## Features

- Basic mathematical operations: addition, subtraction, multiplication, division
- Fully tested with pytest
- 100% code coverage
- Type hints for better IDE support
- Clean, simple API

## Installation

### From PyPI (when published)

```bash
pip install rw_math
```

Or with uv:

```bash
uv add rw_math
```

**Important: Package vs. Module Naming**

Understanding the difference between package name and module name is crucial:

1. **Package Name** (what you install): `rw_math`
   - This is the name in `pyproject.toml`
   - When you run `uv add rw_math`, uv normalizes it to `rw-math` in your dependencies
   - This normalization is automatic and follows [PEP 503](https://peps.python.org/pep-0503/)

2. **Module Name** (what you import): `rwmath`
   - This is the **folder name** inside `src/`
   - This is what you use in your code: `from rwmath import add`
   - Module names cannot have hyphens or underscores when importing

**Example:**
```toml
# After running: uv add rw_math
# Your pyproject.toml will show:
[project]
dependencies = [
    "rw-math",  # ← Note: normalized to hyphen
]
```

```python
# But in your code, you import using the module name (folder name):
from rwmath import add, sub, mul, div  # ← Uses folder name, no hyphens/underscores
```

**Summary:**
- Install with: `rw_math` → becomes `rw-math` in dependencies (automatic)
- Import with: `rwmath` → the actual module/folder name

### For Development

```bash
# Clone the repository
git clone <repository-url>
cd python_module

# Tests work directly without installation due to pythonpath configuration
pytest
```

## Usage

### As a Library

```python
from rwmath import add, sub, mul, div

# Addition
result = add(3, 4)  # 7

# Subtraction
result = sub(10, 4)  # 6

# Multiplication
result = mul(5, 6)  # 30

# Division
result = div(10, 2)  # 5.0
```

### Command Line

```bash
rw_math
# Output: Hello from python-module!
#         add 7
```

## API Reference

Simple mathematical operations: `add()`, `sub()`, `mul()`, `div()`

See source code in [src/rwmath/math.py](src/rwmath/math.py) for implementation details.

## Building and Publishing

### How to Build

```bash
uv build --no-sources
```

This creates distribution packages in the `dist/` directory.

### How to Publish

**Publish to PyPI:**
```bash
uv publish --token <your_token_from_pypi>
```

**Publish to Test PyPI:**
```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token <your_token>
```

### Getting API Tokens

- **PyPI**: https://pypi.org/manage/account/token/
- **Test PyPI**: https://test.pypi.org/manage/account/token/

### Testing Installation from Test PyPI

After publishing to Test PyPI, test the installation in another project:

```bash
# Install from Test PyPI with fallback to PyPI
uv add \
  --index https://test.pypi.org/simple/ \
  --index-strategy unsafe-best-match \
  rw_math==0.1.1
```

**Options explained:**
- `--index`: Use Test PyPI as the package index (persists in pyproject.toml)
- `--index-strategy unsafe-best-match`: Allow fallback to PyPI for dependencies
- `rw_math==0.1.1`: Specify version to avoid getting older versions

**Note**: Your package has no runtime dependencies, but the `--index-strategy` flag ensures proper resolution when Test PyPI and PyPI are both used.

## Development

### Project Structure

```
python_module/
├── src/
│   ├── main.py              # Entry point
│   └── rwmath/
│       ├── __init__.py      # Package exports
│       └── math.py          # Core functions
├── tests/
│   ├── __init__.py
│   └── test_math.py         # Unit tests
├── pyproject.toml           # Project configuration
├── .gitignore
└── README.md
```

### Setup Development Environment

1. **Clone the repository**:
```bash
git clone <repository-url>
cd python_module
```

2. **Install development dependencies**:
```bash
# Install the package with dev dependencies
uv sync --extra dev
```

Or manually:
```bash
uv add --dev pytest pytest-cov
```

The project uses `pythonpath = ["src"]` in `pyproject.toml`, which allows pytest to import modules directly without installing the package.

### Running Tests

All test settings are configured in `pyproject.toml`, so you just need to run:

**Basic test run** (includes coverage automatically):
```bash
pytest
```

This automatically:
- Finds tests in `tests/` directory
- Measures code coverage for `src/rwmath/`
- Shows missing lines in terminal
- Generates HTML report in `htmlcov/`
- Fails if coverage drops below 80%

**Additional test commands:**

```bash
# Verbose output
pytest -v

# Run specific test
pytest tests/test_math.py::TestAdd::test_add_positive_numbers

# View HTML coverage report
open htmlcov/index.html  # macOS
```

### Test Coverage

Current coverage: **100%**

All coverage settings are centralized in `pyproject.toml`:
- **Minimum required**: 80% (configurable)
- **HTML reports**: Generated in `htmlcov/`
- **Terminal output**: Shows missing lines
- **Excludes**: Test files and `__init__.py` files
- **Precision**: 2 decimal places

### Code Quality Standards

- **Type Hints**: All functions use type annotations
- **Testing**: 100% code coverage with pytest
- **Documentation**: Docstrings for all public functions
- **Edge Cases**: Comprehensive testing including error conditions

## Configuration Files

### pyproject.toml

All project and test configuration is centralized in `pyproject.toml`:

**Project Metadata:**
```toml
[project]
name = "rw_math"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["pytest>=8.4.2", "pytest-cov>=7.0.0"]
```

**Pytest Configuration:**
```toml
[tool.pytest.ini_options]
pythonpath = ["src"]           # Import from src/ without installation
testpaths = ["tests"]          # Test discovery location
addopts = [
    "--cov=src/rwmath",        # Coverage target
    "--cov-report=term-missing", # Terminal report
    "--cov-report=html",       # HTML report
    "--cov-fail-under=80",     # Minimum 80% coverage
]
```

**Coverage Settings:**
```toml
[tool.coverage.run]
source = ["src"]               # Source code location
omit = ["*/tests/*", "*/__init__.py"]  # Exclude from coverage

[tool.coverage.report]
precision = 2                  # Decimal places
show_missing = true            # Show uncovered lines
fail_under = 80                # Minimum threshold

[tool.coverage.html]
directory = "htmlcov"          # HTML report location
```

**Key Benefits:**
- ✅ No separate `pytest.ini` or `.coveragerc` files needed
- ✅ All settings version-controlled in one place
- ✅ Consistent configuration across all environments
- ✅ `pythonpath = ["src"]` enables imports without package installation

## Requirements

- Python 3.12 or higher
- pytest >= 8.4.2
- pytest-cov >= 7.0.0

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Ensure coverage is maintained (`pytest --cov`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Write docstrings for public APIs
- Keep functions simple and focused (Single Responsibility Principle)
- Write tests for all new functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Ronson W.

## Changelog

### [0.1.0] - 2024-10-28

#### Added
- Initial release
- Basic mathematical operations (add, sub, mul, div)
- Complete test suite with 100% coverage
- Type hints for all functions
- Command-line interface
- Comprehensive documentation

## Roadmap

Future enhancements under consideration:
- [ ] Additional mathematical operations (power, modulo, etc.)
- [ ] Support for floating-point inputs
- [ ] More robust error handling
- [ ] Performance optimizations
- [ ] CLI with argument parsing

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

## Acknowledgments

- Built with [uv](https://github.com/astral-sh/uv) for fast Python package management
- Tested with [pytest](https://pytest.org/)
- Coverage reports by [pytest-cov](https://pytest-cov.readthedocs.io/)
