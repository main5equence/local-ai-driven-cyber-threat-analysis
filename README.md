# Local AI-Driven Cyber-Threat Analysis

## Overview

Local AI-driven Cyber-Threat Analysis is a lightweight cybersecurity monitoring platform designed to analyze network activity, detect suspicious behavior, and generate AI-powered incident analysis using locally hosted language models.

The system monitors network traffic in real time, detects anomalies such as port scanning or suspicious activity, and visualizes incidents through an interactive Streamlit dashboard.

All threat analysis is performed locally using Ollama and local LLMs, ensuring that sensitive network data is not sent to external cloud services.

---

## Features
- Real-time network traffic monitoring
- Packet sniffing with Scapy
- Threat and anomaly detection
- AI-powered incident analysis
- Local LLM integration using Ollama
- Threat severity classification
- JSON alert generation
- SQLite incident database
- Interactive Streamlit dashboard
- Threat analytics and visualizations
- Simulated cybersecurity incident generation
- Fully local/offline architecture

---

## Technologies Used
- Python
- Streamlit
- Scapy
- SQLite
- SQLAlchemy
- Ollama
- Mistral LLM
- Pandas
- Nmap

---

## System Architecture
```
Network Traffic
       ↓
Packet Sniffer (Scapy)
       ↓
Threat Detection Engine
       ↓
JSON Incident Generator
       ↓
AI Threat Analysis (Ollama + Mistral)
       ↓
SQLite Database
       ↓
Streamlit Dashboard
```


## JSON Alert Logging

When the system detects suspicious network activity, it automatically generates a structured JSON alert containing information about the detected incident.

Alerts are stored locally inside the `alerts/` directory and can be used for:
- threat analysis,
- debugging,
- incident history,
- forensic investigation,
- future SIEM integrations.

---

### Example Alert

Example generated alert file:

```text
alerts/PORT_SCAN_192.168.0.15.json
```

<img width="410" height="42" alt="Zrzut ekranu 2026-05-15 132806" src="https://github.com/user-attachments/assets/eee52081-4aaa-42ec-b4de-1310183273b5" />


Example JSON structure:

```JSON
{
    "timestamp": "2026-05-15 18:22:10",
    "event_type": "PORT_SCAN",
    "source_ip": "192.168.X.X",
    "severity": "HIGH"
}
```

Alert Workflow

```
Network Traffic
      ↓
Threat Detection
      ↓
JSON Alert Generation
      ↓
AI Threat Analysis
      ↓
SQLite Database
      ↓
Streamlit Dashboard
```

The generated alert is then analyzed by the local AI model running through Ollama and displayed in the Streamlit dashboard together with threat analytics and severity information.

---

### AI Threat Analysis with Ollama

After detecting suspicious network activity and generating a JSON alert, the incident is sent to a locally running AI model through Ollama for further analysis.
The AI engine analyzes the alert data, evaluates the potential threat severity, and generates a human-readable explanation of the incident together with security recommendations.
The entire analysis process is performed locally without sending network data to external cloud services.


<img width="1906" height="623" alt="Zrzut ekranu 2026-05-15 152036" src="https://github.com/user-attachments/assets/5ae7257d-0ab3-467c-8302-c90b3d87d6ca" />


AI Analysis Workflow

```text
Threat Detection
      ↓
JSON Alert Generated
      ↓
Prompt Creation
      ↓
Ollama Local LLM Analysis
      ↓
Threat Severity Evaluation
      ↓
Security Recommendations
      ↓
SQLite Database
      ↓
Streamlit Dashboard
```

Example AI Prompt

```text
You are a cybersecurity SOC analyst.
Analyze this security incident:

{
  "event_type": "PORT_SCAN",
  "source_ip": "192.168.X.X",
  "severity": "HIGH"
}

Provide:
- Threat level
- Explanation
- Possible risks
- Recommended actions
```

Example AI Response
```text
Threat Level: 7/10

The system detected behavior consistent with a port scan.
This activity may indicate reconnaissance attempts before a potential attack.

Possible risks:
- Vulnerability discovery
- Unauthorized access attempts
- Malware activity

Recommended actions:
1. Identify the source device
2. Verify firewall configuration
3. Scan the device for malware
4. Monitor further suspicious activity
```
Local AI Processing

The project uses:
- Ollama
- Local LLMs (e.g. Mistral)

which allows all AI threat analysis to remain fully local and privacy-focused.
No traffic data or incidents are sent to external AI providers or cloud services.


---


## Dashboard Features
- Threat severity metrics
- AI-generated threat analysis
- Threat type distribution
- Suspicious IP activity
- Incident history
- Real-time cybersecurity analytics
  

<img width="1795" height="666" alt="Zrzut ekranu 2026-05-15 134031" src="https://github.com/user-attachments/assets/dbca4cb3-9d7a-4710-a801-185d9c15c586" />


<img width="1782" height="443" alt="Zrzut ekranu 2026-05-15 134106" src="https://github.com/user-attachments/assets/3981197a-fbde-4e38-bb76-89f4edc43d6e" />


<img width="467" height="513" alt="Zrzut ekranu 2026-05-15 134154" src="https://github.com/user-attachments/assets/1766d26d-ddd1-42e7-acd9-9b9d839c5c53" />


<img width="1780" height="842" alt="Zrzut ekranu 2026-05-15 140300" src="https://github.com/user-attachments/assets/5f7b8af6-f72d-4b84-b44e-d5156d7a85e8" />




## Project Structure
```
local-ai-cyber-threat-analysis/
│
├── app/
│   │
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── ai_engine.py
│   │   └── prompt_builder.py
│   │
│   ├── dashboard/
│   │   ├── __init__.py
│   │   └── dashboard.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── models.py
│   │   └── save_threat.py
│   │
│   ├── incidents/
│   │   ├── __init__.py
│   │   ├── json_generator.py
│   │   └── playbook_loader.py
│   │
│   ├── monitor/
│   │   ├── __init__.py
│   │   ├── anomaly_detector.py
│   │   └── packet_sniffer.py
│   │
│   └── simulator/
│       ├── __init__.py
│       └── threat_simulator.py
│
├── playbooks/
│   ├── brute_force.json
│   ├── dns_tunneling.json
│   ├── malware_traffic.json
│   ├── port_scan.json
│   └── suspicious_traffic.json
│
├── screenshots/
│   ├── dashboard.png
│   ├── packet_sniffer.png
│   ├── ai_analysis.png
│   └── architecture_diagram.png
│
├── .gitignore
├── README.md
├── requirements.txt
├── setup_db.py
└── simulate_threats.py
```
---

## Threat Simulation

The project includes a threat simulation module (`simulate_threats.py`) used for generating example cybersecurity incidents for testing, demonstrations, and dashboard visualization.

The simulator creates artificial threats such as:
- PORT_SCAN
- BRUTE_FORCE
- MALWARE_TRAFFIC
- DDOS_ATTEMPT
- DNS_TUNNELING
and sends them to the local AI analysis engine.

<img width="302" height="106" alt="Zrzut ekranu 2026-05-15 133946" src="https://github.com/user-attachments/assets/aef0971c-2ff6-48e5-b67c-3dd7ec46dd0d" />

<img width="337" height="98" alt="Zrzut ekranu 2026-05-15 133722" src="https://github.com/user-attachments/assets/f39d4b11-9139-4d22-95f2-8f0eaa44ef4b" />

---

### Using Real Local Network Monitoring Only

If you want to use the project only for real local network monitoring and do not want to generate artificial threats:

1. Do not run:

```
python simulate_threats.py
```

2. Start only the real network monitoring module:
```
python -m app.main
```

3. (Optional) You can remove or ignore:
```
simulate_threats.py
app/simulator/
```

The Streamlit dashboard will then display only real network activity and detected incidents from your local environment.

---

## Installation

Clone repository

```
git clone https://github.com/YOUR_USERNAME/local-ai-cyber-threat-analysis.git
```

```
cd local-ai-cyber-threat-analysis
```

Install dependencies

```
pip install -r requirements.txt
```

Install Ollama

Install Ollama locally: https://ollama.com/


Pull AI model
```
ollama pull mistral
```

Initialize database
```
python setup_db.py
```
---

## Running the Project

Start Streamlit dashboard
```
streamlit run app/dashboard/dashboard.py
```
Local Streamlit Dashboard:
http://localhost:8501


Generate simulated threats
```
python simulate_threats.py
```

Start live network monitoring
```
python -m app.main
```

Generate real port scan test
```
nmap 127.0.0.1
```


## Educational Purpose
This project was created for educational and research purposes related to cybersecurity, AI-powered threat analysis, and local LLM integration. Project was developed as part of the SheCODE:ME Cyber Academy within the CODE:ME Shell Scholarship Programme for Women, focused on developing practical skills in cybersecurity, AI, and dual-use modern technologies.


## Important
Always use the monitoring and packet analysis features responsibly and only on networks you own or are authorized to test.






















