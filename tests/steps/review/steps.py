from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.film.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def get_film(film_id):
        a.get(f'{PROJECT_URL}film?filmID={film_id}')

    @staticmethod
    def enter_review_text(title, text):
        Pages.set_review_title(title)
        Pages.set_review_body(text)

    @staticmethod
    def submit_review():
        Pages.submit_review()