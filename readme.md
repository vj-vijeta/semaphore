```markdown
# Concurrent Access Control in Educational System

This code demonstrates how to implement concurrent access control using mutex and semaphore in an educational system. The system simulates students accessing assessment resources concurrently while teachers grade assessments. Mutex and semaphore are used to ensure exclusive access to grading resources and limit the number of students accessing assessment resources simultaneously.

## Code Structure

- `main.py`: Entry point of the program. Orchestrates the threads for students and teachers.
- `student.py`: Contains functions for simulating students accessing assessment resources.
- `teacher.py`: Contains functions for simulating teachers grading assessments.

## Usage

1. Run `main.py` to start the simulation.

## Sample Output

```
Student 0 is accessing the assessment resources
Student 1 is accessing the assessment resources
Teacher is grading assessment for student 0
Teacher is grading assessment for student 1
Student 2 is accessing the assessment resources
Student 3 is accessing the assessment resources
Teacher is grading assessment for student 2
Teacher is grading assessment for student 3
Student 4 is accessing the assessment resources
Student 5 is accessing the assessment resources
Teacher is grading assessment for student 4
Student 0 completed accessing assessment resources
Student 1 completed accessing assessment resources
Teacher completed grading assessment for student 0
Teacher completed grading assessment for student 1
Student 6 is accessing the assessment resources
Student 7 is accessing the assessment resources
...
```

## License

This code is licensed under the [MIT License](LICENSE).
```
#   s e m a p h o r e  
 