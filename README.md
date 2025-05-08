
# 🌍 GeoModule — Find Closest GPS Points

**GeoModule** is a Python utility that finds the closest GPS coordinate in one dataset to each point in another.  
It’s built for developers and analysts working with geographic data — think cities matched to the nearest airport, service requests matched to field offices, etc.

---

## 📦 Features

- 📍 Match each point in dataset A to the **closest** point in dataset B
- 🧠 Uses the accurate **Haversine formula** (great-circle distance)
- 🔄 Supports **CSV**, **JSON**, or **manual input**
- 📂 Saves results in structured JSON format with distances
- 🛠 CLI and batch testing via `main.py` and `test_runner.py`

---

## 🗂 Project Structure

```

GeoLocation---Ex1/
├── geomodule/
│   ├── matcher.py       # Distance logic (Haversine + matching)
│   └── io\_utils.py      # CSV, JSON, and manual input/output
├── test\_cases/          # Example datasets and output files
├── main.py              # CLI tool for matching coordinates
├── test\_runner.py       # Batch testing runner
├── requirements.txt     # Dependencies (e.g., requests)
└── README.md            # This file

````

---

## 🚀 Getting Started

### 🔧 1. Install Dependencies

```bash
pip install -r requirements.txt
````

---

### 🖥 2. Run with CLI

```bash
python main.py
```

Choose from:

1. Load from CSV
2. Load from JSON
3. Manual input

> ✅ Results will be saved to `output.json`.

---

### 🧪 3. Batch Testing

Configure `test_runner.py` like this:

```python
test_configs = [
    ("test_cases/world_cities.csv", "test_cases/iata_airports.csv", "csv")
]
```

Run with:

```bash
python test_runner.py
```

✔️ Output is saved in `test_cases/` with timestamp.

---

## 📄 Sample Output

```json
{
  "timestamp": "2025-05-08T06:33:47Z",
  "source_A": "world_cities.csv",
  "source_B": "iata_airports.csv",
  "results": [
    {
      "from": { "lat": 42.35036, "lon": -71.096966 },
      "to": { "lat": 42.2702, "lon": -71.0844 },
      "distance_km": 8.97
    }
  ]
}
```

---

## 🌐 Tested Data Sources

* 🌍 [World Cities CSV](https://raw.githubusercontent.com/joelacus/world-cities/refs/heads/main/world_cities.csv)
* ✈️ [IATA Airport CSV](https://github.com/ip2location/ip2location-iata-icao/blob/master/iata-icao.csv)
* 🏙 Boston 311 Service Request GPS Reports

---

## 💡 Future Ideas

* Filter by bounding radius (e.g. only match if within 100km)
* Group matches by country or region
* Visualize matches using Folium, Plotly, or Streamlit
* Optimize using KDTree (scikit-learn)

---
