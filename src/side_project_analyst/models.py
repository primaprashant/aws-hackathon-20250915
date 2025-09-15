from pydantic import BaseModel, Field
from typing import List, Dict, Any


# Input Model
class ProjectIdea(BaseModel):
    """User's project idea input"""
    description: str = Field(..., description="Project idea description")
    goals: List[str] = Field(..., description="Project goals")
    target_audience: str = Field(..., description="Target audience")


# Search Agent Outputs
class MarketInsights(BaseModel):
    """Market research findings"""
    market_size: str
    competition_level: str
    opportunities: List[str]
    challenges: List[str]


class TechnicalAnalysis(BaseModel):
    """Technical feasibility"""
    tech_stack: Dict[str, List[str]]
    complexity: str
    estimated_time: str
    challenges: List[str]


class UserResearch(BaseModel):
    """User research findings"""
    pain_points: List[str]
    user_needs: List[str]
    personas: List[Dict[str, Any]]


class CompetitorAnalysis(BaseModel):
    """Competitor analysis"""
    competitors: List[Dict[str, str]]
    market_gaps: List[str]
    competitive_advantages: List[str]


class TrendAnalysis(BaseModel):
    """Industry trends"""
    trends: List[str]
    growth_indicators: List[str]
    future_outlook: str


# Strategy Outputs
class MarketingStrategy(BaseModel):
    """Marketing plan"""
    value_proposition: str
    channels: List[str]
    messaging: Dict[str, str]
    campaigns: List[str]


class SEOStrategy(BaseModel):
    """SEO plan"""
    keywords: List[str]
    content_topics: List[str]
    technical_requirements: List[str]


class GoToMarketPlan(BaseModel):
    """Launch plan"""
    timeline: List[Dict[str, str]]
    launch_activities: List[str]
    growth_tactics: List[str]
    success_metrics: List[str]


class ValidationReport(BaseModel):
    """Project validation"""
    viability_score: str  # "high", "medium", "low"
    strengths: List[str]
    weaknesses: List[str]
    risks: List[str]
    recommendation: str


# Final Report
class AnalysisReport(BaseModel):
    """Complete analysis report"""
    project: ProjectIdea
    market: MarketInsights
    technical: TechnicalAnalysis
    users: UserResearch
    competitors: CompetitorAnalysis
    trends: TrendAnalysis
    marketing_strategy: MarketingStrategy
    seo_strategy: SEOStrategy
    go_to_market: GoToMarketPlan
    validation: ValidationReport