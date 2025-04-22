from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import feedparser
import requests

app = FastAPI()

RSS_URL = "https://bair.berkeley.edu/blog/feed.xml"

def fetch_feed():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(RSS_URL, headers=headers)
    return feedparser.parse(response.content)

@app.get("/", response_class=HTMLResponse)
async def get_blogs():
    feed = fetch_feed()
    blogs = [{"title": entry.title, "link": entry.link, "summary": entry.summary} for entry in feed.entries]
    
    html_content = """
    <html>
        <head>
            <title>BAIR Blog</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
                h1 { color: #333; }
                li { margin-bottom: 20px; }
                a { text-decoration: none; font-weight: bold; color: #0066cc; }
                a:hover { text-decoration: underline; }
                .summary { color: #555; font-size: 0.9em; }
            </style>
        </head>
        <body>
            <h1>BAIR Blog Posts</h1>
            <ul>
    """
    for blog in blogs:
        html_content += f"<li><a href='{blog['link']}' target='_blank'>{blog['title']}</a><br><div class='summary'>{blog['summary']}</div></li>"
    
    html_content += "</ul></body></html>"
    return HTMLResponse(content=html_content)

@app.get("/blogs")
def read_blogs():
    feed = fetch_feed()
    blogs = [
        {
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("updated", "N/A")
        }
        for entry in feed.entries
    ]
    return blogs
