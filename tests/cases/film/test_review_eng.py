from time import sleep

from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestReviewENG:
    def test(self):
        title = "testreview1review"
        body = "testtestetstesttestest"

        #TODO: Auth.simpleAuth()

        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        Film.create_review(title, body)
        Film.check_review(title, body)

        #TODO: logout




        