# Side Project Idea Analysis Workflow

## Overview
This workflow analyzes a side project idea using an orchestrator agent that distributes search tasks to multiple search agents working in parallel with web search capabilities, then merges insights to generate comprehensive marketing and SEO strategies.

## Workflow Architecture

```mermaid
graph TB
    %% Input
    UserInput["User's Project Idea<br/>(Description, Goals, Target Audience)"]

    %% Orchestrator
    UserInput --> Orchestrator["Orchestrator Agent<br/>(Distributes search tasks)"]

    %% Search Agents (Parallel)
    Orchestrator --> MarketSearchAgent["Market Search Agent<br/>(Market size, competition)"]
    Orchestrator --> TechSearchAgent["Technical Search Agent<br/>(Tech stack, complexity)"]
    Orchestrator --> UserSearchAgent["User Search Agent<br/>(Pain points, personas)"]
    Orchestrator --> CompetitorSearchAgent["Competitor Search Agent<br/>(Existing solutions)"]
    Orchestrator --> TrendSearchAgent["Trend Search Agent<br/>(Industry trends, growth)"]

    %% Web Search Tools (MCP)
    MarketSearchAgent -.->|Uses| WebSearch1["Web Search<br/>(Firecrawl MCP)"]
    TechSearchAgent -.->|Uses| WebSearch2["Web Search<br/>(GitHub, StackOverflow)"]
    UserSearchAgent -.->|Uses| WebSearch3["Web Search<br/>(Reddit, Forums)"]
    CompetitorSearchAgent -.->|Uses| WebSearch4["Web Search<br/>(Product Hunt, G2)"]
    TrendSearchAgent -.->|Uses| WebSearch5["Web Search<br/>(Google Trends, News)"]

    %% Merge Node
    MarketSearchAgent --> MergerAgent["Insight Merger Agent<br/>(Synthesizes all findings)"]
    TechSearchAgent --> MergerAgent
    UserSearchAgent --> MergerAgent
    CompetitorSearchAgent --> MergerAgent
    TrendSearchAgent --> MergerAgent

    %% Strategy Generation
    MergerAgent --> StrategyAgent["Strategy Generator Agent<br/>(Marketing & SEO planning)"]

    %% Output Nodes
    StrategyAgent --> MarketingPlan["Marketing Strategy<br/>(Channels, messaging, positioning)"]
    StrategyAgent --> SEOPlan["SEO Strategy<br/>(Keywords, content plan)"]
    StrategyAgent --> GTMPlan["Go-to-Market Plan<br/>(Launch strategy, timeline)"]
    StrategyAgent --> ValidationReport["Validation Report<br/>(Viability score, risks)"]

    %% Final Output
    MarketingPlan --> FinalReport["Complete Analysis Report"]
    SEOPlan --> FinalReport
    GTMPlan --> FinalReport
    ValidationReport --> FinalReport

    %% Styling with dark text
    classDef inputStyle fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000000
    classDef agentStyle fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000000
    classDef webStyle fill:#f3e5f5,stroke:#4a148c,stroke-width:1px,stroke-dasharray: 5 5,color:#000000
    classDef outputStyle fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px,color:#000000
    classDef finalStyle fill:#fce4ec,stroke:#880e4f,stroke-width:3px,color:#000000

    class UserInput inputStyle
    class Orchestrator,MarketSearchAgent,TechSearchAgent,UserSearchAgent,CompetitorSearchAgent,TrendSearchAgent,MergerAgent,StrategyAgent agentStyle
    class WebSearch1,WebSearch2,WebSearch3,WebSearch4,WebSearch5 webStyle
    class MarketingPlan,SEOPlan,GTMPlan,ValidationReport outputStyle
    class FinalReport finalStyle
```
