from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class Wikipedia:

    def verify_tutorial_presented(self):
        with step('Проверяем налиичия руководства при первом запуске'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.absent)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).should(be.present)

    def interact_and_complete_tutorial(self):
        with step('Проверяем заголовок первой страницы'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('The Free Encyclopedia'))
        with step('Нажимаем "продолжить"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        with step('Проверяем заголовок второй страницы'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('New ways to explore'))
        with step('Нажимаем "продолжить"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        with step('Проверяем заголовок третьей страницы'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Reading lists with sync'))
        with step('Нажимаем "продолжить"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        with step('Проверяем заголовок четвертой страницы'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Send anonymous data'))
        with step('Проверяем наличие параметров «Принять» или «Отклонить»'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/rejectButton')).should(be.present)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).should(be.present)
        with step('Нажимаем "Принять"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()
        with step('Проверяем, что есть строка для поиска'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.present)

    def skip_tutorial(self):
        with step('Пропускаем руководство'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    def verify_tutorial_not_presented(self):
        with step('Проверяем, что руководство закрыто'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(be.absent)
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.present)

    def search_article(self, text):
        with step('Кликаем на поиск'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

    def verify_article_title_in_list(self, text):
        with step('Проверяем, что поиск выполнен'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(text))

    def open_article_in_search_results_having_order_n(self, n):
        with step('Нажимаем на первую найденную статью'):
            browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[n].click()

    def verify_phrase_exists_in_article(self, text):
        with step('Нажимаем "Найти в статье"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_find_in_article')).click()
        with step('Вводим текст и проверяем одно совпадение'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/find_in_page_match')).should(have.text('1/1'))
