from typing import Optional
from pydantic import BaseModel, ConfigDict


class MenuBase(BaseModel):
    menuDish: str
    menuIngredients: str
    menuPrice: float
    menuCalories: int
    menuCategory: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(BaseModel):
    menuDish: Optional[str] = None
    menuIngredients: Optional[str] = None
    menuPrice: Optional[float] = None
    menuCalories: Optional[int] = None
    menuCategory: Optional[str] = None


class Menu(MenuBase):
    menuID: int

    model_config = ConfigDict(from_attributes=True)