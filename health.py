class Health:
    def __init__(self, name: str, weight_kg: float, height_m: float):

        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        try:  
            if weight_kg <= 0:
                raise ValueError("Weight must be greater than 0.")
        
            if height_m <= 0:
                raise ValueError("Height must be greater than 0.")
        except:
             raise ValueError("Must enter float")
        
        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.bmi = round(weight_kg / (height_m ** 2), 2)
        
    def get_category(self) -> str:
            if self.bmi < 18.5:
                return "Underweight"
            elif 18.5 <= self.bmi < 25:
                return "Normal"
            elif 25 <= self.bmi < 30:
                return "Overweight"
            else:
                return "Obese"
            
    
    def get_health_advice(self) -> str:
            category = self.get_category()
            if category == "Underweight":
                return (
                "You really need to eat more king/queen. Get some calorie heavy foods in you rn! "
            )
            elif category == "Normal":
                return (
                "Your BMI is in the healthy range. Maintain this glorious balanced life."
            )
            elif category == "Overweight":
                return (
                "You may benefit from increasing physical activity and improving dietary habits. "
                "Please reduce those processed foods"
            )
            else:
                return (
                "Your BMI suggests obesity. You are offically on the way to become massive and girthy. Please eat less and take care of yourself"
            )

            
        
    def get_ideal_weight(self) -> float:
            return round(22 * (self.height_m ** 2), 1)
        
        
        
        
