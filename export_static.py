import psycopg2
from psycopg2.extras import RealDictCursor
from jinja2 import Environment, FileSystemLoader
import os
import shutil

# Database credentials
DB_USER = 'postgres'
DB_PASS = 'IGOSDP2022'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'neoscona_db'

def export_site():
    print("🚀 Starting static export for GitHub Pages...")
    
    # 1. Connect to local database
    try:
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM posts ORDER BY created_at DESC')
        posts = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")
        return

    # 2. Setup Jinja2 Environment
    env = Environment(loader=FileSystemLoader('templates'))

    # 3. Render index.html (from neoscona.html)
    print("Rendering index.html...")
    index_template = env.get_template('neoscona.html')
    # index.html doesn't need posts but we pass empty just in case
    index_html = index_template.render(posts=[])
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # 4. Render blog.html
    print("Rendering blog.html with live posts...")
    blog_template = env.get_template('blog.html')
    blog_html = blog_template.render(posts=posts)
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_html)

    # 5. Create CNAME
    print("Creating CNAME file...")
    with open('CNAME', 'w') as f:
        f.write('neoscona.xyz')

    print("\n✅ Export Complete!")
    print("Files ready for GitHub Pages: index.html, blog.html, CNAME, static/")
    print("Note: Ensure your GitHub repository includes the 'static/' folder.")

if __name__ == '__main__':
    export_site()
