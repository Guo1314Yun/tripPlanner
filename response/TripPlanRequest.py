from typing import List, Optional

from pydantic import Field, BaseModel

from helloagents_trip_planner.backend.models.base_entity import DayPlan, WeatherInfo, Budget


class TripPlanRequest(BaseModel):
    city: str = Field(...,description="目的地城市")
    accommodation: str = Field(...,description="住宿")
    preferences: str = Field(...,description="偏好")
    start_date: str = Field(...,description="开始日期")
    end_date: str = Field(...,description="结束日期")
    days: List[DayPlan] = Field(default_factory=list,description="每日行程")
    weather_info: List[WeatherInfo] = Field(default_factory=list,description="天气信息")
    overall_suggestions: str = Field(...,description="总体建议")
    budget: Optional[Budget] = Field(default=None,description="预算信息")
    transportation: str = Field(default=None,description="交通方式")