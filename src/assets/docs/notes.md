# Bug Fix Notes

## Summary

This document records all bugs fixed during the code review session on 2026-10-31.

---

## Bugs Fixed

### Bug #1: `Util.find_path()` doesn't halt execution when file is missing
- **File:** `../../utils.py`
- **Problem:** `find_path()` only logged an error and returned `None` when the file didn't exist. Execution continued, causing an unhandled `FileNotFoundError` on the subsequent `open()` call.
- **Fix:** `find_path()` now returns `False` when the file doesn't exist, and `True` when it does. In `main.py`, the return value is checked and `sys.exit(1)` is called if the file is missing.

### Bug #2: Hardcoded duplicate path instead of using the variable
- **File:** `../../main.py`
- **Problem:** `config_json` variable was assigned on line 12 but never used. Line 14 hardcoded `'src/data/config.json'` again.
- **Fix:** Changed `open('src/data/config.json', 'r')` to `open(config_json, 'r')`.

### Bug #4: Typo `"titel"` instead of `"title"`
- **Files:** `../../main.py`, `../../data/config.json`
- **Problem:** The config key was misspelled as `"titel"` in both files.
- **Fix:** Renamed `"titel"` to `"title"` in `config.json` and updated `main.py` to use `config["root"].get("title", "Keycaps")`.

### Bug #5: `logging.basicConfig()` called at class body level
- **File:** `../../utils.py`
- **Problem:** `logging.basicConfig()` was executed when the `Logger` class was first imported, locking in the logging configuration at import time and preventing later changes.
- **Fix:** Moved `logging.basicConfig()` into a new `_ensure_logger_configured()` classmethod that is called lazily — only the first time a logging method is invoked. A `_logger_configured` flag prevents reconfiguration.

### Bug #6: `Logger.test()` uses bare class name instead of `cls`
- **File:** `../../utils.py`
- **Problem:** In the `test()` method, calls like `Logger.info(...)`, `Logger.warning(...)`, etc. used the hardcoded class name. If `Logger` were subclassed, these wouldn't dispatch to the subclass.
- **Fix:** Replaced all `Logger.*` calls in `test()` with `cls.*` calls.

### Bug #9: Unused `"appearance"` config key
- **Files:** `../../main.py`, `../../data/config.json`
- **Problem:** `"appearance": "System"` was defined in config but never read or applied. CustomTkinter supports appearance modes, but `ctk.set_appearance_mode()` was never called.
- **Fix:** Added `ctk.set_appearance_mode(config["root"].get("appearance", "System"))` in the `main()` function before `app.mainloop()`.

### Bug #10: `"root"` is an array with a single object
- **File:** `../../data/config.json`
- **Problem:** The `"root"` key was an array containing a single object, requiring `config["root"][0]` access — unnecessarily complex.
- **Fix:** Changed `"root"` from an array to a plain object. Updated all references in `main.py` from `config["root"][0]["key"]` to `config["root"].get("key", default)`.

### Bug #11: Comment typo "Build-in" instead of "Built-in"
- **File:** `../../main.py`
- **Problem:** The section comment read `# --- Build-in ---`.
- **Fix:** Corrected to `# --- Built-in ---`.

### Bug #12: `KeyboardInterrupt` handling improved
- **File:** `../../main.py`
- **Problem:** `KeyboardInterrupt` (Ctrl+C) may not propagate cleanly through `mainloop()` on all platforms. The except clause might never trigger, and logging wasn't flushed on exit.
- **Fix:** Added `logging.shutdown()` before `sys.exit(0)` to flush logs. Added a general `except Exception` clause to catch unexpected errors (including potential `TclError` on Windows). Imported `sys` module for `sys.exit()`.

---

## Files Modified

| File | Changes |
|------|---------|
| `../../main.py` | Fixed hardcoded path, typo, comment, exception handling, appearance mode, config access pattern |
| `../../utils.py` | Lazy logger configuration, `cls` usage in `test()`, `find_path()` returns boolean |
| `../../data/config.json` | Simplified `root` to object, fixed `titel` → `title` |
