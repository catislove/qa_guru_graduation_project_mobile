import allure
from allure_commons.types import Severity

from mobile.models.wikipedia_app import Wikipedia


@allure.feature('Тесты для приложения википедии')
@allure.label('owner', 'Amalia')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем наличие руководства после установки')
def test_tutorial_shown_and_functional_after_installation():
    application = Wikipedia()
    application.verify_tutorial_presented()
    application.interact_and_complete_tutorial()


@allure.feature('Тесты для приложения википедии')
@allure.label('owner', 'Amalia')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Пропускаем руководство')
def test_skip_tutorial():
    application = Wikipedia()
    application.skip_tutorial()
    application.verify_tutorial_not_presented()


@allure.feature('Тесты для приложения википедии')
@allure.label('owner', 'Amalia')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Поиск статьи по названию')
def test_search_article_by_title():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_article('Appium')
    application.verify_article_title_in_list('Appium')


@allure.feature('Тесты для приложения википедии')
@allure.label('owner', 'Amalia')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие первой статьи')
def test_open_found_article():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_article('Python lang')
    application.verify_article_title_in_list('Python (programming language)')
    application.open_article_in_search_results_having_order_n(0)
    application.verify_phrase_exists_in_article('the designer of python, Guido van Rossum')
