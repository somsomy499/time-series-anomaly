"""Ensemble anomaly detector."""
import numpy as np
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class AnomalyResult:
    timestamp: float
    value: float
    score: float
    is_anomaly: bool
    method: str

class AnomalyDetector:
    def __init__(self, method="ensemble", threshold=0.95):
        self.method = method
        self.threshold = threshold
        
    def detect(self, data):
        results = []
        for i, val in enumerate(data):
            score = self._score(val, data, i)
            results.append(AnomalyResult(
                timestamp=i, value=val, score=score,
                is_anomaly=score > self.threshold, method=self.method
            ))
        return results
        
    def _score(self, val, data, idx):
        mean = np.mean(data)
        std = np.std(data) + 1e-8
        return min(1.0, abs(val - mean) / (3 * std))
