import re
from playwright.sync_api import Page, expect

URL = "https://demo.playwright.dev/todomvc"
PLACEHOLDER = "What needs to be done?"


def test_add_todo(page: Page):
    """TC-1: 할 일을 추가하면 목록에 나타난다"""
    page.goto(URL)
    page.get_by_placeholder(PLACEHOLDER).fill("Playwright 과제 하기")
    page.get_by_placeholder(PLACEHOLDER).press("Enter")
    expect(page.locator(".todo-list li")).to_have_text("Playwright 과제 하기")


def test_complete_todo(page: Page):
    """TC-2: 할 일을 체크하면 완료 상태가 된다"""
    page.goto(URL)
    page.get_by_placeholder(PLACEHOLDER).fill("GitHub에 올리기")
    page.get_by_placeholder(PLACEHOLDER).press("Enter")
    page.locator(".todo-list li .toggle").click()
    expect(page.locator(".todo-list li")).to_have_class(re.compile("completed"))


def test_todo_count(page: Page):
    """TC-3: 할 일 3개를 추가하면 개수가 3으로 표시된다"""
    page.goto(URL)
    for task in ["첫 번째", "두 번째", "세 번째"]:
        page.get_by_placeholder(PLACEHOLDER).fill(task)
        page.get_by_placeholder(PLACEHOLDER).press("Enter")
    expect(page.locator(".todo-list li")).to_have_count(3)
    expect(page.locator(".todo-count")).to_contain_text("3")