import gradio as gr
from voice_menu import VoiceMenu

menu = VoiceMenu()

def gradio_interface(text_command, audio_command, log_password):
    if text_command and text_command.strip():
        command = text_command.strip()
    elif audio_command is not None:
        command = menu.transcribe_audio_file(audio_command)
        if not command:
            return "Could not understand audio. Please try again."
    else:
        return "Please enter or speak a command."
    if menu.match_command(command) == "help":
        return '\n'.join([f"{i+1}. {k.replace('_',' ')}: {menu.commands[k][1]}" for i, k in enumerate(menu.command_keys)])
    return menu.run_command(command, log_password=log_password)

def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("""
        # Voice Menu Assistant
        **Available Commands:**
        <pre>""" + '\n'.join([f"{i+1}. {k.replace('_',' ')}: {menu.commands[k][1]}" for i, k in enumerate(menu.command_keys)]) + "</pre>\nType a command, number, or use your voice. For logs, use password: <b>password</b>.""")
        with gr.Row():
            text_input = gr.Textbox(label="Type your command here", placeholder="e.g. 1, open notepad, log, help")
            audio_input = gr.Audio(type="filepath", label="Or speak your command")
        log_password = gr.Textbox(label="Log Password (for 'log' command)", type="password")
        output = gr.Textbox(label="Assistant Output")
        submit_btn = gr.Button("Submit")
        submit_btn.click(gradio_interface, inputs=[text_input, audio_input, log_password], outputs=output)
    return demo

demo = build_ui()

if __name__ == "__main__":
    demo.launch() 