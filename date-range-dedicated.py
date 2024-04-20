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

def generate_csv(cluster_name, start_date, end_date):
    # Write CSV header
    with open('cluster_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["month", "date", "AIT", "nodes", "cpu total", "cluster-name", "lane", "source tag"])

    # Convert start and end date strings to datetime objects
    start_datetime = datetime.datetime.strptime(start_date, "%m-%d-%Y")
    end_datetime = datetime.datetime.strptime(end_date, "%m-%d-%Y")

    # Iterate through dates and generate rows for each day
    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        # Fetch current month and date
        month = current_datetime.strftime("%B")
        date = current_datetime.strftime("%m-%d-%Y")

        # Fetch values from cluster and Prometheus
        AIT = fetch_cluster_label("default", "AIT")
        lane = fetch_cluster_label("default", "lane")
        nodes = fetch_prometheus_data('sum(kube_node_info)')
        cpu_total = fetch_prometheus_data('sum(rate(node_cpu_seconds_total{mode="idle"}[5m]))')

        # Prepare CSV data for current day
        row = [month, date, AIT, nodes, cpu_total, cluster_name, lane, "BCC2"]

        # Append row to CSV
        with open('cluster_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

        # Move to the next day
        current_datetime += datetime.timedelta(days=1)

if __name__ == "__main__":
    cluster_name = input("Enter the cluster name: ")
    start_date = input("Enter the start date (MM-DD-YYYY): ")
    end_date = input("Enter the end date (MM-DD-YYYY): ")
    generate_csv(cluster_name, start_date, end_date)