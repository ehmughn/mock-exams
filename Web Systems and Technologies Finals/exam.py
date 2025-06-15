import os
import random
from collections import defaultdict

# Quiz data: List of dictionaries containing question, choices, correct answer, reasoning, and section
quiz = [
    # Section 1: Web Development Life Cycle - Planning (10 questions)
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "What is the primary question that the planning phase of a website should answer?",
        "choices": ["a. How to host the website?", "b. What is the purpose of the website?", "c. What programming language to use?", "d. How to secure the website?"],
        "correct": "b",
        "reasoning": "The planning phase should answer 'what is the purpose of the website?' to guide development (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "True or False: Businesses create websites only to sell products.",
        "choices": ["a. True", "b. False", "c. Only for e-commerce", "d. Only for advertising"],
        "correct": "b",
        "reasoning": "Businesses create websites to advertise, sell products, or provide 24-hour support (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "Which of the following is a purpose for an individual developing a website?",
        "choices": ["a. To share hobbies", "b. To manage corporate databases", "c. To optimize network traffic", "d. To create a firewall"],
        "correct": "a",
        "reasoning": "Individuals develop websites to share hobbies, post resumes, or share ideas (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "All of the following are reasons organizations create websites EXCEPT:",
        "choices": ["a. Keep members informed", "b. Recruit new members", "c. Develop software", "d. Provide event updates"],
        "correct": "c",
        "reasoning": "Organizations create websites to inform or recruit members, not develop software (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "In the planning phase, understanding the computing environment of users is important to:",
        "choices": ["a. Choose a database", "b. Ensure compatibility", "c. Select a server", "d. Design graphics"],
        "correct": "b",
        "reasoning": "Understanding users’ computing environments ensures website compatibility (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "What is a key consideration in the planning phase?",
        "choices": ["a. Writing server-side code", "b. Identifying the website’s purpose", "c. Testing usability", "d. Maintaining backups"],
        "correct": "b",
        "reasoning": "Identifying the website’s purpose is critical in planning (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "Instructors may create websites to:",
        "choices": ["a. Sell products", "b. Inform students of course policies", "c. Manage network security", "d. Optimize server performance"],
        "correct": "b",
        "reasoning": "Instructors create websites to inform students of course policies or requirements (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "The planning phase should consider:",
        "choices": ["a. User tasks and content needs", "b. Database schema design", "c. Server-side scripting", "d. Graphic rendering"],
        "correct": "a",
        "reasoning": "Planning considers user tasks and content needs to define functionality (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "Which group creates websites to provide 24-hour online support?",
        "choices": ["a. Individuals", "b. Businesses", "c. Educational institutions", "d. Non-profits"],
        "correct": "b",
        "reasoning": "Businesses create websites for 24-hour online support (reviewer, page 7)."
    },
    {
        "section": "Web Development Life Cycle - Planning",
        "question": "True or False: Planning involves deciding the website’s programming language.",
        "choices": ["a. True", "b. False", "c. Only for dynamic sites", "d. Only for static sites"],
        "correct": "b",
        "reasoning": "Planning focuses on purpose and user needs, not programming languages (reviewer, page 7)."
    },
    # Section 2: Web Development Life Cycle - Analysis and Design (10 questions)
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "The analysis phase involves identifying:",
        "choices": ["a. Server hardware", "b. User tasks and website functionality", "c. Graphic design tools", "d. Hosting providers"],
        "correct": "b",
        "reasoning": "Analysis identifies user tasks and required website functionality (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "A key consideration in website design is:",
        "choices": ["a. Selecting a database", "b. Organizing webpage content", "c. Writing server-side scripts", "d. Configuring firewalls"],
        "correct": "b",
        "reasoning": "Organizing webpage content is a key design consideration (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "Which website structure connects pages in a straight line?",
        "choices": ["a. Hierarchical", "b. Linear", "c. Webbed", "d. Random"],
        "correct": "b",
        "reasoning": "Linear structure connects pages in a straight line for sequential reading (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "True or False: A hierarchical website structure is unsuitable for sites with a main index.",
        "choices": ["a. True", "b. False", "c. Only for large sites", "d. Only for small sites"],
        "correct": "b",
        "reasoning": "Hierarchical structure works well with a main index or table of contents (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "A webbed website structure is best for sites where:",
        "choices": ["a. Content must be read in order", "b. Users need many navigation options", "c. A single index is required", "d. Multimedia is avoided"],
        "correct": "b",
        "reasoning": "Webbed structure offers many navigation options with no set order (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "All of the following are website organizational standards EXCEPT:",
        "choices": ["a. Simple titles", "b. Headings for main topics", "c. Long paragraphs", "d. Contact email inclusion"],
        "correct": "c",
        "reasoning": "Paragraphs should be short to divide text; long paragraphs are not standard (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "Why should critical information be placed at the top of a webpage?",
        "choices": ["a. To reduce server load", "b. To increase user visibility", "c. To simplify coding", "d. To enhance security"],
        "correct": "b",
        "reasoning": "Placing critical information at the top increases the likelihood users see it (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "Horizontal rules in webpages are used to:",
        "choices": ["a. Encrypt data", "b. Separate main topics", "c. Validate forms", "d. Optimize images"],
        "correct": "b",
        "reasoning": "Horizontal rules provide graphical separation of main topics (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "Designing for accessibility involves:",
        "choices": ["a. Using complex graphics", "b. Addressing user access issues", "c. Minimizing content", "d. Avoiding navigation"],
        "correct": "b",
        "reasoning": "Accessibility design addresses issues to ensure user access (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Analysis and Design",
        "question": "A good webpage title should:",
        "choices": ["a. Be complex to attract attention", "b. Explain the page’s purpose", "c. Include many keywords", "d. Be hidden from users"],
        "correct": "b",
        "reasoning": "Simple titles explain the page’s purpose and aid search engine results (reviewer, page 8)."
    },
    # Section 3: Web Development Life Cycle - Testing and Implementation (10 questions)
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Usability testing measures how well a website:",
        "choices": ["a. Secures data", "b. Allows users to accomplish goals", "c. Loads quickly", "d. Uses multimedia"],
        "correct": "b",
        "reasoning": "Usability testing measures ease-of-use and user experience in achieving goals (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Which is a method of usability testing?",
        "choices": ["a. Encrypting data", "b. Observing users", "c. Writing server code", "d. Configuring DNS"],
        "correct": "b",
        "reasoning": "Usability testing can involve observing users performing tasks (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "True or False: Compatibility testing ensures a website works across different browsers.",
        "choices": ["a. True", "b. False", "c. Only for mobile browsers", "d. Only for desktop browsers"],
        "correct": "a",
        "reasoning": "Compatibility testing verifies functionality across various browsers and versions (reviewer, page 9)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Stress testing determines:",
        "choices": ["a. User satisfaction", "b. Performance under high user load", "c. Security vulnerabilities", "d. Content accuracy"],
        "correct": "b",
        "reasoning": "Stress testing checks website performance with many users (reviewer, page 9)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Implementation of a website involves:",
        "choices": ["a. Designing graphics", "b. Publishing the site", "c. Writing code", "d. Planning content"],
        "correct": "b",
        "reasoning": "Implementation is the actual publishing of the website (reviewer, page 9)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "All of the following are website testing steps EXCEPT:",
        "choices": ["a. Proofreading content", "b. Checking links", "c. Writing server scripts", "d. Testing forms"],
        "correct": "c",
        "reasoning": "Writing scripts is development, not testing (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Maintenance of a website includes:",
        "choices": ["a. Updating content and functionality", "b. Designing initial layout", "c. Selecting a domain", "d. Choosing a programming language"],
        "correct": "a",
        "reasoning": "Maintenance involves updating content, structure, and functionality (reviewer, page 9)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Checking graphics during testing ensures they:",
        "choices": ["a. Are encrypted", "b. Appear and link correctly", "c. Are dynamic", "d. Optimize server load"],
        "correct": "b",
        "reasoning": "Testing graphics confirms they display and link correctly (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Why test webpage load times?",
        "choices": ["a. To ensure security", "b. To improve user experience", "c. To validate forms", "d. To select a host"],
        "correct": "b",
        "reasoning": "Testing load times ensures a good user experience (reviewer, page 8)."
    },
    {
        "section": "Web Development Life Cycle - Testing and Implementation",
        "question": "Usability testing can involve:",
        "choices": ["a. Using a questionnaire", "b. Configuring servers", "c. Writing CSS", "d. Selecting fonts"],
        "correct": "a",
        "reasoning": "Questionnaires are used in usability testing to gather user feedback (reviewer, page 8)."
    },
    # Section 4: Client-Side and Server-Side Programming Basics (10 questions)
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Client-side scripting runs on the:",
        "choices": ["a. Web server", "b. User’s browser", "c. Database server", "d. DNS server"],
        "correct": "b",
        "reasoning": "Client-side scripts are executed by the user’s web browser (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Which is an example of client-side technology?",
        "choices": ["a. PHP", "b. JavaScript", "c. Ruby on Rails", "d. ASP"],
        "correct": "b",
        "reasoning": "JavaScript is a client-side scripting language (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "True or False: Server-side scripts generate dynamic HTML pages.",
        "choices": ["a. True", "b. False", "c. Only for static pages", "d. Only for client-side"],
        "correct": "a",
        "reasoning": "Server-side scripts generate dynamic HTML based on user requests (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Server-side scripting is used for:",
        "choices": ["a. Styling webpages", "b. Database interactions", "c. Animating graphics", "d. Validating forms locally"],
        "correct": "b",
        "reasoning": "Server-side scripting handles database interactions and dynamic responses (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "All of the following are server-side technologies EXCEPT:",
        "choices": ["a. PHP", "b. CSS", "c. ASP", "d. JSP"],
        "correct": "b",
        "reasoning": "CSS is client-side for styling; others are server-side (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Client-side scripts are embedded in HTML using:",
        "choices": ["a. The <SERVER> tag", "b. The <SCRIPT> tag", "c. The <DATABASE> tag", "d. The <STYLE> tag"],
        "correct": "b",
        "reasoning": "Client-side scripts use the <SCRIPT> tag in HTML (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "A disadvantage of posting online (e.g., wikis) is:",
        "choices": ["a. High control", "b. Lack of dynamic content", "c. Quick turnaround", "d. Ease of use"],
        "correct": "b",
        "reasoning": "Posting online lacks dynamic content compared to custom development (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Writing code from scratch offers:",
        "choices": ["a. Limited flexibility", "b. Complete control", "c. Ugly code", "d. Quick turnaround"],
        "correct": "b",
        "reasoning": "Writing from scratch provides complete control but is time-consuming (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Which is a disadvantage of WYSIWYG tools like Dreamweaver?",
        "choices": ["a. Flexible code", "b. Ugly code", "c. Fast development", "d. Cross-platform compatibility"],
        "correct": "b",
        "reasoning": "WYSIWYG tools often produce ugly or inefficient code (reviewer, page 9)."
    },
    {
        "section": "Client-Side and Server-Side Programming Basics",
        "question": "Server-side scripting allows for:",
        "choices": ["a. Local form validation", "b. Highly customizable responses", "c. Browser animations", "d. CSS styling"],
        "correct": "b",
        "reasoning": "Server-side scripting provides customizable responses based on user queries (reviewer, page 9)."
    },
    # Section 5: Web Hosting and Web Servers (8 questions)
    {
        "section": "Web Hosting and Web Servers",
        "question": "A web server is a program that:",
        "choices": ["a. Stores user data", "b. Answers HTTP requests", "c. Manages DNS", "d. Encrypts traffic"],
        "correct": "b",
        "reasoning": "A web server answers requests and sends responses via HTTP (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "Web server extensions are used for:",
        "choices": ["a. Styling webpages", "b. Server-side dynamic content", "c. Client-side animations", "d. DNS resolution"],
        "correct": "b",
        "reasoning": "Extensions like PHP or ASP enable server-side dynamic content (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "True or False: Hosting your own website avoids maintenance responsibilities.",
        "choices": ["a. True", "b. False", "c. Only for static sites", "d. Only for dynamic sites"],
        "correct": "b",
        "reasoning": "Self-hosting requires maintenance, backups, and upgrades (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "An advantage of using a hosting service is:",
        "choices": ["a. Full control over hardware", "b. Automatic backups", "c. Low cost always", "d. No limitations"],
        "correct": "b",
        "reasoning": "Hosting services often provide automatic backups (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "Which consideration is important when choosing a hosting service?",
        "choices": ["a. User interface design", "b. Disk space and traffic", "c. Graphic editing tools", "d. Client-side scripting"],
        "correct": "b",
        "reasoning": "Disk space and traffic are key hosting considerations (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "A disadvantage of self-hosting is:",
        "choices": ["a. High flexibility", "b. Expensive line speed", "c. Automatic backups", "d. Easy maintenance"],
        "correct": "b",
        "reasoning": "Self-hosting requires expensive high-speed connections (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "All of the following are hosting considerations EXCEPT:",
        "choices": ["a. Technology preferences", "b. Disk space", "c. Content design", "d. Traffic load"],
        "correct": "c",
        "reasoning": "Content design is not a hosting consideration (reviewer, page 10)."
    },
    {
        "section": "Web Hosting and Web Servers",
        "question": "Hosting services provide:",
        "choices": ["a. Complete hardware control", "b. High-speed connections", "c. Client-side scripting", "d. Graphic design tools"],
        "correct": "b",
        "reasoning": "Hosting services offer high-speed connections for accessibility (reviewer, page 10)."
    },
    # Section 6: Web Security Basics (10 questions)
    {
        "section": "Web Security Basics",
        "question": "Which is a traditional area of security concern?",
        "choices": ["a. Usability", "b. Confidentiality", "c. Performance", "d. Aesthetics"],
        "correct": "b",
        "reasoning": "Confidentiality is a key security concern, along with integrity and availability (reviewer, page 10)."
    },
    {
        "section": "Web Security Basics",
        "question": "True or False: Security needs are the same for all organizations.",
        "choices": ["a. True", "b. False", "c. Only for large organizations", "d. Only for small organizations"],
        "correct": "b",
        "reasoning": "Security needs vary by organization context (reviewer, page 10)."
    },
    {
        "section": "Web Security Basics",
        "question": "Network security involves:",
        "choices": ["a. Firewalls and operating systems", "b. Graphic design", "c. Client-side scripting", "d. Content management"],
        "correct": "a",
        "reasoning": "Network security includes firewalls and OS protections (reviewer, page 10)."
    },
    {
        "section": "Web Security Basics",
        "question": "What is a vulnerability in an application?",
        "choices": ["a. A secure feature", "b. A design flaw or bug", "c. A user interface", "d. A performance boost"],
        "correct": "b",
        "reasoning": "A vulnerability is a design flaw or bug that allows attacks (reviewer, page 11)."
    },
    {
        "section": "Web Security Basics",
        "question": "All of the following are types of security EXCEPT:",
        "choices": ["a. Physical", "b. Network", "c. Application", "d. Usability"],
        "correct": "d",
        "reasoning": "Usability is not a type of security (reviewer, page 10)."
    },
    {
        "section": "Web Security Basics",
        "question": "A threat agent is:",
        "choices": ["a. A security protocol", "b. An individual or group exploiting vulnerabilities", "c. A user interface", "d. A performance metric"],
        "correct": "b",
        "reasoning": "Threat agents are individuals or groups that can manifest threats (reviewer, page 10)."
    },
    {
        "section": "Web Security Basics",
        "question": "Controls in security are used to:",
        "choices": ["a. Enhance aesthetics", "b. Detect or deter attacks", "c. Optimize load times", "d. Design navigation"],
        "correct": "b",
        "reasoning": "Controls detect, deter, or deny attacks (reviewer, page 11)."
    },
    {
        "section": "Web Security Basics",
        "question": "Business impact of a security breach may include loss of:",
        "choices": ["a. Usability", "b. Reputation", "c. Navigation options", "d. Page load speed"],
        "correct": "b",
        "reasoning": "Business impacts include loss of reputation, money, or customers (reviewer, page 11)."
    },
    {
        "section": "Web Security Basics",
        "question": "Technical impact refers to:",
        "choices": ["a. User satisfaction", "b. System damage from a breach", "c. Content accuracy", "d. Design quality"],
        "correct": "b",
        "reasoning": "Technical impact is the system damage from a security breach (reviewer, page 11)."
    },
    {
        "section": "Web Security Basics",
        "question": "The OWASP Top 10 aims to:",
        "choices": ["a. Optimize websites", "b. Educate about security risks", "c. Design user interfaces", "d. Test usability"],
        "correct": "b",
        "reasoning": "OWASP Top 10 educates about application security risks (reviewer, page 11)."
    },
    # Section 7: OWASP Top 10 Risks - Part 1 (A1-A5) (10 questions)
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "Injection flaws (A1) occur when:",
        "choices": ["a. Data is encrypted", "b. Untrusted data is sent to an interpreter", "c. Pages load slowly", "d. Users are authenticated"],
        "correct": "b",
        "reasoning": "Injection flaws involve untrusted data tricking an interpreter (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "Broken Authentication (A2) allows attackers to:",
        "choices": ["a. Optimize performance", "b. Compromise user identities", "c. Enhance navigation", "d. Validate forms"],
        "correct": "b",
        "reasoning": "Broken authentication lets attackers assume user identities (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "True or False: Cross-Site Scripting (XSS, A3) executes scripts in the user’s browser.",
        "choices": ["a. True", "b. False", "c. Only for server-side", "d. Only for databases"],
        "correct": "a",
        "reasoning": "XSS allows attackers to execute scripts in the victim’s browser (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "Insecure Direct Object References (A4) expose:",
        "choices": ["a. User interfaces", "b. Internal implementation objects", "c. Secure data", "d. Navigation menus"],
        "correct": "b",
        "reasoning": "A4 exposes internal objects like files or database keys (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "Security Misconfiguration (A5) involves:",
        "choices": ["a. Secure default settings", "b. Improperly configured servers", "c. Validated redirects", "d. Encrypted data"],
        "correct": "b",
        "reasoning": "A5 results from insecure configurations of servers or platforms (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "All of the following are injection types (A1) EXCEPT:",
        "choices": ["a. SQL", "b. OS", "c. LDAP", "d. CSS"],
        "correct": "d",
        "reasoning": "CSS is not an injection type; SQL, OS, and LDAP are (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "XSS (A3) can lead to:",
        "choices": ["a. Faster page loads", "b. Hijacking user sessions", "c. Secure authentication", "d. Optimized graphics"],
        "correct": "b",
        "reasoning": "XSS can hijack sessions or deface websites (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "A4 can be prevented by:",
        "choices": ["a. Exposing all objects", "b. Implementing access control checks", "c. Using untrusted data", "d. Avoiding encryption"],
        "correct": "b",
        "reasoning": "Access control checks prevent insecure direct object references (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "Security Misconfiguration (A5) requires:",
        "choices": ["a. Secure configuration maintenance", "b. Open default settings", "c. Unvalidated redirects", "d. Exposed sensitive data"],
        "correct": "a",
        "reasoning": "A5 requires defined and maintained secure configurations (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 1",
        "question": "Broken Authentication (A2) may involve flaws in:",
        "choices": ["a. Session management", "b. Page load speed", "c. Graphic design", "d. Content organization"],
        "correct": "a",
        "reasoning": "A2 includes flaws in authentication and session management (reviewer, page 11)."
    },
    # Section 8: OWASP Top 10 Risks - Part 2 (A6-A10) (10 questions)
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "Sensitive Data Exposure (A6) involves:",
        "choices": ["a. Proper encryption", "b. Weakly protected data", "c. Validated redirects", "d. Secure configurations"],
        "correct": "b",
        "reasoning": "A6 occurs when sensitive data lacks proper encryption or hashing (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "Missing Function Level Access Control (A7) allows:",
        "choices": ["a. All users to access all functions", "b. Secure data exposure", "c. Validated redirects", "d. Optimized performance"],
        "correct": "a",
        "reasoning": "A7 permits unauthorized access to functions due to missing controls (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "True or False: CSRF (A8) forces a user’s browser to send forged requests.",
        "choices": ["a. True", "b. False", "c. Only for unauthenticated users", "d. Only for server-side"],
        "correct": "a",
        "reasoning": "CSRF forces a logged-on user’s browser to send forged HTTP requests (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "Using Components with Known Vulnerabilities (A9) is common because:",
        "choices": ["a. Components are always secure", "b. Developers may not track versions", "c. All components are updated", "d. Vulnerabilities are rare"],
        "correct": "b",
        "reasoning": "A9 occurs due to untracked or outdated component versions (reviewer, page 12)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "Unvalidated Redirects and Forwards (A10) can lead to:",
        "choices": ["a. Secure authentication", "b. Phishing or malware sites", "c. Optimized load times", "d. Validated forms"],
        "correct": "b",
        "reasoning": "A10 allows redirects to malicious sites without validation (reviewer, page 12)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "All of the following are sensitive data (A6) EXCEPT:",
        "choices": ["a. Credit cards", "b. SSNs", "c. Navigation menus", "d. Authentication credentials"],
        "correct": "c",
        "reasoning": "Navigation menus are not sensitive data; others require protection (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "CSRF (A8) exploits:",
        "choices": ["a. Secure session cookies", "b. User’s authenticated session", "c. Encrypted data", "d. Validated redirects"],
        "correct": "b",
        "reasoning": "CSRF uses a victim’s authenticated session to send forged requests (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "A7 can be caused by:",
        "choices": ["a. Proper access checks", "b. Misconfigured function access", "c. Encrypted data", "d. Validated inputs"],
        "correct": "b",
        "reasoning": "Missing function-level access control is due to misconfiguration or lack of checks (reviewer, page 11)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "To prevent A9, developers should:",
        "choices": ["a. Use outdated components", "b. Keep components updated", "c. Avoid access controls", "d. Expose sensitive data"],
        "correct": "b",
        "reasoning": "Updating components prevents known vulnerabilities (reviewer, page 12)."
    },
    {
        "section": "OWASP Top 10 Risks - Part 2",
        "question": "Unvalidated Redirects (A10) use:",
        "choices": ["a. Trusted data only", "b. Untrusted data for destinations", "c. Encrypted links", "d. Secure configurations"],
        "correct": "b",
        "reasoning": "A10 uses untrusted data to determine redirect destinations (reviewer, page 12)."
    },
    # Section 9: Practical Examples and Applications (12 questions)
    {
        "section": "Practical Examples and Applications",
        "question": "A website with a table of contents linking to detailed pages uses a:",
        "choices": ["a. Linear structure", "b. Hierarchical structure", "c. Webbed structure", "d. Random structure"],
        "correct": "b",
        "reasoning": "Hierarchical structure uses a main index linking to detailed pages (reviewer, page 8)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "Testing a website’s links to ensure they are not broken is part of:",
        "choices": ["a. Planning", "b. Design", "c. Testing", "d. Maintenance"],
        "correct": "c",
        "reasoning": "Checking links is a testing step to ensure functionality (reviewer, page 8)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "A website using JavaScript for interactive effects is an example of:",
        "choices": ["a. Server-side scripting", "b. Client-side scripting", "c. Database management", "d. Web hosting"],
        "correct": "b",
        "reasoning": "JavaScript is used for client-side interactive effects (reviewer, page 9)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "A website using PHP to query a database uses:",
        "choices": ["a. Client-side scripting", "b. Server-side scripting", "c. CSS styling", "d. HTML markup"],
        "correct": "b",
        "reasoning": "PHP is a server-side scripting language for database interactions (reviewer, page 9)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "Choosing a hosting service with sufficient disk space is important for:",
        "choices": ["a. Content storage", "b. Graphic design", "c. Client-side scripting", "d. Usability testing"],
        "correct": "a",
        "reasoning": "Disk space is needed for storing website content (reviewer, page 10)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "An SQL injection attack is an example of OWASP risk:",
        "choices": ["a. A1 - Injection", "b. A2 - Broken Authentication", "c. A3 - XSS", "d. A4 - Insecure References"],
        "correct": "a",
        "reasoning": "SQL injection is a type of injection flaw (A1) (reviewer, page 11)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "A website redirecting users to a phishing site is an example of:",
        "choices": ["a. A7 - Missing Access Control", "b. A8 - CSRF", "c. A9 - Vulnerable Components", "d. A10 - Unvalidated Redirects"],
        "correct": "d",
        "reasoning": "Unvalidated redirects (A10) can lead to phishing sites (reviewer, page 12)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "Including a contact email on a webpage follows which standard?",
        "choices": ["a. Page length", "b. Organizational standard", "c. Horizontal rule", "d. List usage"],
        "correct": "b",
        "reasoning": "Including a contact email is an organizational standard (reviewer, page 8)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "A website failing under high traffic is identified through:",
        "choices": ["a. Usability testing", "b. Compatibility testing", "c. Stress testing", "d. Proofreading"],
        "correct": "c",
        "reasoning": "Stress testing checks performance under high user load (reviewer, page 9)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "Protecting credit card data from theft addresses OWASP risk:",
        "choices": ["a. A5 - Security Misconfiguration", "b. A6 - Sensitive Data Exposure", "c. A7 - Missing Access Control", "d. A8 - CSRF"],
        "correct": "b",
        "reasoning": "A6 addresses weak protection of sensitive data like credit cards (reviewer, page 11)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "Using outdated libraries in a website is an example of:",
        "choices": ["a. A1 - Injection", "b. A3 - XSS", "c. A9 - Vulnerable Components", "d. A10 - Unvalidated Redirects"],
        "correct": "c",
        "reasoning": "A9 involves using components with known vulnerabilities (reviewer, page 12)."
    },
    {
        "section": "Practical Examples and Applications",
        "question": "A website allowing unauthorized access to admin functions is an example of:",
        "choices": ["a. A2 - Broken Authentication", "b. A7 - Missing Access Control", "c. A8 - CSRF", "d. A9 - Vulnerable Components"],
        "correct": "b",
        "reasoning": "A7 involves missing function-level access controls (reviewer, page 11)."
    }
]

def randomize_questions(quiz_list):
    """
    Randomizes the order of questions in the quiz list in place.
    
    Args:
        quiz_list (list): List of dictionaries containing quiz questions
    """
    random.shuffle(quiz_list)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz():
    score = 0
    results = []
    section_scores = defaultdict(lambda: {"correct": 0, "total": 0})
    
    # Randomize the quiz questions
    randomize_questions(quiz)
    
    for i, item in enumerate(quiz, 1):
        clear_screen()
        print(f"Question {i} of {len(quiz)}: {item['section']}")
        print(item['question'])
        for choice in item['choices']:
            print(choice)
        print("\nEnter your answer (a, b, c, or d): ", end="")
        
        while True:
            answer = input().strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            print("Invalid input. Please enter a, b, c, or d: ", end="")
        
        correct = item['correct']
        section = item['section']
        section_scores[section]["total"] += 1
        
        if answer == correct:
            print("\nCorrect!")
            score += 1
            section_scores[section]["correct"] += 1
            results.append((i, True, answer, correct, ""))
        else:
            print(f"\nIncorrect! The correct answer is {correct}.")
            print(f"Reasoning: {item['reasoning']}")
            results.append((i, False, answer, correct, item['reasoning']))
        
        print("\nPress Enter to continue...", end="")
        input()

    # Display results
    clear_screen()
    print("=== Quiz Results ===")
    print(f"Total Questions: {len(quiz)}")
    print(f"Correct Answers: {score}")
    print(f"Incorrect Answers: {len(quiz) - score}")
    print(f"Percentage Score: {(score / len(quiz)) * 100:.2f}%")
    
    print("\nSection-wise Breakdown:")
    print("-" * 50)
    print(f"{'Section':<40} {'Correct':<10} {'Total':<10} {'Percentage':<10}")
    print("-" * 50)
    for section, data in section_scores.items():
        correct = data['correct']
        total = data['total']
        percentage = (correct / total) * 100 if total > 0 else 0
        print(f"{section:<40} {correct:<10} {total:<10} {percentage:.2f}%")
    
    print("\nDetailed Results:")
    print("-" * 50)
    for result in results:
        q_num, is_correct, user_answer, correct_answer, reasoning = result
        status = "Correct" if is_correct else f"Incorrect (Your answer: {user_answer}, Correct: {correct_answer})"
        print(f"Question {q_num}: {status}")
        if not is_correct:
            print(f"Reasoning: {reasoning}")
        print()

if __name__ == "__main__":
    print("Welcome to the Web Technology Quiz Bee!")
    print("Answer each question with a, b, c, or d. Press Enter to proceed after each question.")
    print("Press Enter to start...", end="")
    input()
    run_quiz()