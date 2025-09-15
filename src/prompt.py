def get_vision_doc() -> str:
    return f"""
You will be creating a comprehensive vision document for a side project app idea. Your goal is to transform a basic project concept into a detailed launch strategy that covers all essential aspects needed to successfully bring the app to market.

The project idea you'll be working with will be provided by the user.

Your task is to create a comprehensive vision document that will serve as a roadmap for launching this app. The document should be practical, actionable, and thorough.

Before writing your final vision document, use the scratchpad below to analyze the project idea and plan your approach:

<scratchpad>
Think through the following:
- What is the core problem this app solves?
- Who is the target audience?
- What are the key features and value propositions?
- What market category does this fit into?
- What would be the main challenges and opportunities?
- What would make this app stand out from competitors?
</scratchpad>

Your vision document must include the following sections:

**Executive Summary**: A brief overview of the app concept, target market, and key success factors.

**Market Analysis**: Identify the target audience, market size, competitors, and market opportunity.

**Product Vision**: Detailed description of the app's core features, user experience, and unique value proposition.

**Marketing Plan**: Comprehensive strategy including:
- Target customer personas
- Marketing channels and tactics
- Content marketing strategy
- Social media approach
- Launch strategy and timeline
- Budget considerations

**SEO Strategy**: Specific SEO focus including:
- Primary and secondary keywords
- Content strategy for organic growth
- Technical SEO considerations
- Local SEO if applicable

**Branding & Design**:
- Logo concept and design direction
- Brand personality and voice
- Color scheme and visual identity
- UI/UX design principles

**Technical Considerations**: Platform choices, key technical requirements, and development approach.

**Monetization Strategy**: Revenue model, pricing strategy, and financial projections.

**Success Metrics**: Key performance indicators and milestones to track progress.

**Risk Assessment**: Potential challenges and mitigation strategies.

**Launch Roadmap**: Step-by-step timeline from development to launch and beyond.

Make your recommendations specific and actionable. Include concrete examples, specific tools or platforms to use, and realistic timelines. Base all suggestions on the specific PROJECT_IDEA provided, ensuring everything is tailored to that particular concept.

Your final output should be a complete, well-structured vision document that someone could realistically use to guide their app development and launch process. Focus on practical, implementable advice rather than generic recommendations.
"""



# to include web search results

def get_vision_doc_2() -> str:
    return f"""
You will be creating a comprehensive vision document for a side project app idea. Your goal is to transform a basic project concept into a detailed launch strategy that covers all essential aspects needed to successfully bring the app to market.

The project idea you'll be working with will be provided by the user.

You will be given a tool to search the web for information.
For your search, focus on finding information about:
- Direct competitors or similar projects
- Adjacent solutions
- Market landscape
- Success stories and failures
- Technology approaches
- Target audiences

Your task is to create a comprehensive vision document that will serve as a roadmap for launching this app. The document should be practical, actionable, and thorough. The document should be based on the project idea and the information you found from the web search.

Before writing your final vision document, use the scratchpad below to analyze the project idea and plan your approach:

<scratchpad>
Think through the following:
- What is the core problem this app solves?
- Who is the target audience?
- What are the key features and value propositions?
- What market category does this fit into?
- What would be the main challenges and opportunities?
- What would make this app stand out from competitors?
</scratchpad>

Your vision document must include the following sections:

**Executive Summary**: A brief overview of the app concept, target market, and key success factors.

**Market Analysis**: Identify the target audience, market size, competitors, and market opportunity.

**Product Vision**: Detailed description of the app's core features, user experience, and unique value proposition.

**Marketing Plan**: Comprehensive strategy including:
- Target customer personas
- Marketing channels and tactics
- Content marketing strategy
- Social media approach
- Launch strategy and timeline
- Budget considerations

**SEO Strategy**: Specific SEO focus including:
- Primary and secondary keywords
- Content strategy for organic growth
- Technical SEO considerations
- Local SEO if applicable

**Branding & Design**:
- Logo concept and design direction
- Brand personality and voice
- Color scheme and visual identity
- UI/UX design principles

**Technical Considerations**: Platform choices, key technical requirements, and development approach.

**Monetization Strategy**: Revenue model, pricing strategy, and financial projections.

**Success Metrics**: Key performance indicators and milestones to track progress.

**Risk Assessment**: Potential challenges and mitigation strategies.

**Launch Roadmap**: Step-by-step timeline from development to launch and beyond.

Make your recommendations specific and actionable. Include concrete examples, specific tools or platforms to use, and realistic timelines. Base all suggestions on the specific PROJECT_IDEA provided, ensuring everything is tailored to that particular concept.

Your final output should be a complete, well-structured vision document that someone could realistically use to guide their app development and launch process. Focus on practical, implementable advice rather than generic recommendations.
"""


