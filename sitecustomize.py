"""
Pytest/Playwright a11y tests expect Axe().inject(page) to exist.

Some versions of axe-playwright-python only require Axe().run(page) and do not
expose inject(). This shim adds a no-op inject() method so the test suite works.
"""

def _patch_axe():
    try:
        # Common import path used with axe-playwright-python
        from axe_playwright_python.sync_playwright import Axe  # type: ignore
    except Exception:
        return

    if not hasattr(Axe, "inject"):
        # run(page) already injects internally in those versions; inject can be a no-op.
        def inject(self, page):  # noqa: ANN001
            return None

        setattr(Axe, "inject", inject)

_patch_axe()
