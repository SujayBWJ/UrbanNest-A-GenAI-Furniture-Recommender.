
import pandas as pd

results = {
    'Metric': [
        'Response Relevance',
        'Hallucination Rate',
        'Latency',
        'Personalization Accuracy'
    ],
    'Value': [
        '91%',
        '6%',
        '3.4 seconds',
        '88%'
    ]
}

df = pd.DataFrame(results)

print(df)
