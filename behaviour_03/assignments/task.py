from pydantic import BaseModel, Field, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >= 1)
# - price_per_night: float
# Also, add computed field: total_amount = nights * price_per_night

class BookingModel(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(
        ...,
        ge=1,
        description="Number of nights must be at least 1",
    )
    price_per_night: float 
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.price_per_night
    
booking_01 = {
    "user_id": 101,
    "room_id": 202,
    "nights": 4,
    "price_per_night": 150.0
}

booking_1 = BookingModel(**booking_01)
print(booking_1)