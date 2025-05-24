# Monitoring Stack: Prometheus + Grafana + Loki

A complete observability stack for metrics and logs using Docker Compose.

## 📊 What's Included

- **Prometheus** — Metrics collection (scrapes targets)
- **Grafana** — Dashboards and visualization
- **Loki** — Log aggregation

## 🧱 Project Structure

monitoring-stack/
├── docker-compose.yml
├── prometheus/
│ └── prometheus.yml # Prometheus scrape config
├── loki/
│ └── config.yaml # Loki log storage config
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Run the stack

```bash
docker-compose up --build
🌐 Access Services
Prometheus: http://localhost:9090

Grafana: http://localhost:3000

Login: admin / admin

Loki API: http://localhost:3100

⚙️ Setup in Grafana
Add Data Sources
Prometheus

URL: http://prometheus:9090

Loki

URL: http://loki:3100

Create Dashboards
Build metrics panels (CPU, memory, uptime)

Use Loki to view logs from connected services

🧼 Stopping the Stack
bash
Copy
Edit
docker-compose down
📦 Future Enhancements
Forward logs from a Flask app to Loki using promtail

Set up alerting with Prometheus Alertmanager

Push to production cluster with Kubernetes

🙌 Author
ViorelH — Monitoring stack project for DevOps portfolio