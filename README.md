# Time-Series Anomaly Detection 📊

Real-time anomaly detection for streaming time-series data with ensemble methods.

## Methods

- **Autoencoder**: Deep learning reconstruction-based
- **Isolation Forest**: Tree-based outlier detection  
- **Prophet**: Seasonal decomposition
- **Ensemble**: Weighted combination of above

## Benchmarks

| Method | Precision | Recall | F1 | Latency |
|--------|-----------|--------|-----|---------|
| Autoencoder | 0.92 | 0.88 | 0.90 | 5ms |
| Isolation Forest | 0.85 | 0.91 | 0.88 | 2ms |
| Prophet | 0.78 | 0.83 | 0.80 | 50ms |
| Ensemble | 0.94 | 0.90 | 0.92 | 15ms |

## Quick Start

```python
from ts_anomaly import AnomalyDetector

detector = AnomalyDetector(method="ensemble")
results = detector.detect(streaming_data)
anomalies = results.filter(threshold=0.95)
```

## License

MIT