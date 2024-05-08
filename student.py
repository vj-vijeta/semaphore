import threading
import time

def access_assessment_resources(student_id, semaphore):
    """
    Simulates a student accessing assessment resources.
    Args:
        student_id (int): The ID of the student.
        semaphore (Semaphore): Semaphore for controlling access to assessment resources.
    """
    try:
        with semaphore:
            print(f"Student {student_id} is accessing the assessment resources")
            # Simulating accessing assessment resources
            time.sleep(2)
            print(f"Student {student_id} completed accessing assessment resources")
    except Exception as e:
        print(f"Error occurred for student {student_id}: {e}")
