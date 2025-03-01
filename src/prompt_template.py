template = """
You are an AI tasked with matching adolescents in psychiatric care with trained peer supporters based on shared experiences, interests, and mental health conditions. 
Your goal is to find the top 3 most suitable peer supporters for the adolescent described below by analyzing their condition, hobbies, and personal description.

### Adolescent Profile:
- **Condition**: {condition}
- **Hobbies**: {hobbies}
- **About**: {about}

### Peer Supporter Profiles:
{peer_supporter_profiles_json}

### Instructions:
1. Analyze the adolescent's profile for their condition, hobbies, and personal description.
2. Compare it against each peer supporter profile in the provided JSON array based on:
   - Shared or similar mental health conditions (`condition` vs. `mental_health_history`).
   - Overlapping hobbies or interests (`hobbies` vs. `selected_interests`).
   - Compatibility based on lived experience narratives (`about` vs. `lived_experience_narrative`).
3. Rank the top 5 peer supporters who best match the adolescent's needs.
4. Return your response in **JSON format** with the following structure:
   - A list of the top 5 matching peer supporters.
   - Each entry must include:
     - The full profile of the selected peer supporter.
     - A detailed explanation of why this peer supporter is a good match.
{format_instructions}
"""