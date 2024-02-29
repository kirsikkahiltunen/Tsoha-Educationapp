CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    course_name TEXT,
    teacher_id INT REFERENCES users(id),
    course_description TEXT
);

CREATE TABLE course_enrollments(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    course_id INT REFERENCES courses(id)
);

CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    task_name TEXT,
    course_id INT REFERENCES courses(id)
    task_total INT
);

CREATE TABLE completed_tasks(
    course_id INT REFERENCES courses(id),
    task_id INT REFERENCES tasks(id),
    student_id INT REFERENCES users(id)
);