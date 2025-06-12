from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class TfidfEntry(BaseModel):
    term: str
    tf: float
    idf: float
    score: float


class StatisticsBase(BaseModel):
    document_id: int = Field(..., description="ID of the document this statistic belongs to")
    tfidf_json: Optional[Dict[str, Any]] = Field(None, description="Top 50 TF-IDF words with scores")


class StatisticsCreate(BaseModel):
    document_id: int
    tfidf_json: List[Dict[str, Any]] 


class StatisticsUpdate(BaseModel):
    tfidf_json: Optional[List[Dict[str, Any]]] = Field(None, description="Updated TF-IDF scores")


class StatisticsRead(StatisticsBase):
    """Schema for reading statistics (response model)"""
    id: int = Field(..., description="Unique statistics ID")
    created_at: datetime = Field(..., description="Timestamp when TF-IDF was generated")
    tfidf_json: List[Dict[str, Any]]
    
    class Config:
        from_attributes = True 
