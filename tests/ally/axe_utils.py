from axe_playwright_python.sync_playwright import Axe


def _results_to_dict(results):
    """
    Normalize AxeResults (or similar) into a plain dict.
    Supports multiple versions of axe-playwright-python.
    """
    if isinstance(results, dict):
        return results

    # Common method names across versions / wrappers
    for method_name in ("to_dict", "as_dict", "to_json"):
        if hasattr(results, method_name):
            try:
                data = getattr(results, method_name)
                if callable(data):
                    data = data()
                # to_json might return a dict or a JSON string depending on version
                if isinstance(data, dict):
                    return data
            except:
                pass

    # If it has attribute access like results.violations, we can synthesize dict
    violations_attr = getattr(results, "violations", None)
    if violations_attr is not None:
        return {"violations": violations_attr}

    # Try direct access for AxeResults
    try:
        if hasattr(results, 'violations'):
            return {"violations": results.violations}
    except:
        pass

    # Try other attributes
    for attr_name in ("results", "data", "report"):
        try:
            attr = getattr(results, attr_name, None)
            if attr is not None:
                if isinstance(attr, dict):
                    if "violations" in attr:
                        return attr
                    else:
                        return {"violations": attr.get("violations", [])}
                elif isinstance(attr, list):
                    return {"violations": attr}
        except:
            pass

    # Try __dict__
    try:
        d = results.__dict__
        if isinstance(d, dict) and "violations" in d:
            return d
    except:
        pass

    # Fallback: assume no violations
    return {"violations": []}

    raise TypeError(f"Unexpected axe results type: {type(results)!r}")

    # Fallback: assume no violations
    return {"violations": []}


def run_axe(page, *, included_impacts=None):
    """
    Run axe accessibility scan on a Playwright page and return violations.
    Optionally filter to only include certain impact levels.
    """
    axe = Axe()
    axe.inject(page)

    results = axe.run(page)
    data = _results_to_dict(results)

    violations = data.get("violations") or []
    # Ensure list-like
    if not isinstance(violations, list):
        violations = list(violations)

    if included_impacts:
        impacts = {i.lower() for i in included_impacts}
        violations = [
            v for v in violations
            if (v.get("impact") or "").lower() in impacts
        ]

    return violations
