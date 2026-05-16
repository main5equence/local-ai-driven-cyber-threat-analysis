def build_prompt(alert):

    return f"""
You are a cybersecurity SOC analyst.

Analyze this incident:

{alert}

Provide:
- Threat level (1-10)
- Explanation
- Possible risks
- Recommended actions

Explain simply.
"""
