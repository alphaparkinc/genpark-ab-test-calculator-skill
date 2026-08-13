![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![License MIT](https://img.shields.io/badge/license-MIT-green) ![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-purple) ![GenPark AI](https://img.shields.io/badge/GenPark-AI--Agent--Skill-orange)

# genpark-ab-test-calculator-skill

> **GenPark AI Agent Skill** -- Two-tailed Z-score A/B test statistical calculator.

## Quick Start

```python
from client import ABTestCalculatorClient
client = ABTestCalculatorClient()
res = client.calculate_results(5000, 100, 5000, 140)
print(res["is_significant"])
```

## 📊 Agentic Architecture Flowchart
```mermaid
graph LR
  User([User / AI Agent]) -->|JSON Request| Skill[GenPark AI Skill]
  Skill -->|Execution Logic| CoreEngine[Core Analytics & Processing]
  CoreEngine -->|Structured Output| User
```

## 🔌 MCP (Model Context Protocol) Integration
Run natively as an MCP server for Cursor, Claude Desktop & LLM frameworks:
```bash
python mcp_server.py
```
