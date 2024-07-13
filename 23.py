class Airport:
    def __init__(self,name:str,location:str) -> None:
        self.name = name
        self.location = location

    def get_info(self:str):
        return f"""
        Ismi: {self.name}
        Location: {self.location}
        """
    def colculate(self:float):
        return 0.0
    
class InternationalAirport(Airport):
    
    def __init__(self, name: str, location: str, num_international_flight: int) -> None:
        super().__init__(name, location)
        self.num_international_flight = num_international_flight

    def get_info(self) -> str:
        return f"""
        Nomi: {self.name}
        Manzil: {self.location}
        Xalqaro parvozlar soni: {self.num_international_flight}
        """
    
    def colculate(self: float):
        return self.num_international_flight * 500
    
class DomesticAirport(Airport):
    def __init__(self, name: str, location: str,num_demostic_flight:int) -> None:
        super().__init__(name, location)
        self.num_demostic_flight = num_demostic_flight

    def get_info(self: str):
        return f"""
        Nomi: {self.name}
        Manzil: {self.location}
        Parvoz soni: {self.num_demostic_flight}
        """
    
    def colculate(self):
        return self.num_demostic_flight * 100
    

natija = Airport("Airport Name","Andijan")
print(natija.get_info())
print(f"Narxi: {natija.colculate()}")

natijaaa = InternationalAirport("Airport Name","Farg'ona",5)
print(natijaaa.get_info())
print(f"Narxi: {natijaaa.colculate()}")

natijaa = DomesticAirport("Airport Name","Tashkent",3)
print(natijaa.get_info())
print(f"Narxi: {natijaa.colculate()}")

