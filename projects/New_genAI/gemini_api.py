import google.generativeai as genai

# Always keep your API key secure
genai.configure(api_key="AIzaSyAe7py0ok82pNrJgk82V-O48RyaXSDTogQ")

def generate_project_ideas(skills, domain=None):
    try:
        # Use a supported model
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Construct the prompt
        prompt = f"""
        Given these skills: {skills}
        {'In the domain of: ' + domain if domain else ''}

        Generate 3 unique project ideas. For each idea, include:
        1. Project Name
        2. Required Tools/Technologies
        3. Brief Description
        4. Difficulty Level (Beginner/Intermediate/Advanced)
        5. Estimated Time to Complete

        Format the output in a clear, structured way.
        """

        # Send prompt as plain text
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
