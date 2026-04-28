import os
import requests

E2EM_URL = os.getenv("E2EM_BACKEND_URL", "http://mock-e2em:8080")

def validate_apps(apps):
    results = []

    for app in apps:
        try:
            r = requests.get(f"{E2EM_URL}/traces/{app['name']}", timeout=2)
            has_trace = r.status_code == 200
        except:
            has_trace = False

        results.append({
            "name": app["name"],
            "instrumented": app["instrumented"],
            "trace_found": has_trace
        })

    return results