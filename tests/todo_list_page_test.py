import allure
from pages.todo_list_page import TodoListPage

@allure.suite('Todo list')
class TestTodoListPage:

    URL = "/To-Do-List/index.html"

    @allure.title('10 - Check todo list updated')
    def test_todo_list_update(self, driver):
        todo_list_page = TodoListPage(driver, self.URL)
        items_count = todo_list_page.get_updated_todo_list_items()
        assert items_count == 4, 'The item has not been deleted'