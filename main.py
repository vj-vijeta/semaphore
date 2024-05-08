import threading
import student
import teacher

def main():
    """
    Entry point of the program.
    """
    try:
        num_assessment_resources = 3  # Number of available assessment resources
        assessment_semaphore = threading.Semaphore(num_assessment_resources)

        num_students = 10  # Number of students
        for i in range(num_students):
            t = threading.Thread(target=student.access_assessment_resources, args=(i, assessment_semaphore))
            t.start()

        grading_mutex = threading.Lock()

        num_teachers = 5  # Number of teachers
        for i in range(num_teachers):
            t = threading.Thread(target=teacher.grade_assessment, args=(i, grading_mutex))
            t.start()
        
        # Wait for all threads to complete
        main_thread = threading.current_thread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
