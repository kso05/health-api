from src.health_app.health import Health
import pytest


def test_valid_input():
    """Test valid input"""
    b = Health("Victoria", 65, 1.70)

    assert b.name == "Victoria"
    assert b.weight_kg == 65
    assert b.height_m == 1.70


def test_input_validation(): 
    """Test input validation"""
    with pytest.raises(ValueError):
        Health("Victoria", -65, "hello")

def test_bmi_calculation():
    """"BMI calculation"""
    b1 = Health("Victoria", 65, 1.70)
    
def test_bmi_categorization():
    """BMI categorization"""
    underweight = Health("A", 45, 1.70)   
    normal = Health("B", 65, 1.70)        
    overweight = Health("C", 80, 1.70)    
    obese = Health("D", 100, 1.70) 

    assert underweight.get_category() == "Underweight"
    assert normal.get_category() == "Normal"
    assert overweight.get_category() == "Overweight"
    assert obese.get_category() == "Obese"       


def test_health_advice():
    """Health Advice"""
    underweight = Health("A", 45, 1.70)
    normal = Health("B", 65, 1.70)
    overweight = Health("C", 80, 1.70)
    obese = Health("D", 100, 1.70)

    assert "eat more" in underweight.get_health_advice().lower()
    assert "healthy range" in normal.get_health_advice().lower()
    assert "physical activity" in overweight.get_health_advice().lower()
    assert "obesity" in obese.get_health_advice().lower()



def test_ideal_weight_calculation():
    """Ideal weight calculation"""
    b = Health("Victoria", 65, 1.70)

    expected = round(22 * (1.70 ** 2), 1)
    assert b.get_ideal_weight() == expected




    