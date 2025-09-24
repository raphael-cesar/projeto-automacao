import json
import os
from datetime import datetime

def generate_dashboard():
    allure_results_path = "allure-results"
    if not os.path.exists(allure_results_path):
        print("Allure results directory not found. Please run tests with --alluredir=allure-results")
        return

    results = []
    for filename in os.listdir(allure_results_path):
        if filename.endswith("-result.json"):
            with open(os.path.join(allure_results_path, filename)) as f:
                results.append(json.load(f))

    html_content = """
    <html>
    <head>
        <title>Test Execution Dashboard</title>
        <style>
            body { font-family: sans-serif; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Test Execution Dashboard</h1>
        <table>
            <tr>
                <th>Test Case</th>
                <th>Status</th>
                <th>Duration (s)</th>
                <th>Start Time</th>
                <th>Stop Time</th>
            </tr>
    """

    for result in results:
        start_time = datetime.fromtimestamp(result['start'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        stop_time = datetime.fromtimestamp(result['stop'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        duration = (result['stop'] - result['start']) / 1000
        html_content += f"""
            <tr>
                <td>{result['name']}</td>
                <td>{result['status']}</td>
                <td>{duration:.2f}</td>
                <td>{start_time}</td>
                <td>{stop_time}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open("dashboard.html", "w") as f:
        f.write(html_content)

    print("Dashboard generated: dashboard.html")

if __name__ == "__main__":
    generate_dashboard()