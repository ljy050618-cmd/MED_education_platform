import os
from nicegui import ui, app

from pages.home import register_home_page
from pages.class_page import register_class_page
from pages.genre_page import register_genre_page
from pages.missions_page import register_missions_page
from pages.quiz_page import register_quiz_page
from pages.quiz_paper_page import register_quiz_paper_page
from dotenv import load_dotenv 

app.add_static_files('/education_images', 'education_images')

register_home_page()
register_class_page()
register_genre_page()
register_missions_page()
register_quiz_page()
register_quiz_paper_page()
load_dotenv()

port = int(os.environ.get('PORT', 8080))
storage_secret = os.environ.get('STORAGE_SECRET', 'dev-secret-key-change-me')


ui.run(host='0.0.0.0', port=port, storage_secret=storage_secret,)