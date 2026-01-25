from axe_playwright_python.sync_playwright import Axe

def run_axe(page, *, included_impacts=None):
    axe = Axe()
    axe.inject(page)
    results = axe.run(page)
    violations = results.get("violations", [])
    if included_impacts:
        violations = [v for v in violations if v.get("impact") in included_impacts]
    return violations
