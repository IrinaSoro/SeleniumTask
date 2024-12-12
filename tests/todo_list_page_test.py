import allure
from pages.todo_list_page import TodoListPage

@allure.suite('Todo list')
class TestTodoListPage:

    @allure.title('10 - Check todo list updated')
    def test_todo_list_update(self, driver):
        todo_list_page = TodoListPage(driver, "https://webdriveruniversity.com/To-Do-List/index.html")
        todo_list_page.open()
        items_count = todo_list_page.update_todo_list_items()
        assert items_count == 4, 'The item has not been deleted'