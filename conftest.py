def pytest_configure():
    """
    Tests expect Axe().inject(page). Some axe/playwright wrappers do not expose inject().
    This shim adds an inject() method to whatever Axe class is installed.
    """
    possible_imports = [
        # Common variants seen across axe-playwright python wrappers
        ("axe_playwright_python.sync_playwright", "Axe"),
        ("axe_playwright_python.sync_api", "Axe"),
        ("axe_playwright_python", "Axe"),
        ("playwright_axe", "Axe"),
    ]

    Axe = None
    for module_name, class_name in possible_imports:
        try:
            mod = __import__(module_name, fromlist=[class_name])
            Axe = getattr(mod, class_name, None)
            if Axe is not None:
                break
        except Exception:
            continue

    if Axe is None:
        # If Axe isn't importable, let the tests fail with the original error.
        return

    if not hasattr(Axe, "inject"):
        def inject(self, page):  # noqa: ANN001
            # In many versions, run() handles injection internally.
            return None

        setattr(Axe, "inject", inject)
