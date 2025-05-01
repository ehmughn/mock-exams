#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

#define NUM_QUESTIONS 80
#define MAX_STR 512
#define MAX_CHOICES 4

// Structure to hold quiz question data
typedef struct {
    char section[MAX_STR];
    char question[MAX_STR];
    char choices[MAX_CHOICES][MAX_STR];
    char correct;
    char reasoning[MAX_STR];
} Question;

// Quiz data
Question quiz[NUM_QUESTIONS] = {
    // Section 1: Entity Relationship Diagrams (ERD) Basics (10 questions)
    {
        "ERD Basics",
        "What is an Entity Relationship Diagram (ERD)?",
        {"a. A programming language", "b. A graphical representation of relationships in an IT system", "c. A type of database", "d. A data analysis tool"},
        'b',
        "An ERD is a graphical representation depicting relationships among entities in an IT system (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "The primary purpose of an ERD is to:",
        {"a. Execute SQL queries", "b. Model and design relational databases", "c. Optimize database performance", "d. Store data directly"},
        'b',
        "ERDs are used to model and design relational databases in terms of logic and business rules (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "True or False: An ERD serves as a reference point only during database design.",
        {"a. True", "b. False", "c. Only for logical models", "d. Only for physical models"},
        'b',
        "An ERD can serve as a reference point after database rollout for debugging or re-engineering (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "Which of the following is NOT a type of ERD data model?",
        {"a. Conceptual", "b. Logical", "c. Physical", "d. Operational"},
        'd',
        "The reviewer lists conceptual, logical, and physical data models, but not operational (page 1)."
    },
    {
        "ERD Basics",
        "A conceptual data model provides:",
        {"a. Detailed attributes", "b. A high-level overview of data relationships", "c. A blueprint for a relational database", "d. Specific technology details"},
        'b',
        "A conceptual data model lacks specific details but provides an overview of project scope and data relationships (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "Which data model must be based on a logical data model?",
        {"a. Conceptual", "b. Physical", "c. Relational", "d. Hierarchical"},
        'b',
        "A physical data model is based on a logical data model (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "All of the following are benefits of ERDs EXCEPT:",
        {"a. Visualizing database design", "b. Determining system requirements", "c. Executing database queries", "d. Aiding in debugging"},
        'c',
        "ERDs help with design, requirements, and debugging, but not query execution (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "An ERD is a foundation for:",
        {"a. A relational database", "b. A programming framework", "c. A network architecture", "d. A user interface"},
        'a',
        "ERDs serve as the foundation for a relational database (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "A logical data model includes:",
        {"a. Technology-specific details", "b. Specific attributes and relationships", "c. Only high-level relationships", "d. Hardware specifications"},
        'b',
        "A logical data model illustrates specific attributes and relationships (reviewer, page 1)."
    },
    {
        "ERD Basics",
        "The importance of an ERD includes helping to:",
        {"a. Write SQL code", "b. Define business processes", "c. Manage network traffic", "d. Develop applications"},
        'b',
        "ERDs help define business processes (reviewer, page 1)."
    },
    // Section 2: ERD Components (10 questions)
    {
        "ERD Components",
        "Entities in an ERD represent:",
        {"a. Relationships between tables", "b. Objects or concepts with stored data", "c. Database queries", "d. Constraints"},
        'b',
        "Entities are objects or concepts that can have data stored about them (reviewer, page 1)."
    },
    {
        "ERD Components",
        "Which of the following is an example of an entity in a School database?",
        {"a. Teacher_Name", "b. Course", "c. Student_Age", "d. Primary_Key"},
        'b',
        "Course is a concept entity; others are attributes or keys (reviewer, page 1)."
    },
    {
        "ERD Components",
        "A weak entity is characterized by:",
        {"a. Having a primary key", "b. Dependence on a parent entity", "c. Independence from other entities", "d. Multiple primary keys"},
        'b',
        "Weak entities lack a primary key and depend on a parent entity (reviewer, page 1)."
    },
    {
        "ERD Components",
        "True or False: A strong entity does not depend on any other entity.",
        {"a. True", "b. False", "c. Only for weak entities", "d. Only for relationships"},
        'a',
        "A strong entity has a primary key and is independent (reviewer, page 1)."
    },
    {
        "ERD Components",
        "An attribute in an ERD is:",
        {"a. A table in the database", "b. A property of an entity", "c. A relationship between entities", "d. A primary key only"},
        'b',
        "Attributes are properties or characteristics of entities (reviewer, page 1)."
    },
    {
        "ERD Components",
        "Which attribute can have multiple values for a single entity?",
        {"a. Primary key", "b. Multivalued attribute", "c. Composite attribute", "d. Derived attribute"},
        'b',
        "A multivalued attribute can have multiple values for one entity (reviewer, page 1)."
    },
    {
        "ERD Components",
        "A composite attribute is one that:",
        {"a. Has multiple values", "b. Is derived from another attribute", "c. Consists of two or more attributes", "d. Is a primary key"},
        'c',
        "A composite attribute comprises two or more other attributes (reviewer, page 1)."
    },
    {
        "ERD Components",
        "A derived attribute's value is calculated from:",
        {"a. Another attribute", "b. A primary key", "c. A foreign key", "d. A relationship"},
        'a',
        "Derived attributes are calculated from another attribute (reviewer, page 1)."
    },
    {
        "ERD Components",
        "Relationships in an ERD are represented by:",
        {"a. Rectangles", "b. Diamond-shaped boxes", "c. Circles", "d. Lines"},
        'b',
        "Relationships are shown as diamond-shaped boxes (reviewer, page 1)."
    },
    {
        "ERD Components",
        "All of the following are attributes EXCEPT:",
        {"a. Teacher_Name", "b. Course", "c. Student_Age", "d. Teacher_Address"},
        'b',
        "Course is an entity, not an attribute (reviewer, page 1)."
    },
    // Section 3: Participation Constraints (8 questions)
    {
        "Participation Constraints",
        "Total participation in an ERD is indicated by:",
        {"a. Single lines", "b. Double lines", "c. Dashed lines", "d. No lines"},
        'b',
        "Total participation is represented by double lines (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "Partial participation means:",
        {"a. All entities are involved", "b. Not all entities are involved", "c. No entities are involved", "d. Only weak entities are involved"},
        'b',
        "Partial participation is represented by single lines, indicating not all entities participate (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "True or False: Total participation requires every entity to be involved in a relationship.",
        {"a. True", "b. False", "c. Only for strong entities", "d. Only for weak entities"},
        'a',
        "Total participation means each entity is involved in the relationship (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "Which of the following indicates partial participation?",
        {"a. Double lines", "b. Single lines", "c. Dotted lines", "d. Diamond shapes"},
        'b',
        "Partial participation is shown with single lines (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "In a School database, if every Student must enroll in a Course, this is:",
        {"a. Partial participation", "b. Total participation", "c. No participation", "d. Weak participation"},
        'b',
        "Requiring every entity (Student) to participate indicates total participation (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "If some Teachers are not assigned to Courses, this is:",
        {"a. Total participation", "b. Partial participation", "c. Strong participation", "d. Derived participation"},
        'b',
        "Not all entities (Teachers) participating indicates partial participation (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "All of the following describe participation constraints EXCEPT:",
        {"a. Total participation", "b. Partial participation", "c. Primary key", "d. Entity involvement"},
        'c',
        "Primary key is not a participation constraint (reviewer, page 2)."
    },
    {
        "Participation Constraints",
        "The difference between total and partial participation is:",
        {"a. Line style in ERD", "b. Entity type", "c. Attribute type", "d. Key type"},
        'a',
        "Total participation uses double lines, partial uses single lines (reviewer, page 2)."
    },
    // Section 4: MySQL Constraints Basics (10 questions)
    {
        "MySQL Constraints Basics",
        "MySQL constraints are used to:",
        {"a. Optimize queries", "b. Ensure data integrity", "c. Create indexes", "d. Manage users"},
        'b',
        "Constraints ensure data integrity, accuracy, and consistency (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "When are constraints typically applied?",
        {"a. During query execution", "b. During table creation or alteration", "c. During data retrieval", "d. During backup"},
        'b',
        "Constraints are used during table creation or alteration (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "True or False: Constraints prevent invalid data entry.",
        {"a. True", "b. False", "c. Only for NOT NULL", "d. Only for PRIMARY KEY"},
        'a',
        "Constraints help prevent invalid data entry into the database (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "Which constraint ensures a column cannot have NULL values?",
        {"a. UNIQUE", "b. NOT NULL", "c. FOREIGN KEY", "d. CHECK"},
        'b',
        "NOT NULL prevents a column from accepting NULL values (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "The UNIQUE constraint ensures:",
        {"a. No NULL values", "b. All values are different", "c. Referential integrity", "d. Specific conditions"},
        'b',
        "UNIQUE ensures all values in a column are distinct (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "Which constraint combines NOT NULL and UNIQUE?",
        {"a. FOREIGN KEY", "b. CHECK", "c. PRIMARY KEY", "d. DEFAULT"},
        'c',
        "PRIMARY KEY combines NOT NULL and UNIQUE (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "All of the following are MySQL constraints EXCEPT:",
        {"a. NOT NULL", "b. UNIQUE", "c. INDEX", "d. FOREIGN KEY"},
        'c',
        "INDEX is not a constraint; it’s used for performance (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "Constraints enforce:",
        {"a. Business rules", "b. Query optimization", "c. User authentication", "d. Data compression"},
        'a',
        "Constraints enforce business rules at the database level (reviewer, page 3)."
    },
    {
        "MySQL Constraints Basics",
        "The purpose of constraints includes:",
        {"a. Speeding up queries", "b. Ensuring data accuracy", "c. Creating tables", "d. Managing backups"},
        'b',
        "Constraints ensure data accuracy and consistency (reviewer, page 2)."
    },
    {
        "MySQL Constraints Basics",
        "Which statement is true about constraints?",
        {"a. They are optional", "b. They are only for queries", "c. They are applied after data entry", "d. They are for indexing only"},
        'a',
        "Constraints are optional but recommended for data integrity (reviewer, page 2)."
    },
    // Section 5: Specific MySQL Constraints (10 questions)
    {
        "Specific MySQL Constraints",
        "The FOREIGN KEY constraint ensures:",
        {"a. Unique values", "b. Referential integrity", "c. No NULL values", "d. Specific conditions"},
        'b',
        "FOREIGN KEY ensures referential integrity between tables (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "The CHECK constraint is used to:",
        {"a. Prevent NULL values", "b. Ensure unique values", "c. Meet specific conditions", "d. Link tables"},
        'c',
        "CHECK ensures values meet specific criteria (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "True or False: CHECK constraint is supported in all MySQL versions.",
        {"a. True", "b. False", "c. Only for MySQL 5.7", "d. Only for MySQL 8.0+"},
        'b',
        "CHECK is supported in MySQL 8.0 and later (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "The DEFAULT constraint provides:",
        {"a. A unique value", "b. A default value when none is specified", "c. Referential integrity", "d. A primary key"},
        'b',
        "DEFAULT assigns a default value when none is provided (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "Which constraint is typically applied to an 'id' column?",
        {"a. NOT NULL", "b. UNIQUE", "c. PRIMARY KEY", "d. CHECK"},
        'c',
        "PRIMARY KEY is usually applied to 'id' columns (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "An example of a NOT NULL constraint is:",
        {"a. email VARCHAR(100) UNIQUE", "b. username VARCHAR(50) NOT NULL", "c. age INT CHECK (age >= 18)", "d. status VARCHAR(10) DEFAULT 'active'"},
        'b',
        "username VARCHAR(50) NOT NULL prevents NULL values (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "The FOREIGN KEY constraint links to:",
        {"a. A UNIQUE column", "b. A PRIMARY KEY in another table", "c. A NOT NULL column", "d. A CHECK column"},
        'b',
        "FOREIGN KEY references a PRIMARY KEY in another table (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "All of the following are true for DEFAULT constraint EXCEPT:",
        {"a. Provides a default value", "b. Useful for timestamps", "c. Ensures unique values", "d. Used when no value is specified"},
        'c',
        "DEFAULT does not ensure unique values; it provides a default (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "The CHECK constraint example 'age INT CHECK (age >= 18)' ensures:",
        {"a. Age is unique", "b. Age is not NULL", "c. Age is at least 18", "d. Age is a default value"},
        'c',
        "CHECK ensures age meets the condition (age >= 18) (reviewer, page 2)."
    },
    {
        "Specific MySQL Constraints",
        "Which constraint can be added using ALTER TABLE?",
        {"a. NOT NULL", "b. UNIQUE", "c. CHECK", "d. All of the above"},
        'd',
        "ALTER TABLE can add NOT NULL, UNIQUE, CHECK, and other constraints (reviewer, page 3)."
    },
    // Section 6: Modifying Tables with Constraints (8 questions)
    {
        "Modifying Tables with Constraints",
        "The ALTER TABLE statement is used to:",
        {"a. Create new tables", "b. Add or remove constraints", "c. Execute queries", "d. Backup data"},
        'b',
        "ALTER TABLE adds or removes constraints (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "Which command adds a UNIQUE constraint to an existing table?",
        {"a. ALTER TABLE users ADD CONSTRAINT UNIQUE (email)", "b. CREATE TABLE users (email UNIQUE)", "c. MODIFY TABLE users UNIQUE", "d. ADD UNIQUE TO users"},
        'a',
        "ALTER TABLE users ADD CONSTRAINT UNIQUE (email) adds a UNIQUE constraint (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "True or False: Constraints can only be added during table creation.",
        {"a. True", "b. False", "c. Only for PRIMARY KEY", "d. Only for FOREIGN KEY"},
        'b',
        "Constraints can be added using ALTER TABLE after table creation (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "The command 'ALTER TABLE users MODIFY name VARCHAR(100) NOT NULL' does what?",
        {"a. Adds a UNIQUE constraint", "b. Adds a NOT NULL constraint", "c. Changes the table name", "d. Deletes the column"},
        'b',
        "It modifies the 'name' column to be NOT NULL (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "All of the following can be done with ALTER TABLE EXCEPT:",
        {"a. Add constraints", "b. Remove constraints", "c. Create a new database", "d. Modify column constraints"},
        'c',
        "ALTER TABLE does not create databases (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "To enforce business rules after table creation, use:",
        {"a. CREATE TABLE", "b. ALTER TABLE", "c. SELECT", "d. INSERT"},
        'b',
        "ALTER TABLE adds constraints to enforce business rules (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "Which is a best practice for constraints?",
        {"a. Avoid PRIMARY and FOREIGN KEYS", "b. Define PRIMARY and FOREIGN KEYS", "c. Use constraints without indexing", "d. Apply constraints after data entry"},
        'b',
        "Always define PRIMARY and FOREIGN KEYS for relational integrity (reviewer, page 3)."
    },
    {
        "Modifying Tables with Constraints",
        "Combining constraints with indexing improves:",
        {"a. Data entry speed", "b. Database performance", "c. Table creation time", "d. Query complexity"},
        'b',
        "Constraints with indexing improve performance (reviewer, page 3)."
    },
    // Section 7: MySQL JOIN Basics (10 questions)
    {
        "MySQL JOIN Basics",
        "JOIN statements in MySQL are used to:",
        {"a. Create tables", "b. Combine rows from multiple tables", "c. Delete records", "d. Update constraints"},
        'b',
        "JOINs combine rows from two or more tables based on a related column (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "JOINs are useful when data is:",
        {"a. Stored in a single table", "b. Normalized across multiple tables", "c. Not relational", "d. Backed up"},
        'b',
        "JOINs are useful for normalized data stored across multiple tables (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "True or False: JOINs require a related column between tables.",
        {"a. True", "b. False", "c. Only for INNER JOIN", "d. Only for OUTER JOIN"},
        'a',
        "JOINs are based on a related column between tables (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "Which JOIN returns rows with matches in both tables?",
        {"a. LEFT JOIN", "b. RIGHT JOIN", "c. INNER JOIN", "d. CROSS JOIN"},
        'c',
        "INNER JOIN returns rows where the join condition is met in both tables (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "All of the following are types of JOINs EXCEPT:",
        {"a. INNER JOIN", "b. LEFT JOIN", "c. RIGHT JOIN", "d. TOP JOIN"},
        'd',
        "TOP JOIN is not a MySQL JOIN type (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "The purpose of a JOIN is to:",
        {"a. Delete data", "b. Retrieve meaningful information", "c. Create constraints", "d. Optimize indexes"},
        'b',
        "JOINs retrieve meaningful information through relationships (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "Which JOIN is based on a condition like table1.column = table2.column?",
        {"a. CROSS JOIN", "b. INNER JOIN", "c. SELF JOIN", "d. All of the above"},
        'b',
        "INNER JOIN uses a condition like table1.column = table2.column (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "JOINs help retrieve data from:",
        {"a. A single table", "b. Multiple related tables", "c. Non-relational databases", "d. External files"},
        'b',
        "JOINs combine data from multiple related tables (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "The syntax 'SELECT columns FROM table1 INNER JOIN table2 ON condition' is for:",
        {"a. LEFT JOIN", "b. RIGHT JOIN", "c. INNER JOIN", "d. CROSS JOIN"},
        'c',
        "This syntax defines an INNER JOIN (reviewer, page 3)."
    },
    {
        "MySQL JOIN Basics",
        "JOINs are essential for:",
        {"a. Data normalization", "b. Data retrieval from normalized tables", "c. Data compression", "d. Data encryption"},
        'b',
        "JOINs are used to retrieve data from normalized tables (reviewer, page 3)."
    },
    // Section 8: Specific MySQL JOIN Types (10 questions)
    {
        "Specific MySQL JOIN Types",
        "LEFT JOIN returns:",
        {"a. All rows from the right table", "b. All rows from the left table", "c. Only matching rows", "d. All combinations"},
        'b',
        "LEFT JOIN returns all rows from the left table, with NULLs for unmatched right table rows (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "RIGHT JOIN is also known as:",
        {"a. LEFT OUTER JOIN", "b. RIGHT OUTER JOIN", "c. INNER JOIN", "d. FULL JOIN"},
        'b',
        "RIGHT JOIN is synonymous with RIGHT OUTER JOIN (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "True or False: MySQL directly supports FULL OUTER JOIN.",
        {"a. True", "b. False", "c. Only in MySQL 8.0", "d. Only with UNION"},
        'b',
        "MySQL does not directly support FULL OUTER JOIN; it can be emulated with UNION (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "CROSS JOIN produces:",
        {"a. Matching rows only", "b. The Cartesian product of two tables", "c. All left table rows", "d. All right table rows"},
        'b',
        "CROSS JOIN returns the Cartesian product of two tables (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "SELF JOIN involves:",
        {"a. Joining two different tables", "b. Joining a table to itself", "c. Joining three tables", "d. No join condition"},
        'b',
        "SELF JOIN joins a table to itself using aliases (reviewer, page 4)."
    },
    {
        "Specific MySQL JOIN Types",
        "Which JOIN is used to find employees and their managers in the same table?",
        {"a. INNER JOIN", "b. LEFT JOIN", "c. SELF JOIN", "d. CROSS JOIN"},
        'c',
        "SELF JOIN is used for relationships within the same table, like employees and managers (reviewer, page 4)."
    },
    {
        "Specific MySQL JOIN Types",
        "FULL OUTER JOIN can be emulated in MySQL using:",
        {"a. INNER JOIN", "b. LEFT and RIGHT JOIN with UNION", "c. CROSS JOIN", "d. SELF JOIN"},
        'b',
        "FULL OUTER JOIN is emulated with UNION of LEFT and RIGHT JOINs (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "All of the following describe INNER JOIN EXCEPT:",
        {"a. Returns matching rows", "b. Excludes unmatched rows", "c. Includes all left table rows", "d. Uses a join condition"},
        'c',
        "INNER JOIN does not include all left table rows; that’s LEFT JOIN (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "The use case 'List all departments, even those without employees' requires:",
        {"a. INNER JOIN", "b. LEFT JOIN", "c. RIGHT JOIN", "d. CROSS JOIN"},
        'c',
        "RIGHT JOIN lists all right table rows (departments), even without matches (reviewer, page 3)."
    },
    {
        "Specific MySQL JOIN Types",
        "CROSS JOIN is useful for:",
        {"a. Matching related rows", "b. Generating all combinations", "c. Retrieving unmatched rows", "d. Joining a table to itself"},
        'b',
        "CROSS JOIN generates all combinations of two tables (reviewer, page 3)."
    },
    // Section 9: Practical Examples and Calculations (4 questions)
    {
        "Practical Examples and Calculations",
        "The SQL statement to retrieve employee names with department names uses:",
        {"a. INNER JOIN", "b. LEFT JOIN", "c. RIGHT JOIN", "d. CROSS JOIN"},
        'a',
        "INNER JOIN retrieves matching employee and department names (reviewer, page 4)."
    },
    {
        "Practical Examples and Calculations",
        "The constraint 'CREATE TABLE users (status VARCHAR(10) DEFAULT \\'active\\')' sets:",
        {"a. A default value", "b. A unique value", "c. A primary key", "d. A check condition"},
        'a',
        "This sets a DEFAULT constraint for the 'status' column (reviewer, page 2)."
    },
    {
        "Practical Examples and Calculations",
        "In an ERD for a School database, the number of entities for Students, Teachers, and Courses is:",
        {"a. 1", "b. 2", "c. 3", "d. 4"},
        'c',
        "Students, Teachers, and Courses are three distinct entities (reviewer, page 1)."
    },
    {
        "Practical Examples and Calculations",
        "The SQL command 'ALTER TABLE users ADD CONSTRAINT UNIQUE (email)' adds:",
        {"a. A NOT NULL constraint", "b. A UNIQUE constraint", "c. A FOREIGN KEY", "d. A CHECK constraint"},
        'b',
        "This command adds a UNIQUE constraint to the 'email' column (reviewer, page 3)."
    }
};

// Function to clear the screen (platform-dependent)
void clear_screen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// Function to randomize questions using Fisher-Yates shuffle
void randomize_questions(Question *quiz, int size) {
    srand((unsigned int)time(NULL));
    for (int i = size - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        // Swap quiz[i] and quiz[j]
        Question temp = quiz[i];
        quiz[i] = quiz[j];
        quiz[j] = temp;
    }
}

// Function to run the quiz
void run_quiz() {
    int score = 0;
    int section_scores[9][2] = {{0}}; // [0]: correct, [1]: total for 9 sections
    char section_names[9][MAX_STR] = {
        "ERD Basics", "ERD Components", "Participation Constraints",
        "MySQL Constraints Basics", "Specific MySQL Constraints",
        "Modifying Tables with Constraints", "MySQL JOIN Basics",
        "Specific MySQL JOIN Types", "Practical Examples and Calculations"
    };
    int results[NUM_QUESTIONS][3]; // [0]: correct (1/0), [1]: user_answer, [2]: correct_answer

    // Randomize questions
    randomize_questions(quiz, NUM_QUESTIONS);

    for (int i = 0; i < NUM_QUESTIONS; i++) {
        clear_screen();
        printf("Question %d of %d: %s\n", i + 1, NUM_QUESTIONS, quiz[i].section);
        printf("%s\n", quiz[i].question);
        for (int j = 0; j < MAX_CHOICES; j++) {
            printf("%s\n", quiz[i].choices[j]);
        }
        printf("\nEnter your answer (a, b, c, d, or e to exit): ");

        char answer;
        while (1) {
            scanf(" %c", &answer);
            if (answer == 'a' || answer == 'b' || answer == 'c' || answer == 'd') {
                break;
            }
            else if (answer == 'e') {
                return;
            }
            printf("Invalid input. Please enter a, b, c, d, or e to exit: ");
        }
        getchar(); // Clear newline

        // Determine section index
        int section_idx = 0;
        for (int j = 0; j < 9; j++) {
            if (strcmp(quiz[i].section, section_names[j]) == 0) {
                section_idx = j;
                break;
            }
        }
        section_scores[section_idx][1]++;

        if (answer == quiz[i].correct) {
            printf("\nCorrect!\n");
            score++;
            section_scores[section_idx][0]++;
            results[i][0] = 1;
        } else {
            printf("\nIncorrect! The correct answer is %c.\n", quiz[i].correct);
            printf("Reasoning: %s\n", quiz[i].reasoning);
            results[i][0] = 0;
        }
        results[i][1] = answer;
        results[i][2] = quiz[i].correct;

        printf("\nPress Enter to continue...");
        getchar();
    }

    // Display results
    clear_screen();
    printf("=== Quiz Results ===\n");
    printf("Total Questions: %d\n", NUM_QUESTIONS);
    printf("Correct Answers: %d\n", score);
    printf("Incorrect Answers: %d\n", NUM_QUESTIONS - score);
    printf("Percentage Score: %.2f%%\n", (float)score / NUM_QUESTIONS * 100);
    printf("\nPress Enter to continue...");
    getchar();

    clear_screen();
    printf("\nSection-wise Breakdown:\n");
    printf("--------------------------------------------------\n");
    printf("%-40s %-10s %-10s %-10s\n", "Section", "Correct", "Total", "Percentage");
    printf("--------------------------------------------------\n");
    for (int i = 0; i < 9; i++) {
        float percentage = section_scores[i][1] > 0 ? (float)section_scores[i][0] / section_scores[i][1] * 100 : 0;
        printf("%-40s %-10d %-10d %.2f%%\n", section_names[i], section_scores[i][0], section_scores[i][1], percentage);
    }
    printf("\nPress Enter to continue...");
    getchar();

    clear_screen();
    printf("\nDetailed Results:\n");
    printf("--------------------------------------------------\n");
    for (int i = 0; i < NUM_QUESTIONS; i++) {
        printf("Question %d: %s\n", i + 1, results[i][0] ? "Correct" : "Incorrect");
        if (!results[i][0]) {
            printf("Your answer: %c, Correct: %c\n", results[i][1], results[i][2]);
            printf("Reasoning: %s\n", quiz[i].reasoning);
        }
        printf("\n");
    }
    printf("\nPress Enter to continue...");
    getchar();
    
    clear_screen();
    printf("Thank you for answering this Mock Exam!");
}

int main() {
    printf("Welcome to the Database Systems Mock Exam!\n");
    printf("Answer each question with a, b, c, or d. Press Enter to proceed after each question.\n");
    printf("Press Enter to start...");
    getchar();
    run_quiz();
    return 0;
}