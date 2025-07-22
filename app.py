from flask import Flask, send_from_directory, request, jsonify, send_file, render_template_string
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_secret_key')

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'your-email@gmail.com')  # Your Gmail address
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', 'your-app-password')  # Your Gmail app password
RECIPIENT_EMAIL = 'nikuluhach.86209@gmail.com'  # Your email to receive messages

def send_email(name, email, subject, message):
    """Send email notification for contact form submission"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"Portfolio Contact: {subject}"
        
        # Email body
        body = f"""
        New contact form submission from your portfolio website!
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        
        Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

# Resume Maker HTML Template
RESUME_MAKER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Builder & Analyzer</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #2c3e50, #34495e);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        .content {
            padding: 30px;
        }
        
        .form-section {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 5px solid #667eea;
        }
        
        .form-section h3 {
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }
        
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 15px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: #2c3e50;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }
        
        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .form-group textarea {
            min-height: 100px;
            resize: vertical;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        }
        
        .btn-secondary {
            background: #6c757d;
            margin-left: 10px;
        }
        
        .resume-preview {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
        }
        
        .resume-preview h2 {
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .skill-tag {
            background: #e9ecef;
            padding: 5px 12px;
            border-radius: 15px;
            margin: 5px;
            display: inline-block;
            font-size: 0.9rem;
        }
        
        .back-btn {
            background: #6c757d;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-bottom: 20px;
            transition: background 0.3s ease;
        }
        
        .back-btn:hover {
            background: #5a6268;
            color: white;
        }
        
        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📝 Resume Builder & Analyzer</h1>
            <p>Create a professional resume in minutes</p>
        </div>
        
        <div class="content">
            <a href="/" class="back-btn">← Back to Portfolio</a>
            
            <form id="resumeForm">
                <div class="form-section">
                    <h3>👤 Personal Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="name">Full Name *</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email *</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="phone">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required>
                        </div>
                        <div class="form-group">
                            <label for="location">Location</label>
                            <input type="text" id="location" name="location">
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="linkedin">LinkedIn URL</label>
                            <input type="url" id="linkedin" name="linkedin">
                        </div>
                        <div class="form-group">
                            <label for="github">GitHub URL</label>
                            <input type="url" id="github" name="github">
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>📝 About Me</h3>
                    <div class="form-group">
                        <label for="about">Professional Summary</label>
                        <textarea id="about" name="about" placeholder="Write a brief summary about yourself, your career goals, and what makes you unique..."></textarea>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>🎓 Education</h3>
                    <div class="form-group">
                        <label for="education">Education Details</label>
                        <textarea id="education" name="education" placeholder="Example:&#10;B.Sc in Computer Science&#10;XYZ University&#10;2020-2024&#10;GPA: 3.8/4.0"></textarea>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>💼 Work Experience</h3>
                    <div class="form-group">
                        <label for="experience">Work Experience</label>
                        <textarea id="experience" name="experience" placeholder="Example:&#10;Software Engineer Intern&#10;ABC Corporation&#10;June 2023 - August 2023&#10;• Developed and maintained web applications&#10;• Collaborated with team members on project planning"></textarea>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>🛠️ Skills</h3>
                    <div class="form-group">
                        <label for="skills">Skills (one per line)</label>
                        <textarea id="skills" name="skills" placeholder="Example:&#10;Python&#10;JavaScript&#10;React&#10;Node.js&#10;Git&#10;Docker"></textarea>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>📌 Projects</h3>
                    <div class="form-group">
                        <label for="projects">Projects</label>
                        <textarea id="projects" name="projects" placeholder="Example:&#10;Portfolio Website&#10;• Built a responsive personal portfolio using React and Node.js&#10;• Implemented dark mode and animations&#10;• Deployed on AWS"></textarea>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 30px;">
                    <button type="submit" class="btn">Generate Resume</button>
                    <button type="button" class="btn btn-secondary" onclick="clearForm()">Clear Form</button>
                </div>
            </form>
            
            <div id="resumePreview" class="resume-preview" style="display: none;">
                <h2>Your Resume Preview</h2>
                <div id="previewContent"></div>
                <div style="text-align: center; margin-top: 20px;">
                    <button class="btn" onclick="downloadResume()">Download PDF</button>
                    <button class="btn btn-secondary" onclick="printResume()">Print Resume</button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('resumeForm').addEventListener('submit', function(e) {
            e.preventDefault();
            generateResume();
        });
        
        function generateResume() {
            const formData = new FormData(document.getElementById('resumeForm'));
            const data = Object.fromEntries(formData);
            
            // Validate required fields
            if (!data.name || !data.email || !data.phone) {
                alert('Please fill in all required fields (Name, Email, Phone)');
                return;
            }
            
            // Create resume preview
            const preview = document.getElementById('previewContent');
            preview.innerHTML = `
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="color: #2c3e50; font-size: 2.5rem; margin-bottom: 10px;">${data.name}</h1>
                    <p style="color: #666; font-size: 1.1rem;">
                        ${data.email} | ${data.phone}
                        ${data.location ? ' | ' + data.location : ''}
                    </p>
                    ${data.linkedin ? `<p><a href="${data.linkedin}" target="_blank">LinkedIn</a></p>` : ''}
                    ${data.github ? `<p><a href="${data.github}" target="_blank">GitHub</a></p>` : ''}
                </div>
                
                ${data.about ? `
                <div style="margin-bottom: 25px;">
                    <h3 style="color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px;">About Me</h3>
                    <p style="margin-top: 10px; line-height: 1.6;">${data.about.replace(/\\n/g, '<br>')}</p>
                </div>
                ` : ''}
                
                ${data.education ? `
                <div style="margin-bottom: 25px;">
                    <h3 style="color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px;">Education</h3>
                    <p style="margin-top: 10px; line-height: 1.6;">${data.education.replace(/\\n/g, '<br>')}</p>
                </div>
                ` : ''}
                
                ${data.experience ? `
                <div style="margin-bottom: 25px;">
                    <h3 style="color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px;">Work Experience</h3>
                    <p style="margin-top: 10px; line-height: 1.6;">${data.experience.replace(/\\n/g, '<br>')}</p>
                </div>
                ` : ''}
                
                ${data.skills ? `
                <div style="margin-bottom: 25px;">
                    <h3 style="color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px;">Skills</h3>
                    <div style="margin-top: 10px;">
                        ${data.skills.split('\\n').filter(skill => skill.trim()).map(skill => 
                            `<span class="skill-tag">${skill.trim()}</span>`
                        ).join('')}
                    </div>
                </div>
                ` : ''}
                
                ${data.projects ? `
                <div style="margin-bottom: 25px;">
                    <h3 style="color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px;">Projects</h3>
                    <p style="margin-top: 10px; line-height: 1.6;">${data.projects.replace(/\\n/g, '<br>')}</p>
                </div>
                ` : ''}
            `;
            
            document.getElementById('resumePreview').style.display = 'block';
            document.getElementById('resumePreview').scrollIntoView({ behavior: 'smooth' });
        }
        
        function clearForm() {
            document.getElementById('resumeForm').reset();
            document.getElementById('resumePreview').style.display = 'none';
        }
        
        function downloadResume() {
            // This would require a backend endpoint to generate PDF
            alert('PDF download feature will be implemented soon!');
        }
        
        function printResume() {
            window.print();
        }
    </script>
</body>
</html>
"""

# Serve static files (CSS, JS, images)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Serve project files
@app.route('/projects/<path:filename>')
def serve_project(filename):
    return send_from_directory('projects', filename)

# Serve CSS file
@app.route('/styles.css')
def serve_css():
    return send_file('styles.css', mimetype='text/css')

# Serve JavaScript file
@app.route('/script.js')
def serve_js():
    return send_file('script.js', mimetype='application/javascript')

# Main route - serve the portfolio
@app.route('/')
def home():
    return send_file('index.html')

# Resume Maker route
@app.route('/resume-maker')
def resume_maker():
    return render_template_string(RESUME_MAKER_HTML)

# API endpoint to list available projects
@app.route('/api/projects')
def list_projects():
    try:
        projects_dir = 'projects'
        if not os.path.exists(projects_dir):
            return jsonify({'projects': []})
        
        projects = []
        for item in os.listdir(projects_dir):
            item_path = os.path.join(projects_dir, item)
            if os.path.isdir(item_path):
                # It's a project folder
                projects.append({
                    'name': item,
                    'type': 'folder',
                    'path': f'/projects/{item}'
                })
            else:
                # It's a project file
                file_ext = os.path.splitext(item)[1].lower()
                projects.append({
                    'name': item,
                    'type': 'file',
                    'extension': file_ext,
                    'path': f'/projects/{item}'
                })
        
        return jsonify({'projects': projects})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint for contact form with email functionality
@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Validate required fields
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Send email notification
        email_sent = send_email(name, email, subject, message)
        
        if email_sent:
            print(f"Contact form submitted and email sent: {name}, {email}, {subject}")
            return jsonify({
                'success': True, 
                'message': 'Message sent successfully! I\'ll get back to you soon.'
            })
        else:
            print(f"Contact form submitted but email failed: {name}, {email}, {subject}")
            return jsonify({
                'success': False, 
                'message': 'Message received but there was an issue sending the notification. I\'ll check it manually.'
            }), 500
            
    except Exception as e:
        print(f"Contact form error: {e}")
        return jsonify({'success': False, 'message': 'Error processing your message. Please try again.'}), 500

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Portfolio server is running'})

if __name__ == '__main__':
    print("Starting Nikhil's Portfolio Server...")
    print("Open your browser and go to: http://localhost:5000")
    print("Projects folder created at: /projects")
    print("Resume Maker available at: /resume-maker")
    print(f"Contact form will send emails to: {RECIPIENT_EMAIL}")
    print("Note: Set SENDER_EMAIL and SENDER_PASSWORD in .env file for email functionality")
    app.run(debug=True, host='0.0.0.0', port=5000) 