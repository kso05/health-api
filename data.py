import json
from .health import Health
import pandas as pd

def save_json(barbie: list[Health], filename: str = 'src/health_app/health_records.json'):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        with open(filename, 'w') as json_file:  
            for b in barbie:
                data.append({
                "name": b.name,
                "weight_kg": b.weight_kg,
                "height_m": b.height_m,
                "bmi": b.bmi,
                "bmi_category": b.get_category()
                })
            json.dump(data, json_file, indent=2)

    except FileNotFoundError as e: 
        print(e)
        print("Error, file not found")

def load_json(filename: str = 'src/health_app/health_records.json') -> list[Health]: 
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

        health_list = []

        for item in data:
            h = Health(  
                item["name"],
                item["weight_kg"],
                item["height_m"]
            )
            health_list.append(h)

        return health_list

    except FileNotFoundError as e:
        return []

def get_statistics(filename: str = "src/health_app/health_records.json") -> dict:
    df = pd.read_json(filename) 
    total_records = len(df)
    avg_bmi = round(df['bmi'].mean(), 2)
    most_common_category = df['bmi_category'].mode()[0]
    category_distribution = df['bmi_category'].value_counts().to_dict()

    return{
        "total_records": total_records,
        "avg_bmi": avg_bmi,
        "most_common_category": most_common_category,
        "category_distribution": category_distribution
    }
