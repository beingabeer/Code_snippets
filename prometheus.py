import csv
import datetime
import requests

def fetch_prometheus_data(query):
    # Assuming you have a Prometheus endpoint URL
    prometheus_url = "http://your-prometheus-url/api/v1/query"
    params = {'query': query}
    response = requests.get(prometheus_url, params=params)
    data = response.json()
    value = data['data']['result'][0]['value'][1]
    return value

def fetch_cluster_label(namespace, label):
    # Assuming you have Kubernetes API access
    # You can use libraries like kubernetes-client for this
    # Here's a mock implementation
    return "mocked_label_value"

def generate_csv(cluster_name):
    # Fetch current month and date
    now = datetime.datetime.now()
    month = now.strftime("%B")
    date = now.strftime("%d")

    # Fetch values from cluster and Prometheus
    AIT = fetch_cluster_label("default", "AIT")
    lane = fetch_cluster_label("default", "lane")
    nodes = fetch_prometheus_data('sum(kube_node_info)')
    cpu_total = fetch_prometheus_data('sum(rate(node_cpu_seconds_total{mode="idle"}[5m]))')

    # Prepare CSV data
    rows = [
        [month, date, AIT, nodes, cpu_total, cluster_name, lane, "BCC2"]
    ]

    # Write CSV
    with open('cluster_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["month", "date", "AIT", "nodes", "cpu total", "cluster-name", "lane", "source tag"])
        writer.writerows(rows)

if __name__ == "__main__":
    cluster_name = input("Enter the cluster name: ")
    generate_csv(cluster_name)
