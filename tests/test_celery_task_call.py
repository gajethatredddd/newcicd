from app.tasks.celery_tasks import send_email_task

def test_send_email_task_signature():
    assert hasattr(send_email_task, "delay")
