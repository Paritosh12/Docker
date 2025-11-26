from app import add_task, list_tasks

def test_add_task():
    add_task("Test item")
    assert "Test item" in list_tasks()
