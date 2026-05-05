from flask import Flask, render_template_string
import requests

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Quote of the Day</title>
  <style>
    body { background: #0d1117; color: #cdd6f4; font-family: monospace;
           display: flex; align-items: center; justify-content: center;
           min-height: 100vh; margin: 0; flex-direction: column; gap: 24px; }
    .card { background: #1e1e2e; border: 1px solid #313244; border-radius: 12px;
            padding: 40px; max-width: 600px; text-align: center; }
    .quote { font-size: 1.3rem; line-height: 1.7; color: #cba6f7; }
    .author { margin-top: 16px; color: #6c7086; font-size: 0.9rem; }
    a { color: #89b4fa; text-decoration: none; font-size: 0.85rem;
        border: 1px solid #313244; padding: 8px 20px; border-radius: 6px; }
    a:hover { background: #313244; }
  </style>
</head>
<body>
  <div class="card">
    <div class="quote">"{{ quote }}"</div>
    <div class="author">— {{ author }}</div>
  </div>
  <a href="/">new quote</a>
</body>
</html>
"""

@app.route("/")
def index():
    try:
        res = requests.get("https://zenquotes.io/api/random", timeout=5)
        data = res.json()[0]
        quote = data["q"]
        author = data["a"]
    except Exception:
        quote = "When in doubt, reboot."
        author = "Every sysadmin ever"
    return render_template_string(TEMPLATE, quote=quote, author=author)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
