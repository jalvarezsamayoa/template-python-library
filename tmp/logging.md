# Research Report: Logging Patterns in Best-in-Class Python Libraries

This report examines how 10 of the most popular and well-maintained Python libraries manage logging, their configuration strategies, and how they expose these capabilities to clients.

## 1. Libraries Analyzed

| Library                | Primary Logging Mechanism  | Exposure Pattern                                        |
| :--------------------- | :------------------------- | :------------------------------------------------------ |
| **requests / urllib3** | Standard `logging`         | Hierarchical loggers (e.g., `urllib3.connectionpool`)   |
| **boto3 (AWS SDK)**    | Standard `logging`         | Functional helper (`set_stream_logger`)                 |
| **httpx**              | Standard `logging`         | Namespace-based (`httpx`, `httpcore`)                   |
| **Django / Flask**     | Standard `logging`         | Framework-integrated `dictConfig`                       |
| **SQLAlchemy**         | Standard `logging`         | `echo` parameter (shortcut) + standard loggers          |
| **Click (CLI)**        | `logging` + `click.echo()` | CLI flags for verbosity (`--verbose`)                   |
| **Pydantic**           | Standard `logging`         | Validation errors logged via standard mechanisms        |
| **scikit-learn**       | Custom `verbose` (int)     | Direct `print` (via `joblib`) + custom `verbose` params |
| **pandas**             | `warnings` + `logging`     | Mostly `warnings` for user alerts                       |
| **cryptography**       | Standard `logging`         | Strict `NullHandler` usage, no sensitive data logging   |

---

## 2. Extracted Patterns & Best Practices

### A. The "Hierarchy" Pattern

Nearly all libraries use the standard `logging` module and follow the package hierarchy.

- **Pattern:** `logger = logging.getLogger(__name__)`
- **Why:** This allows users to configure logging at various levels of granularity (e.g., all of `httpx`, or just `httpx.dispatch`).

### B. The "NullHandler" Strategy

Well-behaved libraries ensure they don't produce unexpected output if the user hasn't configured logging.

- **Pattern:** `logging.getLogger("mylib").addHandler(logging.NullHandler())`
- **Why:** Prevents "No handlers could be found for logger" errors in older Python versions and ensures silence by default.

### C. No Side-Effect Configuration

Best-in-class libraries **never** call `logging.basicConfig()` or add handlers (except `NullHandler`) internally.

- **Rule:** Logging configuration is the _responsibility of the application_, not the library.
- **Exception:** Some libraries provide optional "opt-in" helpers (like `boto3.set_stream_logger()`) to quickly enable logging for debugging.

### D. Distinction: Diagnostics vs. Output

Libraries with CLI components (like `Click`) distinguish between two types of messages:

- **Output:** Information the user requested (use `click.echo()` or `print()`).
- **Diagnostics:** Information about what the library is doing (use `logging.debug()` / `logging.info()`).

### E. Shortcuts for Developers

Some libraries provide simplified entry points for common logging tasks.

- **SQLAlchemy:** `create_engine(..., echo=True)` is a shortcut that internally configures a handler for the `sqlalchemy.engine` logger.
- **Boto3:** `boto3.set_stream_logger('boto3.resources', logging.INFO)` simplifies the `getLogger` -> `addHandler` -> `setLevel` boilerplate.

---

## 3. How Libraries Expose Logging to Clients

1.  **Direct Namespace Access:** The most common way. Clients simply use `logging.getLogger('library_name')` to set levels or add handlers.
2.  **Environment Variables:** Some libraries (like `scikit-learn` extensions or `Pydantic Logfire`) allow configuration via environment variables (e.g., `LOG_LEVEL=DEBUG`).
3.  **Library Configuration Objects:** Libraries may have a `settings` or `config` object that can toggle logging-related features (e.g., Pydantic's `SecretStr` for security).
4.  **CLI Arguments:** In CLI tools, patterns like `-v`, `-vv`, or `--log-level` are standard for mapping user intent to internal logging levels.

## 4. Recommendations for Your Library

1.  **Use `logging`**: Stick to the standard library to minimize dependencies.
2.  **Namespace**: Use `logging.getLogger(__name__)` in every module.
3.  **Default to Silence**: Add a `NullHandler` to your top-level logger.
4.  **Don't Configure**: Never call `basicConfig` or add handlers in your library code.
5.  **Expose Helpers**: If your library is complex, provide a `setup_logging()` helper function that users can optionally call.
6.  **Security**: Use types like `SecretStr` or sensitive data masking logic to ensure keys/passwords never hit the logs.
