# Monitoring Stack: Prometheus + Grafana + Loki + Promtail

A complete observability stack for metrics and logs using Docker Compose — now with **log streaming from a Flask app to Loki** using **Promtail**.

##  What's Included

- **Prometheus** — Metrics collection
- **Grafana** — Dashboards and visualization
- **Loki** — Log aggregation
- **Promtail** — Log shipping from Docker container to Loki
- **Flask App** — Demo Python app with logging

##  Project Structure

monitoring-stack/
├── app/ # Flask app with logging
│ ├── app.py
│ └── requirements.txt
├── docker-compose.yml # Defines all services
├── Dockerfile # Builds the Flask app container
├── prometheus/
│ └── prometheus.yml
├── loki/
│ └── config.yaml
├── promtail/
│ └── config.yaml
└── README.md

---

##  Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

###  Run the Stack

docker-compose up --build
 Access Services
Prometheus: http://localhost:9090

Grafana: http://localhost:3000

Login: admin / admin

Loki API: http://localhost:3100

 Log Streaming from Flask App
Logs from the Flask app are:

Written to /var/log/flask/app.log inside the container

Mounted and read by Promtail

Shipped to Loki

Queryable in Grafana

Example Log Query in Grafana Explore

{job="flask"}
 Setup in Grafana
Add Data Sources
Prometheus

URL: http://prometheus:9090

Loki

URL: http://loki:3100

 To Tear Down

docker-compose down

 Future Ideas
Add log labels per container/service

Push metrics to cloud (e.g., Grafana Cloud)

Add Alertmanager integration

 Author
ViorelH — DevOps Portfolio Project 5: Monitoring Stack with Metrics + Logs
