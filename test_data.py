import json
from src.health_app.health import Health
from src.health_app.data import save_json, load_json, get_statistics

def test_save_and_load():
 
    with open("health_records_test.json", "w") as file:
        json.dump([], file)  
        
        """Save/load roundtrip"""
    people = [
        Health("Victoria", 90, 1.75),
        Health("Millie", 50, 1.80)
    ]

    save_json(people, "health_records_test.json")
    loaded = load_json("health_records_test.json")

    assert len(loaded) == 2
    assert loaded[0].name == "Victoria"
    assert loaded[1].weight_kg == 50

    




def test_load_nonexistent_file():
    """Load empty/nonexistent file"""
    
    records = load_json("this_file_doesnt_exist.json")
    
    assert records == []

def test_statistics_calculation():
    """Statistics calculation (all fields)"""

    filename = "test_stats.json"
    test_data = [
        {"name": "Victoria", "weight_kg": 70, "height_m": 1.75, "bmi": 22.86, "bmi_category": "Normal"},
        {"name": "Bob", "weight_kg": 110, "height_m": 1.70, "bmi": 38.06, "bmi_category": "Obese"}
    ]
    with open(filename, "w") as f:
        json.dump(test_data, f)

    test_data = get_statistics(filename)

    assert test_data["total_records"] == 2
    assert test_data["avg_bmi"] == 30.46 
    assert "most_common_category" in test_data
    assert "category_distribution" in test_data

def test_category_distribution():
    """Category distribution accuracy"""
    stats = get_statistics()
    
    distribution = stats["category_distribution"]
    
    assert "Overweight" in distribution
    assert "Underweight" in distribution