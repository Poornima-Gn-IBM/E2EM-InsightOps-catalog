from kubernetes import client, config

def scan_apps():
    try:
        config.load_incluster_config()
    except:
        config.load_kube_config()

    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces()

    apps = []
    for pod in pods.items:
        labels = pod.metadata.labels or {}
        apps.append({
            "name": pod.metadata.name,
            "instrumented": "e2em" in labels
        })

    return apps