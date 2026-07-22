from pydantic import BaseModel, Field, computed_field
from constants.prediction_constant import AgencyType, AgencyCategory, Channel, ProductName, Destination


class CreatePredictionRequest(BaseModel):
    agency: AgencyType
    agency_type: AgencyCategory
    distribution_channel: Channel
    product_name: ProductName
    destination: Destination
    
    duration: int = Field(gt=0, description="Durasi perjalanan dalam hari")
    net_sales: float = Field(description="Nilai penjualan bersih (bisa negatif jika refund)")
    commission: float = Field(ge=0, description="Nilai komisi (minimal 0)")
    age: int = Field(ge=0, le=120, description="Usia penumpang")

    @computed_field
    @property
    def is_refund(self) -> str:
        return "Yes" if self.net_sales < 0 else "No"

    @computed_field
    @property
    def suspected_fraud(self) -> str:
        return "Yes" if self.net_sales < 0 and self.commission > 0 else "No"

    @computed_field
    @property
    def commission_rate(self) -> float:
        if self.net_sales <= 0:
            return 0.0
        return self.commission / self.net_sales