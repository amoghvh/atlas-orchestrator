from .celery_app import celery_app
import time

@celery_app.task(name="atlas.long_task", bind=True)
def long_task(self, seconds: int = 10):
    for i in range(seconds):
        time.sleep(1)
        self.update_state(
            state='PROGRESS',
            meta={
                'current': i + 1,
                'total': seconds,
                'percent': int((i + 1) / seconds * 100)
            }
        )
    return f"✅ Task completed after {seconds} seconds!"
