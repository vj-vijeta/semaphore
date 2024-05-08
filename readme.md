
# Educational Technology Concurrency Control

This project simulates a scenario in educational technology where students access assessment resources concurrently, and teachers grade assessments using concurrency control mechanisms such as mutex and semaphore.

## Code Structure

The project consists of three Python files:

1. `main.py`: This script serves as the entry point of the program. It orchestrates the threads for students accessing assessment resources and teachers grading assessments.

2. `student.py`: This module contains the function `access_assessment_resources`, which simulates a student accessing assessment resources. It uses a semaphore to control access to the resources.

3. `teacher.py`: This module contains the function `grade_assessment`, which simulates a teacher grading an assessment. It uses a mutex to control access to the grading resources.

## Usage

To run the code:

1. Ensure you have Python installed on your system (version 3.x recommended).

2. Clone this repository to your local machine or download the files.

3. Open a terminal or command prompt and navigate to the directory containing the code files.

4. Run the following command to execute the program:

   ```
   python main.py
   ```

## Sample Output

```
Student 0 is accessing the assessment resources
Student 1 is accessing the assessment resources
Student 2 is accessing the assessment resources
Student 3 is accessing the assessment resources
Student 4 is accessing the assessment resources
Student 5 is accessing the assessment resources
Student 6 is accessing the assessment resources
Student 7 is accessing the assessment resources
Student 8 is accessing the assessment resources
Student 9 is accessing the assessment resources
Student 3 completed accessing assessment resources
Student 4 completed accessing assessment resources
Student 0 completed accessing assessment resources
Teacher is grading assessment for student 0
Student 5 completed accessing assessment resources
Student 1 completed accessing assessment resources
Student 2 completed accessing assessment resources
Teacher completed grading assessment for student 0
Teacher is grading assessment for student 1
Teacher completed grading assessment for student 1
Teacher is grading assessment for student 2
Teacher completed grading assessment for student 2
Student 6 completed accessing assessment resources
Teacher is grading assessment for student 3
Student 7 completed accessing assessment resources
Student 8 completed accessing assessment resources
Teacher completed grading assessment for student 3
Teacher is grading assessment for student 4
Teacher completed grading assessment for student 4
Student 9 completed accessing assessment resources
Teacher is grading assessment for student 5
Teacher completed grading assessment for student 5
Teacher is grading assessment for student 6
Teacher completed grading assessment for student 6
Teacher is grading assessment for student 7
Teacher completed grading assessment for student 7
Teacher is grading assessment for student 8
Teacher completed grading assessment for student 8
Teacher is grading assessment for student 9
Teacher completed grading assessment for student 9
```

This output demonstrates students accessing assessment resources concurrently and teachers grading assessments in a controlled manner using mutex and semaphore.



