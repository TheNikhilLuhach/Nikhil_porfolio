import gradio as gr
from gemini_api import generate_project_ideas

class ChatState:
    def __init__(self):
        self.user_name = None
        self.last_topic = None

state = ChatState()

def extract_name(message):
    """Extract name from message if present."""
    name_keywords = ["my name is", "i am", "i'm", "this is"]
    message_lower = message.lower()
    
    for keyword in name_keywords:
        if keyword in message_lower:
            # Get the part after the keyword
            name_part = message_lower.split(keyword)[1].strip()
            # Take the first word as the name
            name = name_part.split()[0].capitalize()
            return name
    return None

def process_input(message, history):
    """
    Process user input and generate project ideas in a chat format.
    
    Args:
        message (str): User's message
        history (list): Chat history
    
    Returns:
        tuple: (response, updated_history)
    """
    # Convert message to lowercase for easier matching
    message_lower = message.lower()
    
    # Check for name introduction
    name = extract_name(message)
    if name:
        state.user_name = name
        return f"Nice to meet you, {name}! I'm your Tech2Idea assistant. I can help you generate project ideas based on your skills and technologies. What would you like to explore today?", history + [[message, f"Nice to meet you, {name}! I'm your Tech2Idea assistant. I can help you generate project ideas based on your skills and technologies. What would you like to explore today?"]]
    
    # Check for greetings
    greetings = ["hi", "hello", "hey", "greetings", "howdy"]
    if any(greeting in message_lower for greeting in greetings):
        if state.user_name:
            return f"Hello again, {state.user_name}! How can I help you with project ideas today?", history + [[message, f"Hello again, {state.user_name}! How can I help you with project ideas today?"]]
        else:
            return "Hello! I'm your Tech2Idea assistant. I can help you generate project ideas based on your skills and technologies. What's your name?", history + [[message, "Hello! I'm your Tech2Idea assistant. I can help you generate project ideas based on your skills and technologies. What's your name?"]]
    
    # Check for help requests
    help_keywords = ["help", "what can you do", "how does this work", "explain"]
    if any(keyword in message_lower for keyword in help_keywords):
        help_response = f"""I can help you with:
1. Generating project ideas based on your skills
2. Suggesting technologies for specific domains
3. Providing guidance on project development

Just tell me about your skills or what kind of project you're interested in, and I'll help you get started!"""
        if state.user_name:
            help_response = f"Hi {state.user_name}!\n" + help_response
        return help_response, history + [[message, help_response]]
    
    # Check if the message contains any of the expected keywords
    valid_keywords = ["skills", "technology", "project", "idea", "generate", "build", "create", "develop"]
    if not any(keyword in message_lower for keyword in valid_keywords):
        response = "I'm here to help you with project ideas and technology suggestions! I can assist you with:\n- Generating project ideas based on your skills\n- Suggesting technologies for specific domains\n- Providing guidance on project development\n\nWhat would you like to explore?"
        if state.user_name:
            response = f"Hi {state.user_name}!\n" + response
        return response, history + [[message, response]]
    
    # Extract skills from the message
    skills = message.strip()
    
    # Generate project ideas
    response = generate_project_ideas(skills, None)
    
    # Add personalization to the response
    if state.user_name:
        response = f"Here are some project ideas for you, {state.user_name}:\n\n" + response
    
    return response, history + [[message, response]]

# Create the Gradio interface
with gr.Blocks(title="Tech2Idea Chatbot", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🤖 Tech2Idea Chatbot
    Chat with me to transform your technical skills into unique project ideas!
    
    Just tell me about your skills and technologies, and I'll help you generate project ideas.
    """)
    
    chatbot = gr.Chatbot(
        label="Chat",
        height=600,
        show_copy_button=True
    )
    
    with gr.Row():
        msg = gr.Textbox(
            label="Your Message",
            placeholder="Tell me about your skills and technologies...",
            lines=2,
            scale=8
        )
        submit = gr.Button("Send", variant="primary", scale=1)
    
    submit.click(
        fn=process_input,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    ).then(
        lambda: "", None, msg
    )
    
    msg.submit(
        fn=process_input,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    ).then(
        lambda: "", None, msg
    )

if __name__ == "__main__":
    demo.launch() 
