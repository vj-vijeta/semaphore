import threading
import time

def grade_assessment(student_id, mutex):
    """
    Simulates a teacher grading an assessment.
    Args:
        student_id (int): The ID of the student whose assessment is being graded.
        mutex (Lock): Mutex for controlling access to grading resources.
    """
    try:
        with mutex:
            print(f"Teacher is grading assessment for student {student_id}")
            # Simulating grading assessment
            time.sleep(1)
            print(f"Teacher completed grading assessment for student {student_id}")
    except Exception as e:
        print(f"Error occurred during grading for student {student_id}: {e}")
