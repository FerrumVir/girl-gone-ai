# Coding Assistant AI Prompt Pack — 100+ Developer Prompts

---

## How to Use This Pack

This pack contains 105 prompts organized across 8 categories for software developers. Every prompt is copy-paste ready — replace the bracketed [PLACEHOLDER] variables with your specific code, language, or context before submitting to your AI assistant (ChatGPT, Claude, Gemini, GitHub Copilot Chat, etc.).

**Tips for getting the best results from AI coding assistants:**

1. **Provide real code, not descriptions of code.** Paste the actual function, file, or stack trace. AI cannot infer what your code looks like — it needs to see it.
2. **Specify your language, framework, and version.** "Python 3.11 with FastAPI" produces better output than "Python." "React 18 with TypeScript" beats "React."
3. **State your constraints upfront.** If you can't use external libraries, if you need to maintain backward compatibility, or if performance is critical — say so in the prompt.
4. **Break complex problems into steps.** Use a planning prompt first ("outline the approach"), then an implementation prompt, then a review prompt.
5. **Always review output before using it.** AI can produce plausible-looking code with subtle bugs. Read it. Test it. Verify edge cases.
6. **Chain prompts.** Generate code → review it for security → write tests for it → generate documentation. Each step builds on the last.
7. **Use language-specific variants.** Where prompts say [LANGUAGE], be specific. The more context you give, the less generic the output.

**How placeholders work:**
- `[LANGUAGE]` — programming language (e.g., Python, TypeScript, Go, Rust, Java)
- `[FRAMEWORK]` — the framework in use (e.g., Django, Next.js, Spring Boot, FastAPI)
- `[CODE BLOCK]` — paste your actual code here
- `[ERROR MESSAGE]` — the full error or stack trace
- `[DESCRIPTION]` — a plain-English description of what the code should do
- `[REQUIREMENT]` — a specific technical or business requirement

---

## Category 1: Debugging (15 Prompts)

### 1. Error Analysis — Full Context

```
I'm getting the following error in my [LANGUAGE] [FRAMEWORK] application:

Error message:
[PASTE FULL ERROR MESSAGE]

Stack trace:
[PASTE FULL STACK TRACE]

Relevant code:
[PASTE CODE BLOCK]

Environment: [OS, language version, framework version, relevant dependencies and versions]

Please:
1. Identify the root cause of this error (not just the surface symptom)
2. Explain why this error occurs in clear terms
3. Provide the corrected code
4. List any other places in the codebase where this same issue might exist (based on the pattern you see)
5. Explain what I should test to confirm the fix works
```

### 2. Stack Trace Interpretation

```
Help me interpret this stack trace from a [LANGUAGE] application. I am a [SKILL LEVEL: junior/mid/senior] developer and want to understand not just the fix, but the cause.

Stack trace:
[PASTE STACK TRACE]

Walk me through:
1. How to read this stack trace from bottom to top — which frame is the true origin of the problem?
2. What each relevant frame tells us
3. The sequence of events that led to this error
4. What I should look at in my code to find and fix the root cause

Do not just give me the fix — teach me how to diagnose this class of error myself next time.
```

### 3. Logic Bug Hunting

```
The following [LANGUAGE] function is producing incorrect output. It is supposed to [DESCRIBE INTENDED BEHAVIOR], but instead it [DESCRIBE ACTUAL BEHAVIOR].

Code:
[PASTE CODE BLOCK]

Test case where it fails:
- Input: [INPUT]
- Expected output: [EXPECTED]
- Actual output: [ACTUAL]

Please:
1. Trace through the code step-by-step with the failing input to find where the logic goes wrong
2. Identify the specific line(s) where the bug lives
3. Explain why the current logic is incorrect
4. Provide the corrected code
5. Suggest 3 additional test cases that would catch this type of bug in the future
```

### 4. Performance Profiling Analysis

```
The following [LANGUAGE] [FRAMEWORK] code is running slower than expected. Profile it and identify performance bottlenecks.

Code:
[PASTE CODE BLOCK]

Context:
- What this code does: [DESCRIPTION]
- Current performance: [METRIC — e.g., "takes 3.2 seconds for 10,000 records"]
- Target performance: [METRIC]
- Data characteristics: [e.g., "input arrays of 10,000–100,000 items," "100 concurrent users"]

Please:
1. Identify all performance bottlenecks, ranked by impact
2. Explain why each bottleneck is expensive (algorithmic complexity, I/O, memory allocation, etc.)
3. Provide an optimized version of the code
4. Estimate the performance improvement each change should deliver
5. Note any trade-offs (readability, memory, complexity) in your optimizations
```

### 5. Memory Leak Detection

```
I suspect a memory leak in the following [LANGUAGE] application. The process memory grows over time even when load is constant.

Relevant code:
[PASTE CODE BLOCK]

Symptoms:
- Memory grows approximately [SIZE] per [TIMEFRAME/OPERATION]
- The leak appears to occur when [TRIGGER OR PATTERN]
- Runtime environment: [DESCRIPTION]

Please:
1. Identify the most likely sources of memory leaks in this code
2. Explain the memory management issue in each case
3. Provide corrected code that fixes the leaks
4. Recommend specific tools and commands to profile memory in [LANGUAGE/ENVIRONMENT] so I can verify the fix
5. Describe the pattern I should watch for to prevent this class of leak going forward
```

### 6. Async/Concurrency Bug Analysis

```
I have a concurrency bug in my [LANGUAGE] code. The behavior is non-deterministic — sometimes it works, sometimes it doesn't.

Code:
[PASTE CODE BLOCK]

Observed behavior:
- [DESCRIBE WHAT HAPPENS INTERMITTENTLY]
- The issue appears more frequently under [HIGH LOAD / CONCURRENT REQUESTS / SPECIFIC CONDITIONS]

Please:
1. Identify all potential race conditions, deadlocks, or synchronization issues in this code
2. Explain each concurrency hazard and when it would manifest
3. Provide thread-safe / async-safe corrected code
4. Recommend how to write a reliable test that can consistently reproduce concurrency bugs like this
5. Note any concurrency patterns or primitives in [LANGUAGE] I should learn to prevent these issues
```

### 7. Third-Party Library / Dependency Error

```
I'm getting an error related to a third-party library in my [LANGUAGE] project.

Error:
[PASTE ERROR]

My code:
[PASTE CODE BLOCK]

Library: [LIBRARY NAME] version [VERSION]
My [LANGUAGE] version: [VERSION]
Relevant dependencies: [LIST OTHER RELEVANT PACKAGES AND VERSIONS]

Please:
1. Determine if this is a usage error, a compatibility issue, or a library bug
2. Show the correct way to use this library for my use case
3. If it's a version incompatibility, identify the compatible versions
4. If there's a known workaround or alternative approach, describe it
5. Provide a minimal working example of the correct usage
```

### 8. Environment / Configuration Debug

```
My [LANGUAGE] application works correctly in [ENVIRONMENT A] but fails in [ENVIRONMENT B].

Error in [ENVIRONMENT B]:
[PASTE ERROR]

Configuration differences I'm aware of:
[LIST KNOWN DIFFERENCES: OS versions, env variables, dependency versions, etc.]

Code that fails:
[PASTE CODE BLOCK]

Please:
1. Identify the most likely environment-related causes of this discrepancy
2. What configuration, dependency, or system difference is the probable culprit?
3. How do I verify which factor is causing the issue?
4. What's the fix for [ENVIRONMENT B]?
5. How do I prevent environment-specific failures in this codebase going forward?
```

### 9. Regex Debugging

```
The following regular expression is not matching what I expect.

Language/flavor: [LANGUAGE/REGEX FLAVOR]
Regex: [PASTE REGEX]
Input string: [PASTE INPUT]
Expected match: [WHAT SHOULD MATCH]
Actual result: [WHAT ACTUALLY MATCHES OR DOESN'T]

Please:
1. Explain what this regex currently matches, character by character
2. Identify exactly where the pattern deviates from my intent
3. Provide a corrected regex
4. Annotate the corrected regex with comments explaining each part
5. Provide 5 test strings: 3 that should match and 2 that should not, to verify correctness
```

### 10. Database Query Debug

```
The following SQL query (or ORM query) is returning incorrect results or performing poorly.

Database: [PostgreSQL / MySQL / SQLite / other]
ORM if applicable: [FRAMEWORK AND VERSION]

Query:
[PASTE QUERY]

Schema (relevant tables):
[PASTE SCHEMA OR TABLE DEFINITIONS]

Problem:
- Expected: [WHAT THE QUERY SHOULD RETURN]
- Actual: [WHAT IT ACTUALLY RETURNS, OR PERFORMANCE METRICS]

Please:
1. Identify the logical error or performance issue in the query
2. Explain what the current query actually does vs. what I intended
3. Provide a corrected query
4. If performance is the issue, show the query plan I should examine and how to read it
5. Suggest indexes or schema changes that would further improve performance
```

### 11. Type Error / Type Mismatch Debug

```
I'm getting a type error in my [LANGUAGE] code. I don't understand why the types aren't aligning.

Error:
[PASTE TYPE ERROR]

Code:
[PASTE CODE BLOCK]

Relevant type definitions:
[PASTE TYPE DEFINITIONS, INTERFACES, OR SCHEMAS]

Please:
1. Explain what types are in conflict and why
2. Show exactly where the type mismatch originates
3. Provide the corrected code with proper typing
4. Explain the typing pattern or concept I'm missing (e.g., generics, union types, type narrowing)
5. Show me how to use [LANGUAGE]'s type system to catch this class of error at compile time going forward
```

### 12. API / Network Request Debug

```
My [LANGUAGE] application is making an API request that is failing or returning unexpected results.

Request details:
- Method: [GET/POST/PUT/DELETE]
- Endpoint: [URL PATTERN — redact auth tokens]
- Headers: [RELEVANT HEADERS]
- Request body (if applicable): [BODY]

Error/unexpected response:
[PASTE ERROR OR RESPONSE]

My code making the request:
[PASTE CODE BLOCK]

Please:
1. Identify what's wrong with the request (malformed body, wrong auth, incorrect headers, etc.)
2. Provide the corrected request code
3. Show me how to add proper error handling and logging so I can debug API issues faster in the future
4. What cURL command would replicate this exact request so I can test it independently?
```

### 13. Build / Compilation Error Debug

```
My [LANGUAGE] project fails to build with the following error.

Build tool: [WEBPACK / GRADLE / CARGO / MAKEFILE / OTHER]
Language/version: [LANGUAGE VERSION]

Full build error output:
[PASTE FULL ERROR]

Project structure (relevant parts):
[PASTE FILE TREE OR CONFIGURATION SNIPPETS]

Please:
1. Identify the root cause of the build failure
2. Show the specific configuration or code change needed to fix it
3. If multiple files need to be changed, list all of them with the required changes
4. Explain why this error occurs so I understand the build system behavior
```

### 14. Test Failure Debug

```
The following test is failing and I don't understand why.

Test framework: [JEST / PYTEST / JUNIT / RSPEC / OTHER]
Language: [LANGUAGE]

Failing test:
[PASTE TEST CODE]

Test output / failure message:
[PASTE FULL TEST OUTPUT]

Code under test:
[PASTE FUNCTION OR CLASS BEING TESTED]

Please:
1. Explain exactly what assertion is failing and why
2. Is this a bug in the code under test, or a bug in the test itself?
3. If the code under test is wrong, show the fix
4. If the test is wrong, show the corrected test
5. What does this failure reveal about the behavior of the function?
```

### 15. Null / Undefined Error Trace

```
I'm getting a null reference or undefined error in my [LANGUAGE] application.

Error:
[PASTE ERROR]

Code:
[PASTE CODE BLOCK]

Data flow:
- This value originates from: [DATA SOURCE — API response, database, user input, etc.]
- It passes through: [TRANSFORMATION STEPS IF APPLICABLE]

Please:
1. Identify exactly where the null/undefined value enters the system
2. Trace the execution path to the point where it causes a failure
3. Provide a defensive fix that handles the null case gracefully
4. Explain the best practice for null safety in [LANGUAGE] — what patterns should I adopt to prevent this class of error?
5. Identify any other places in the surrounding code where the same assumption is made dangerously
```

---

## Category 2: Code Review (15 Prompts)

### 16. Security Review

```
Perform a security-focused code review on the following [LANGUAGE] [FRAMEWORK] code.

Code:
[PASTE CODE BLOCK]

Context:
- This code handles: [DESCRIPTION — e.g., user authentication, file uploads, payment processing]
- It is exposed to: [PUBLIC API / INTERNAL ONLY / ADMIN ONLY]
- Known threats relevant to this feature: [ANY YOU'RE AWARE OF]

Please review for:
1. Injection vulnerabilities (SQL, command, LDAP, XSS, etc.)
2. Authentication and authorization flaws
3. Sensitive data exposure (logs, responses, storage)
4. Insecure direct object references
5. Security misconfigurations
6. Cryptographic weaknesses
7. Any other vulnerabilities specific to [FRAMEWORK/CONTEXT]

For each issue: severity (Critical/High/Medium/Low), explanation, and remediated code.
```

### 17. Performance Review

```
Perform a performance-focused code review on the following [LANGUAGE] code.

Code:
[PASTE CODE BLOCK]

Context:
- Expected load: [REQUESTS PER SECOND / RECORDS PROCESSED / CONCURRENT USERS]
- Performance-sensitive because: [REASON]
- Current performance baseline (if known): [METRICS]

Review for:
1. Algorithmic complexity — identify any O(n²) or worse operations that could be improved
2. Unnecessary database queries (N+1, redundant reads, missing eager loading)
3. Memory inefficiency (unnecessary copying, large object allocation in loops)
4. Missing caching opportunities
5. Blocking I/O in async contexts
6. Any other patterns that would degrade performance at scale

For each issue: estimated impact, explanation, and improved code.
```

### 18. Readability and Maintainability Review

```
Review the following [LANGUAGE] code for readability and long-term maintainability.

Code:
[PASTE CODE BLOCK]

Team context: [solo developer / team of N / junior-heavy team / senior team]
Coding standards we follow: [PEP 8 / Google style / our own — describe briefly, or "none yet"]

Review for:
1. Naming clarity (variables, functions, classes — are they self-documenting?)
2. Function length and single-responsibility adherence
3. Code duplication that should be extracted
4. Comment quality (missing, outdated, or explaining "what" instead of "why")
5. Magic numbers and hardcoded values that should be constants
6. Error handling completeness and clarity
7. Consistency with established patterns

Provide: a line-by-line or section-by-section review, and a refactored version implementing your suggestions.
```

### 19. Architecture Review

```
Review the architecture of the following [LANGUAGE] [FRAMEWORK] module/feature.

Code (provide all relevant files):
[PASTE CODE BLOCKS]

System context:
- This module's role: [DESCRIPTION]
- How it's called: [HTTP endpoint / internal service / cron job / event handler / etc.]
- External dependencies: [DATABASES, APIs, SERVICES IT TALKS TO]
- Current scale: [USAGE VOLUME]
- Expected growth: [SCALE EXPECTATIONS]

Review for:
1. Separation of concerns — are responsibilities clearly divided?
2. Coupling — is this module too tightly coupled to others?
3. Cohesion — does each unit do one thing well?
4. Dependency management — are dependencies injected or hardcoded?
5. Error boundaries — does it handle failures from external dependencies gracefully?
6. Scalability — what breaks first as load increases?
7. Testability — how easy is it to write automated tests for this?

Provide: findings, architectural concerns, and a recommended refactored structure (diagrams in ASCII if helpful).
```

### 20. PR Description Generator

```
Write a pull request description for the following code changes.

PR title: [TITLE]
Branch: [BRANCH NAME]
Base branch: [MAIN / DEVELOP / OTHER]

Diff summary (paste your git diff or describe the changes):
[PASTE DIFF OR DESCRIBE CHANGES]

Ticket/issue reference: [TICKET NUMBER OR LINK]

Write a PR description including:
1. Summary (2–3 sentences): what does this PR do and why?
2. Changes made (bulleted list of specific changes, not a rehash of the diff)
3. Motivation and context: why was this change necessary?
4. Testing done: how was this verified? (list tests run, manual testing steps)
5. Screenshots or examples (placeholder note if visual changes exist)
6. Breaking changes (if any)
7. Reviewer notes: anything that needs special attention or a specific reviewer

Use markdown formatting for GitHub/GitLab/Bitbucket.
```

### 21. Dependency / Package Audit

```
Review the following dependency list for my [LANGUAGE] project and identify potential issues.

Package file contents:
[PASTE package.json / requirements.txt / Cargo.toml / pom.xml / go.mod]

Please identify:
1. Known security vulnerabilities in listed packages (based on your training data — note I should also run [npm audit / pip-audit / cargo audit / etc.])
2. Outdated packages that have significant newer versions with important improvements
3. Redundant or overlapping packages that could be consolidated
4. Packages with poor maintenance signals (abandoned, few contributors)
5. Heavy packages where a lighter alternative exists for my use case
6. Any version pinning issues (too loose or too strict)

Prioritize findings by severity.
```

### 22. API Design Review

```
Review the design of the following API and suggest improvements.

API specification:
[PASTE OPENAPI SPEC, ROUTE DEFINITIONS, OR DESCRIBE THE ENDPOINTS]

Context:
- API type: [REST / GraphQL / gRPC / other]
- Consumers: [FRONTEND / MOBILE / THIRD-PARTY / INTERNAL SERVICES]
- Authentication: [METHOD]

Review for:
1. RESTful / protocol conventions adherence (naming, HTTP verbs, status codes)
2. Consistency across endpoints
3. Versioning strategy
4. Error response format and informativeness
5. Breaking change risks
6. Missing endpoints or resources that consumers will likely need
7. Security surface area (over-exposed data, missing auth on routes)
8. Performance considerations (pagination, filtering, field selection)

Provide: annotated review + redesigned endpoint table.
```

### 23. Database Schema Review

```
Review the following database schema and suggest improvements.

Schema:
[PASTE CREATE TABLE STATEMENTS OR SCHEMA DEFINITION]

Database: [PostgreSQL / MySQL / SQLite / MongoDB / other]
Application type: [DESCRIPTION — e.g., "SaaS with 10k users," "internal analytics tool"]
Expected query patterns: [DESCRIBE THE 3–5 MOST COMMON QUERIES OR ACCESS PATTERNS]

Review for:
1. Normalization issues (over or under normalized)
2. Missing or suboptimal indexes for stated query patterns
3. Data type choices (are they appropriate?)
4. Naming conventions consistency
5. Missing constraints (NOT NULL, UNIQUE, FOREIGN KEYS, CHECK)
6. Fields that should or shouldn't have defaults
7. Any fields suggesting a design smell (e.g., JSON blobs hiding a missing table)
8. Scalability concerns at [EXPECTED SCALE]

Provide: annotated review + improved schema DDL.
```

### 24. Test Coverage Review

```
Review the test suite for the following [LANGUAGE] code and identify gaps.

Code under test:
[PASTE CODE BLOCK]

Existing tests:
[PASTE TEST FILE]

Test framework: [FRAMEWORK]

Please identify:
1. Code paths that have zero test coverage
2. Edge cases that are not tested (nulls, empty inputs, boundary values, error states)
3. Tests that are too tightly coupled to implementation (testing internals, not behavior)
4. Tests that are redundant or provide no additional confidence
5. Missing integration points that should be tested
6. Tests that could be flaky (timing dependencies, external calls without mocking)

Then: write the 5 highest-value missing tests that would most improve coverage.
```

### 25. Error Handling Review

```
Review the error handling in the following [LANGUAGE] code.

Code:
[PASTE CODE BLOCK]

Context:
- This code is called by: [USER-FACING API / INTERNAL SERVICE / BACKGROUND JOB]
- The consequences of unhandled errors here: [DESCRIPTION]

Review for:
1. Unhandled exceptions or errors that could bubble up unexpectedly
2. Overly broad exception catches that hide bugs
3. Error messages that expose internal implementation details (security issue)
4. Missing error logging (or logging in the wrong place)
5. Errors that should trigger retries vs. immediate failure vs. graceful degradation
6. User-facing error messages that are unhelpful or confusing
7. Missing circuit breakers or timeouts on external calls

Provide: annotated findings and a refactored version with robust error handling.
```

### 26. Code Smell Detection

```
Identify code smells in the following [LANGUAGE] code and suggest refactoring approaches.

Code:
[PASTE CODE BLOCK]

Look for:
1. Long methods (doing too much)
2. Large classes (too many responsibilities)
3. Feature envy (a method that uses another object's data more than its own)
4. Data clumps (groups of data that always appear together but aren't encapsulated)
5. Primitive obsession (using primitives where a domain object would be clearer)
6. Switch statements that should be polymorphism
7. Parallel inheritance hierarchies
8. Dead code
9. Speculative generality (abstraction for future requirements that don't exist yet)
10. Comments explaining what instead of why

For each smell found: name it, show where it is, explain why it's problematic, and suggest the specific refactoring to apply.
```

### 27. Logging and Observability Review

```
Review the logging and observability practices in the following [LANGUAGE] [FRAMEWORK] code.

Code:
[PASTE CODE BLOCK]

Current logging setup:
[DESCRIBE YOUR LOGGING LIBRARY AND CONFIGURATION]
[PASTE RELEVANT LOGGING CONFIGURATION IF APPLICABLE]

Monitoring/alerting tools in use: [LIST TOOLS — e.g., Datadog, CloudWatch, Grafana]

Review for:
1. Missing log statements at critical execution points
2. Log statements with insufficient context (missing request IDs, user IDs, correlation IDs)
3. Sensitive data being logged
4. Incorrect log levels (DEBUG in prod, ERROR for expected conditions)
5. Missing structured logging (using string concatenation instead of key-value pairs)
6. Absent or insufficient metrics instrumentation
7. Missing distributed tracing spans
8. Error events that don't generate alerts

Provide: a refactored version with improved observability.
```

### 28. Accessibility Review (Frontend)

```
Review the following [HTML / JSX / Vue template / other] for accessibility issues.

Code:
[PASTE FRONTEND CODE]

Framework: [REACT / VUE / SVELTE / VANILLA HTML / OTHER]
Target WCAG level: [A / AA / AAA]

Review for:
1. Missing or incorrect ARIA labels and roles
2. Images without alt text (or with unhelpful alt text)
3. Form inputs without associated labels
4. Keyboard navigation issues (focus order, focus trapping, skip links)
5. Color contrast issues (describe the color palette so I can check)
6. Interactive elements that aren't accessible to screen readers
7. Missing landmark regions
8. Dynamic content updates not announced to assistive technology

Provide: annotated findings and corrected code for each issue.
```

### 29. Mobile / Responsive Code Review (Frontend)

```
Review the following CSS / [FRAMEWORK] component code for responsive design and mobile usability issues.

Code:
[PASTE CODE BLOCK]

Target devices: [MOBILE-FIRST / DESKTOP-FIRST, screen size range]
Framework: [TAILWIND / BOOTSTRAP / VANILLA CSS / STYLED-COMPONENTS / OTHER]

Review for:
1. Fixed pixel values that break at small screen sizes
2. Missing or incorrect breakpoints
3. Touch target sizes below 44x44px minimum
4. Horizontal scrolling issues
5. Text that becomes too small or too large at certain viewports
6. Images not properly sized or cropped for mobile
7. Layout issues in landscape vs. portrait orientation
8. Performance-heavy CSS that should be optimized for mobile networks

Provide: corrected code with responsive fixes applied.
```

### 30. Internationalization (i18n) Review

```
Review the following [LANGUAGE] / [FRAMEWORK] code for internationalization readiness.

Code:
[PASTE CODE BLOCK]

Current i18n setup (if any): [DESCRIBE OR PASTE CONFIG]
Target locales: [LIST TARGET LANGUAGES/REGIONS]

Review for:
1. Hardcoded strings that should be externalized
2. String concatenation that breaks in non-English languages (word order)
3. Date, time, number, and currency formatting that isn't locale-aware
4. Pluralization logic that doesn't account for languages with complex plural rules
5. RTL layout considerations (if targeting Arabic, Hebrew, etc.)
6. Missing locale in API calls or database queries
7. Untranslated error messages or validation messages

Provide: a migration checklist and example i18n-ready refactoring of the worst offenders.
```

---

## Category 3: Refactoring (15 Prompts)

### 31. Extract Method / Function

```
Refactor the following [LANGUAGE] function by extracting smaller, focused helper functions.

Code:
[PASTE CODE BLOCK]

Goals:
- Each extracted function should do one thing and do it clearly
- Function names should be self-documenting
- The main function should read like a high-level description of the process
- Maintain identical external behavior

Please:
1. Identify the logical segments within this function that should be extracted
2. Propose meaningful names for each extracted function
3. Show the refactored code with all extractions applied
4. Confirm that no behavior has changed (trace through a sample execution)
```

### 32. Simplify Conditionals

```
Simplify the conditional logic in the following [LANGUAGE] code without changing its behavior.

Code:
[PASTE CODE BLOCK]

Please apply as many of these techniques as appropriate:
1. Consolidate duplicate conditional fragments
2. Replace nested ternaries with clear if/else or early returns
3. Decompose complex conditions into named boolean variables
4. Remove dead branches (conditions that can never be true)
5. Replace switch/if-else chains with a lookup table or polymorphism where appropriate
6. Apply guard clauses to reduce nesting

Show the refactored version and confirm equivalent behavior with a test case trace.
```

### 33. Apply Design Pattern

```
Refactor the following [LANGUAGE] code by applying the [DESIGN PATTERN NAME] design pattern.

Code:
[PASTE CODE BLOCK]

Why I think this pattern applies: [YOUR REASONING, OR "not sure — please advise"]

Please:
1. Confirm whether [DESIGN PATTERN] is the right pattern here, or suggest an alternative if not
2. Explain how the pattern applies to this specific code
3. Provide the fully refactored code with the pattern implemented
4. Explain the benefit this pattern brings to this code (testability, extensibility, maintainability)
5. Identify one future change to requirements that this pattern would make significantly easier to implement

If you're suggesting an alternative pattern, explain why it's more appropriate.
```

### 34. Replace Conditionals with Polymorphism

```
Refactor the following [LANGUAGE] code that uses type-checking conditionals (if/switch on type) to use polymorphism instead.

Code:
[PASTE CODE BLOCK]

Please:
1. Identify all places where the code branches based on a type, category, or flag
2. Design the class hierarchy or interface that eliminates these branches
3. Show the fully refactored code: base class/interface + all concrete implementations + updated calling code
4. Demonstrate how adding a new type would work in the refactored version (it should require no changes to existing conditional logic)
```

### 35. Dependency Injection Refactor

```
Refactor the following [LANGUAGE] code to use dependency injection instead of hardcoded dependencies.

Code:
[PASTE CODE BLOCK]

Current hardcoded dependencies:
[LIST THE DEPENDENCIES THAT ARE CREATED INSIDE THE CLASS/FUNCTION — e.g., "instantiates a DatabaseConnection directly"]

Please:
1. Identify all tightly coupled dependencies
2. Refactor to inject these dependencies through the constructor (or function parameters)
3. Show updated class/function signature
4. Explain how this change makes the code more testable (show a simplified unit test that mocks one dependency)
5. If a dependency injection framework is commonly used with [LANGUAGE/FRAMEWORK], mention it
```

### 36. Apply SOLID Principles

```
Review the following [LANGUAGE] code and refactor it to better adhere to SOLID principles.

Code:
[PASTE CODE BLOCK]

For each SOLID principle, note:
- Single Responsibility: Does each class/function have one reason to change?
- Open/Closed: Is the code open for extension without modification?
- Liskov Substitution: Can subtypes replace parent types without breaking behavior?
- Interface Segregation: Are interfaces too large or doing too much?
- Dependency Inversion: Are high-level modules depending on abstractions, not concretions?

For each violation you find: name the principle violated, show the specific code, and provide the refactored version.
```

### 37. Remove Code Duplication (DRY)

```
Identify and eliminate code duplication in the following [LANGUAGE] code.

Code:
[PASTE CODE BLOCK — CAN BE MULTIPLE FILES OR FUNCTIONS]

Please:
1. Identify every instance of duplication (copy-paste code, repeated logic, similar patterns)
2. Categorize each duplication: exact copy / structural similarity / conceptual duplication
3. Propose the right abstraction to eliminate each duplication (extracted function, base class, utility module, generic/template, higher-order function)
4. Show the refactored code with all duplication eliminated
5. Note any duplication you intentionally left (and why the abstraction would cost more than it saves)
```

### 38. Modernize Legacy Code

```
Modernize the following [LANGUAGE] code to use current idioms and best practices. The code was written for [OLD VERSION OR ERA: e.g., "Python 2," "ES5 JavaScript," "Java 7"].

Code:
[PASTE CODE BLOCK]

Target version/standard: [TARGET VERSION — e.g., "Python 3.11," "ES2022," "Java 17"]

Please update:
1. Syntax: use modern language syntax where it improves clarity
2. APIs: replace deprecated APIs with current equivalents
3. Patterns: replace old patterns with modern idioms (e.g., callbacks → async/await, var → const/let)
4. Error handling: apply modern error handling conventions
5. Type annotations: add type hints/annotations where the language supports them

Show before/after and explain each modernization.
```

### 39. Functional Refactor (Imperative → Functional)

```
Refactor the following [LANGUAGE] imperative code to use a more functional style.

Code:
[PASTE CODE BLOCK]

Please:
1. Replace mutable state with immutable transformations where practical
2. Replace for loops with map, filter, reduce, or equivalent functional operations
3. Extract pure functions (no side effects) from mixed-concern code
4. Identify and eliminate shared mutable state
5. Note any places where a purely functional style would harm readability or performance — and leave those imperative

Show the refactored code and comment on what was gained and what trade-offs were made.
```

### 40. Class Decomposition

```
The following [LANGUAGE] class is doing too much. Decompose it into smaller, focused classes.

Code:
[PASTE CLASS]

Please:
1. Identify the distinct responsibilities currently bundled in this class
2. Propose a design with [NUMBER] classes, each with one clear responsibility
3. Define the interface/contract between the new classes
4. Show the complete refactored code for all new classes
5. Show how the calling code changes (if at all)
6. Confirm that the combined behavior of the new classes is identical to the original
```

### 41. Add Type Safety

```
Add comprehensive type annotations/declarations to the following [LANGUAGE] code.

Code:
[PASTE CODE BLOCK]

Language: [TYPESCRIPT / PYTHON WITH MYPY / GO / RUST / OTHER STRONGLY TYPED LANGUAGE]

Please:
1. Add type annotations to all function signatures (parameters and return types)
2. Define interfaces/types/structs for data structures that don't have them
3. Replace any `any`, `object`, or overly broad types with specific types
4. Add generics where the function is type-agnostic but should be type-safe
5. Note any places where the types reveal a potential runtime bug

Show the fully typed version and explain any non-obvious type choices.
```

### 42. Configuration Externalization

```
Refactor the following [LANGUAGE] code to move all hardcoded configuration values to a proper configuration system.

Code:
[PASTE CODE BLOCK]

Hardcoded values to externalize: [LIST THEM OR LET AI IDENTIFY THEM]
Environment: [CLOUD PROVIDER / DOCKER / BARE METAL / LOCAL DEV]
Configuration method preference: [ENV VARS / CONFIG FILE / SECRETS MANAGER]

Please:
1. Identify every hardcoded value (API keys, URLs, timeouts, thresholds, feature flags, credentials)
2. Propose the right storage mechanism for each (env vars for secrets, config files for app settings, etc.)
3. Show the refactored code that reads from configuration
4. Provide a sample .env.example or config template file
5. Add validation that fails loudly at startup if required config is missing
```

### 43. Async/Await Refactor (Callbacks/Promises → Async/Await)

```
Refactor the following [LANGUAGE] code from [CALLBACKS / PROMISE CHAINS] to async/await syntax.

Code:
[PASTE CODE BLOCK]

Please:
1. Convert all callback-based or .then()/.catch() chains to async/await
2. Maintain the same error handling semantics (which errors should be caught where)
3. Handle parallel operations correctly (don't accidentally serialize operations that should run concurrently — use Promise.all or equivalent)
4. Show the refactored code
5. Highlight any cases where the refactoring changed the execution order or error propagation, and confirm the new behavior is correct
```

### 44. Data Model Refactor

```
Refactor the following data model/schema to better represent the domain.

Current model:
[PASTE CLASS DEFINITIONS, INTERFACES, OR SCHEMA]

Problems I've noticed (or suspect):
[DESCRIBE THE ISSUES — e.g., "the User object has both billing and auth fields," "we're using a string for status instead of an enum"]

Domain context:
[DESCRIBE WHAT THIS DATA REPRESENTS IN PLAIN ENGLISH]

Please:
1. Identify all data modeling issues (inappropriate types, missing domain concepts, mixed concerns, anemic models)
2. Propose a refactored model that better reflects the domain
3. Show the new model definitions
4. Describe what migration steps would be needed to move from the old model to the new one
5. Identify any breaking changes to code that uses the old model
```

### 45. Performance-Oriented Refactor

```
Refactor the following [LANGUAGE] code to improve performance while maintaining identical behavior.

Code:
[PASTE CODE BLOCK]

Performance constraint:
- Current: [METRIC — e.g., "processes 1,000 records in 8 seconds"]
- Target: [METRIC — e.g., "must handle 10,000 records in under 2 seconds"]
- Data characteristics: [DESCRIBE INPUT SIZE AND SHAPE]

Please:
1. Profile the algorithmic complexity of the current implementation
2. Identify the highest-impact optimization opportunities
3. Apply optimizations: better algorithms, data structure choices, caching, lazy evaluation, batching
4. Show the optimized code
5. Analyze the new complexity and estimate the speedup
6. Note any new trade-offs (memory usage, code complexity, correctness edge cases)
```

---

## Category 4: Architecture (15 Prompts)

### 46. System Design — Feature Addition

```
Help me design the architecture for adding [NEW FEATURE] to an existing [SYSTEM DESCRIPTION] application.

Current system:
- Language/framework: [LANGUAGE/FRAMEWORK]
- Database: [DATABASE]
- Infrastructure: [CLOUD / ON-PREM / HYBRID — brief description]
- Current scale: [USERS / REQUESTS PER DAY]
- Architecture style: [MONOLITH / MICROSERVICES / SERVERLESS / OTHER]

New feature requirements:
[DESCRIBE THE FEATURE IN DETAIL — what it does, who uses it, expected load, latency requirements]

Please design:
1. How this feature fits into the current architecture
2. New components or services needed
3. Data model changes
4. API surface area
5. Integration points with existing systems
6. Rollout strategy (feature flags, dark launch, gradual rollout)
7. Key risks and how to mitigate them

Use ASCII diagrams if helpful.
```

### 47. API Design — New Service

```
Design a [REST / GraphQL / gRPC] API for [SERVICE NAME], a service that [DESCRIPTION OF WHAT THE SERVICE DOES].

Consumers: [WHO WILL CALL THIS API — frontend, mobile, other microservices]
Authentication: [METHOD]
Scale requirements: [EXPECTED REQUESTS/SECOND, DATA VOLUME]

Design:
1. Resource model (what are the entities/resources?)
2. Endpoint definitions (method, path, request/response schema for each)
3. Authentication and authorization model
4. Error response format and status code conventions
5. Pagination, filtering, and sorting conventions
6. Versioning strategy
7. Rate limiting approach

Provide an OpenAPI 3.0 snippet or a clearly formatted endpoint table. Include example request/response pairs for the 3 most important endpoints.
```

### 48. Database Schema Design

```
Design a database schema for [APPLICATION TYPE] that needs to support the following data and operations:

Entities and their relationships:
[DESCRIBE THE DOMAIN — e.g., "Users who have many Projects, Projects have many Tasks, Tasks can have a parent Task"]

Key query patterns (the most frequent or performance-critical queries):
1. [QUERY PATTERN 1]
2. [QUERY PATTERN 2]
3. [QUERY PATTERN 3]

Constraints:
- Database: [POSTGRESQL / MYSQL / MONGODB / OTHER]
- Expected data volume: [RECORDS PER TABLE AT STEADY STATE]
- Write-heavy vs. read-heavy: [DESCRIBE RATIO]

Provide:
1. Entity-relationship description
2. Full CREATE TABLE statements with appropriate column types and constraints
3. Index recommendations for each key query pattern
4. Any design decisions that warrant explanation (why normalized vs. denormalized, etc.)
```

### 49. Microservices Decomposition

```
Help me decompose the following monolithic application into microservices.

Current monolith:
[DESCRIBE THE MONOLITH — key modules, data model, tech stack, team size]

Problem being solved by decomposing:
[DEPLOYMENT INDEPENDENCE / TEAM SCALING / PERFORMANCE / TECH DIVERSITY / OTHER]

Please:
1. Identify natural service boundaries based on domain and data ownership
2. Define [NUMBER] proposed microservices: name, responsibility, owned data
3. Describe the communication pattern between services (sync REST, async messaging, event-driven)
4. Identify shared data problems and how to resolve them (shared databases are the wrong answer)
5. Define the migration sequence: how to extract services incrementally without a big-bang rewrite
6. Identify the services that present the highest migration risk and why

Use the strangler fig pattern or other incremental approaches.
```

### 50. Scalability Analysis

```
Analyze the scalability of the following system and identify the bottlenecks that will limit growth.

System description:
[DESCRIBE YOUR ARCHITECTURE — components, databases, caches, queues, CDN, etc.]

Current metrics:
- Requests per second: [X]
- Database size: [X]
- Response p50/p95/p99: [TIMES]
- Infrastructure: [SERVERS / CONTAINERS / SERVERLESS — describe]

Growth target: handle [X times current load] within [TIMEFRAME].

Please:
1. Identify the first bottleneck that will be hit as load increases
2. Walk through the cascade: after fixing bottleneck 1, what breaks next?
3. For each bottleneck: the problem, the solution, and the approximate load at which it becomes critical
4. Recommend a prioritized scaling roadmap
5. Identify any architectural decisions that will require invasive changes at scale (and suggest addressing them now)
```

### 51. Caching Strategy Design

```
Design a caching strategy for [APPLICATION TYPE] with the following characteristics:

Read/write patterns:
- [DATA TYPE 1]: read [X times] per second, changes [FREQUENCY]
- [DATA TYPE 2]: read [X times] per second, changes [FREQUENCY]

Consistency requirements:
- [DATA TYPE 1] can tolerate stale data for up to [DURATION]
- [DATA TYPE 2] must always be fresh (or near-fresh)

Infrastructure: [REDIS / MEMCACHED / IN-PROCESS / CDN / OTHER]
Language/framework: [LANGUAGE/FRAMEWORK]

Design:
1. What to cache and what not to cache (with reasoning)
2. Cache key naming conventions
3. TTL strategy for each data type
4. Cache invalidation approach (TTL only / event-driven / write-through / write-behind)
5. Cache stampede protection
6. Cache warming strategy
7. Monitoring and cache hit rate targets

Provide code examples for the cache read/write patterns in [LANGUAGE].
```

### 52. Event-Driven Architecture Design

```
Design an event-driven architecture for [USE CASE] that replaces/extends the current [SYNCHRONOUS / POLLING / DIRECT CALL] approach.

Current behavior:
[DESCRIBE WHAT CURRENTLY HAPPENS — e.g., "Service A calls Service B synchronously and waits for a response"]

Problem with current approach:
[DESCRIBE THE ISSUE — e.g., "tight coupling, cascading failures, slow performance"]

Services involved:
[LIST SERVICES AND THEIR ROLES]

Message broker options available: [KAFKA / RABBITMQ / AWS SQS/SNS / REDIS STREAMS / OTHER]

Design:
1. Event taxonomy: list all events, their names, producers, and consumers
2. Event schema for each event type (JSON example)
3. Queue/topic topology
4. Consumer group strategy
5. Error handling: dead letter queues, retry policy, idempotency
6. Ordering guarantees: which events require ordering and how to achieve it
7. Observability: how to trace a request across event-driven flows
```

### 53. Authentication and Authorization Design

```
Design an authentication and authorization system for [APPLICATION TYPE] with the following requirements:

User types: [LIST USER ROLES — e.g., admin, regular user, read-only viewer, API client]
Access control model: [RBAC / ABAC / ACL / SIMPLE BOOLEAN — or "help me choose"]
Sensitive operations requiring special controls: [LIST]
Multi-tenancy: [YES / NO — if yes, describe isolation requirements]
API type: [REST / GraphQL / OTHER]

Design:
1. Authentication flow (how users prove who they are)
2. Token strategy (JWT vs. opaque sessions — recommend with reasoning)
3. Authorization model: how permissions are defined, stored, and checked
4. Role definitions and permission matrix
5. Code pattern for enforcing permissions (middleware, decorators, guards)
6. Token lifecycle: expiry, refresh, revocation
7. Service-to-service authentication

Provide code examples for [LANGUAGE/FRAMEWORK] for the most critical patterns.
```

### 54. Data Pipeline Architecture

```
Design a data pipeline for [USE CASE — e.g., "ETL from Postgres to analytics warehouse," "real-time event processing"].

Data sources:
- [SOURCE 1]: type, volume, update frequency
- [SOURCE 2]: type, volume, update frequency

Data destinations:
- [DESTINATION]: purpose, query patterns

Latency requirements: [REAL-TIME / NEAR-REAL-TIME (seconds) / BATCH (minutes/hours/daily)]
Data volume: [RECORDS PER DAY / GB PER DAY]
Transformation needs: [DESCRIBE TRANSFORMATIONS NEEDED]

Design:
1. Pipeline architecture (streaming vs. batch vs. lambda)
2. Technology recommendations with justification
3. Data flow diagram (ASCII)
4. Schema evolution strategy
5. Error handling and data quality checks
6. Monitoring and alerting
7. Cost considerations

Language/platform preference: [IF ANY]
```

### 55. Monolith to Serverless Migration Plan

```
Design a migration plan to move [PORTION OR ALL] of a [LANGUAGE/FRAMEWORK] monolith to a serverless architecture on [AWS / GCP / AZURE].

Current monolith:
- Language/framework: [LANGUAGE/FRAMEWORK]
- Key functions/endpoints: [LIST THE MAIN OPERATIONS]
- Database: [DATABASE]
- Current traffic pattern: [STEADY / SPIKY / LOW VOLUME]
- Team size: [NUMBER OF DEVELOPERS]

Migration goals: [COST REDUCTION / SCALABILITY / REDUCED OPS OVERHEAD / OTHER]

Provide:
1. Suitability assessment: which parts of the monolith are good candidates for serverless (and which are not)
2. Recommended serverless services for each component
3. Data access patterns: how functions will talk to the database without connection pool exhaustion
4. Cold start mitigation strategy
5. Migration sequence (what to migrate first, second, last)
6. Cost estimate framework (how to evaluate cost before and after)
7. Rollback plan if migration causes problems
```

### 56. Service Mesh and Observability Design

```
Design the observability and service mesh strategy for a [NUMBER]-service microservices application.

Services:
[LIST YOUR SERVICES AND THEIR LANGUAGES/FRAMEWORKS]

Infrastructure: [KUBERNETES / ECS / VMs / OTHER]
Current observability: [WHAT YOU HAVE NOW — or "none"]

Design:
1. Distributed tracing: tool recommendation and instrumentation strategy
2. Metrics: what to measure per service (the four golden signals: latency, traffic, errors, saturation)
3. Logging: structured logging format, correlation ID propagation, aggregation
4. Service mesh: do we need one? If yes, [ISTIO / LINKERD / OTHER] recommendation with reasoning
5. Alerting: thresholds and escalation paths for critical metrics
6. Runbook template for common failure scenarios

Provide: instrumentation code snippets for [PRIMARY LANGUAGE].
```

### 57. Multi-Tenant Architecture Design

```
Design a multi-tenant architecture for [APPLICATION TYPE] where [TENANT DESCRIPTION — e.g., "each tenant is a company with multiple users"].

Isolation requirements:
- Data isolation: [STRICT (separate DBs) / LOGICAL (shared DB, tenant ID) / HYBRID]
- Performance isolation: [CAN TENANTS IMPACT EACH OTHER'S PERFORMANCE? YES/NO]
- Customization: [CAN TENANTS HAVE CUSTOM CONFIGS / FEATURES?]

Scale: [EXPECTED NUMBER OF TENANTS, USERS PER TENANT, DATA VOLUME PER TENANT]

Design:
1. Tenant isolation model recommendation with trade-offs
2. Database tenancy strategy (database per tenant / schema per tenant / row-level isolation)
3. Tenant identification in the request path
4. Cross-tenant data leakage prevention (middleware, query patterns, tests)
5. Tenant-specific configuration management
6. Onboarding and offboarding flows
7. Billing and usage metering hooks

Language/framework: [LANGUAGE/FRAMEWORK]
```

### 58. Disaster Recovery and Backup Design

```
Design a disaster recovery strategy for [APPLICATION] running on [INFRASTRUCTURE].

Application components:
- [COMPONENT 1]: type, data stored, current backup status
- [COMPONENT 2]: type, data stored, current backup status

RTO (Recovery Time Objective — how long can you be down): [TIME]
RPO (Recovery Point Objective — how much data loss is acceptable): [DURATION]
Compliance requirements: [GDPR / HIPAA / SOC2 / NONE / OTHER]

Design:
1. Backup strategy for each component (frequency, retention, storage location)
2. Failover architecture (what needs to be redundant for the RTO to be achievable)
3. Recovery playbooks (step-by-step for the 3 most likely disaster scenarios)
4. Regular DR testing process
5. Cost estimate framework for the proposed DR setup
6. Monitoring that detects the need to invoke DR before it's too late
```

### 59. Technical Debt Roadmap

```
Help me create a technical debt reduction roadmap for [PROJECT/SYSTEM].

Current technical debt items I'm aware of:
[LIST ALL KNOWN DEBT ITEMS — e.g., "no tests on the payment module," "outdated ORM version," "no error monitoring"]

Project constraints:
- Team size: [NUMBER OF DEVELOPERS]
- Velocity: [SPRINTS PER QUARTER OR SIMILAR]
- Feature work committed for next [TIMEFRAME]: [BRIEF DESCRIPTION]

Please:
1. Categorize each debt item: Critical (causes incidents) / High (slows development significantly) / Medium / Low
2. Estimate relative effort for each item (Small/Medium/Large)
3. Identify dependencies between debt items (what must be done before what)
4. Propose a 3-month roadmap balancing debt reduction with feature delivery (e.g., 20% of every sprint)
5. Identify which debt item, if addressed first, creates the most leverage for addressing the others
```

### 60. Feature Flag Architecture

```
Design a feature flag system for [APPLICATION TYPE] in [LANGUAGE/FRAMEWORK].

Requirements:
- Flag types needed: [RELEASE FLAGS / EXPERIMENT FLAGS / OPS FLAGS / PERMISSION FLAGS]
- Targeting: [% ROLLOUT / USER SEGMENTS / SPECIFIC USER IDs / ALL OR NOTHING]
- Flag evaluation: [SERVER-SIDE / CLIENT-SIDE / BOTH]
- Team size using flags: [NUMBER OF DEVELOPERS]
- Preference: [BUILD IN-HOUSE / USE LAUNCHDARKLY / USE UNLEASH / OTHER]

Design:
1. Flag storage and management approach
2. SDK/integration for [LANGUAGE/FRAMEWORK]
3. Flag evaluation at the right layer (API, service, frontend)
4. Stale flag detection and cleanup process
5. Audit logging for flag changes
6. Emergency kill switch pattern

Provide: a code example of implementing and evaluating a flag in [LANGUAGE/FRAMEWORK].
```

---

## Category 5: Testing (15 Prompts)

### 61. Unit Test Generation

```
Write comprehensive unit tests for the following [LANGUAGE] function.

Code:
[PASTE FUNCTION]

Test framework: [JEST / PYTEST / JUNIT / RSPEC / VITEST / OTHER]
Mocking library: [IF APPLICABLE]

Write tests that cover:
1. The happy path with typical valid inputs
2. Edge cases: empty inputs, null/undefined, empty collections, zero values
3. Boundary values: minimum, maximum, values just inside and outside valid ranges
4. Error cases: what should happen when the function is called incorrectly?
5. All logical branches (ensure every if/else and conditional path is exercised)

For each test:
- Use a descriptive test name that reads like documentation
- Follow Arrange-Act-Assert structure
- Add a one-line comment explaining what scenario the test covers if the name isn't sufficient

Coverage target: 100% branch coverage.
```

### 62. Integration Test Scenarios

```
Design integration test scenarios for the following feature/API endpoint.

Feature: [DESCRIPTION OF THE FEATURE OR ENDPOINT]
Components involved: [LIST — e.g., "API handler → Service layer → Database → External payment API"]
Language/framework: [LANGUAGE/FRAMEWORK]
Test environment: [HOW INTEGRATION TESTS ARE RUN — e.g., "Docker Compose with a real Postgres instance"]

Please:
1. List all integration test scenarios (test the interaction between components, not just one unit)
2. For each scenario: describe the setup (test data, mocked external dependencies), the action, and the expected outcome
3. Identify which external dependencies should be mocked vs. real in these tests
4. Write the 3 most important integration tests as actual code
5. Note any test data management considerations (seeding, teardown, isolation between tests)
```

### 63. Edge Case Identification

```
Identify edge cases that should be tested for the following [LANGUAGE] function or system.

Code / System description:
[PASTE CODE OR DESCRIBE THE SYSTEM]

Input types: [DESCRIBE THE INPUTS]
Business rules: [DESCRIBE RELEVANT RULES — e.g., "dates must be in the future," "quantity must be positive integer"]

Generate a comprehensive edge case list covering:
1. Empty / null / undefined inputs
2. Single-item inputs (when the function handles collections)
3. Very large inputs (performance and overflow)
4. Very small inputs (zero, empty string, minimum values)
5. Boundary conditions (off-by-one, date boundaries, timezone edges)
6. Concurrent access scenarios
7. Invalid data types
8. Data that is technically valid but unusual (e.g., Unicode in text fields, negative zero)
9. Stateful edge cases (what if this is called twice? in the wrong order?)
10. Any domain-specific edge cases relevant to [BUSINESS CONTEXT]

For each edge case: describe the scenario, the expected behavior, and the risk if it's not handled.
```

### 64. Test Data Generation

```
Generate realistic test data for [DESCRIPTION OF WHAT YOU'RE TESTING] in [LANGUAGE].

Data requirements:
- [ENTITY 1]: [FIELD DESCRIPTIONS AND CONSTRAINTS]
- [ENTITY 2]: [FIELD DESCRIPTIONS AND CONSTRAINTS]

Scenarios needed:
- [NUMBER] "happy path" records
- [NUMBER] records representing edge cases: [LIST]
- [NUMBER] records representing invalid data (to test validation rejection)

Please:
1. Generate the test data as [JSON / SQL INSERT statements / [LANGUAGE] objects / CSV]
2. Use realistic values (real-looking names, valid email formats, believable numbers)
3. Create a factory function or fixture in [LANGUAGE/FRAMEWORK] to generate this data programmatically
4. Note any data dependencies (e.g., a record in Table B requires a record in Table A to exist first)
```

### 65. Mocking Strategy

```
Design the mocking strategy for testing the following [LANGUAGE] class/module.

Code to test:
[PASTE CODE]

External dependencies this code calls:
- [DEPENDENCY 1]: what it does, how it's called
- [DEPENDENCY 2]: what it does, how it's called

Test framework: [FRAMEWORK]
Mocking library: [LIBRARY — e.g., jest.mock(), unittest.mock, Mockito, testify/mock]

Please:
1. Identify everything that should be mocked (and explain why)
2. Identify anything that should NOT be mocked (and explain why)
3. Show the mock setup for each dependency
4. Write example tests showing the mock in use for: happy path, error from dependency, slow/timeout from dependency
5. Explain how to verify that the mocks were called correctly (call count, arguments)
```

### 66. Property-Based Test Design

```
Design property-based tests for the following [LANGUAGE] function.

Function:
[PASTE FUNCTION]

Property-based testing library: [HYPOTHESIS / FAST-CHECK / QUICKCHECK / OTHER]

Please:
1. Identify 3–5 properties that should always hold true for this function, regardless of input:
   - Examples: "output length is always <= input length," "function is idempotent," "output is always sorted"
2. Translate each property into a property-based test
3. Define the input generators needed (types, ranges, constraints)
4. Identify what failure cases property tests might find that example-based tests would miss
5. Show the complete test code

Also write the equivalent example-based tests for comparison.
```

### 67. End-to-End Test Script

```
Write an end-to-end test script for the following user flow in [APPLICATION].

User flow:
[DESCRIBE THE COMPLETE FLOW — e.g., "User navigates to login page, enters credentials, submits form, is redirected to dashboard, and sees their name in the header"]

E2E Framework: [PLAYWRIGHT / CYPRESS / SELENIUM / PUPPETEER / OTHER]
Language: [LANGUAGE]
Base URL for tests: [URL PLACEHOLDER]

Test requirements:
1. Test the complete happy path as described
2. Test failed login (wrong password) — verify error message appears
3. Test session persistence (refresh page and remain logged in)

Write the complete test file with:
- Page object model (if framework supports it)
- Proper selectors (prefer data-testid attributes)
- Explicit waits instead of arbitrary sleeps
- Clear test descriptions
- Assertion for each critical step
```

### 68. Test Coverage Analysis Prompt

```
Analyze the test coverage of the following [LANGUAGE] code and identify what's missing.

Production code:
[PASTE CODE]

Existing tests:
[PASTE TESTS]

Coverage tool output (if available):
[PASTE COVERAGE REPORT OR DESCRIBE WHAT YOU KNOW]

Please:
1. Map out all execution paths in the production code
2. Identify which paths are covered by existing tests
3. List all uncovered paths, ordered by risk (what's most dangerous to leave untested?)
4. Write tests for the top 5 uncovered paths
5. Identify any tests that exist but provide false confidence (testing implementation details, not behavior)
```

### 69. API Contract Test

```
Write contract tests for the API endpoint [ENDPOINT] to ensure it meets its consumer's expectations.

API definition:
- Method: [HTTP METHOD]
- Path: [PATH]
- Request body/params: [SCHEMA]
- Expected response: [SCHEMA AND STATUS CODES]

Contract testing framework: [PACT / SPRING CLOUD CONTRACT / OTHER — or "suggest one for [LANGUAGE]"]
Consumer: [NAME OF THE SERVICE OR CLIENT THAT CALLS THIS]
Provider: [NAME OF THE SERVICE THAT EXPOSES THIS]

Write:
1. Consumer-side contract test (what the consumer expects)
2. Provider verification test (the provider proves it meets the contract)
3. Explain how to run these tests in CI/CD to catch breaking changes before deployment
```

### 70. Load Test Script

```
Write a load test script for [ENDPOINT OR FEATURE] using [K6 / LOCUST / GATLING / JMeter / OTHER].

Endpoint to load test:
- URL: [URL]
- Method: [METHOD]
- Headers: [HEADERS]
- Body (if POST/PUT): [BODY]
- Authentication: [MECHANISM]

Load test scenarios:
1. Baseline: [X] concurrent users for [DURATION]
2. Ramp-up: Gradually increase from [X] to [Y] users over [DURATION]
3. Spike: Instantly jump to [X] users for [DURATION], then back down

Success criteria:
- p95 response time < [THRESHOLD]
- Error rate < [X]%

Write the complete load test script including:
- Scenario setup
- Assertions
- Custom metrics to track
- Report output configuration
```

### 71. Snapshot Test Strategy

```
Design a snapshot testing strategy for the following [FRAMEWORK] component.

Component:
[PASTE COMPONENT CODE]

Snapshot framework: [JEST / STORYBOOK / OTHER]

Please:
1. Write snapshot tests for the key rendering states of this component:
   - Default/empty state
   - Populated/loaded state
   - Loading state
   - Error state
   - [ANY OTHER RELEVANT STATES]
2. Explain which props to vary in tests vs. which to keep fixed
3. Address the snapshot maintenance problem: when should I update snapshots vs. investigate a snapshot diff?
4. Identify any dynamic values (dates, IDs, random values) that will cause false failures — and how to handle them
```

### 72. Regression Test Suite Design

```
Design a regression test suite for [FEATURE/MODULE] in [LANGUAGE/FRAMEWORK] after a significant refactoring.

What was changed:
[DESCRIBE THE REFACTORING — e.g., "replaced the payment processing library," "rewrote the auth middleware," "migrated from callbacks to async/await"]

Known risks of the change:
[LIST WHAT COULD HAVE BROKEN]

Please:
1. Define the test categories needed (unit, integration, E2E — what balance?)
2. List the specific behaviors that must be verified to confirm the refactoring is safe
3. Identify the 10 highest-risk scenarios to test first
4. Write tests for the 3 scenarios you consider most critical
5. Define the acceptance criteria: what does "green" mean before we can merge?
```

### 73. Mock Server / API Stub Setup

```
Set up a mock server for [EXTERNAL API NAME] to use in development and testing of [APPLICATION].

External API:
- Base URL: [URL]
- Key endpoints used by my application: [LIST ENDPOINTS, METHODS, AND EXPECTED RESPONSES]
- Authentication: [TYPE]

Tool preference: [MSDN / JSON SERVER / WIREMOCK / PRISM / OR SUGGEST ONE]
Language: [LANGUAGE]

Provide:
1. Mock server setup and configuration
2. Mock responses for each endpoint (realistic example data)
3. How to configure my application to use the mock server vs. real API
4. A script to start/stop the mock server for development
5. How to use this mock in automated tests
```

### 74. Test Doubles Explanation and Implementation

```
Explain the difference between mocks, stubs, fakes, spies, and dummies, and show me when to use each in testing [LANGUAGE] code.

Use the following real code from my project as examples:
[PASTE CODE WITH DEPENDENCIES]

For each test double type:
1. Define it precisely
2. Show a concrete example using my code (not a theoretical example)
3. Explain when this type is the right choice

Then: write tests for [SPECIFIC FUNCTION] using the most appropriate test double for each dependency.

Framework: [TEST FRAMEWORK AND MOCKING LIBRARY]
```

### 75. Continuous Integration Test Configuration

```
Set up an automated testing configuration for a [LANGUAGE/FRAMEWORK] project in [GITHUB ACTIONS / GITLAB CI / JENKINS / CIRCLECI / OTHER].

Project details:
- Language version: [VERSION]
- Test command: [COMMAND]
- Dependencies: [HOW TO INSTALL — e.g., npm install, pip install -r requirements.txt]
- Database required: [YES — specify / NO]
- Any external services required for tests: [LIST]

Write a CI configuration file that:
1. Triggers on every push and pull request
2. Installs dependencies with caching for speed
3. Runs the test suite
4. Reports coverage (tool: [TOOL])
5. Fails the build if coverage drops below [X]%
6. Runs different test stages in parallel where possible
7. Notifies on failure via [SLACK / EMAIL / OTHER — or leave as placeholder]

Include comments explaining each configuration decision.
```

---

## Category 6: Documentation (10 Prompts)

### 76. README Generation

```
Generate a comprehensive README.md for the following [LANGUAGE/FRAMEWORK] project.

Project description: [WHAT THIS PROJECT DOES]
Repository: [GITHUB URL PLACEHOLDER]

Include:
1. Project name and one-sentence description
2. Badges: build status, coverage, version, license (placeholder links)
3. Overview: what problem does this solve and who is it for?
4. Prerequisites: what needs to be installed before setup
5. Installation: step-by-step setup instructions
6. Configuration: environment variables with descriptions and example values
7. Usage: the most common 3–5 use cases with code examples
8. API reference: brief overview linking to full docs (if applicable)
9. Running tests: how to run the test suite
10. Contributing: brief guide for contributors
11. License: [LICENSE TYPE]

Write in clean Markdown. Assume the reader is a developer unfamiliar with this project.
```

### 77. API Documentation (OpenAPI)

```
Write OpenAPI 3.0 documentation for the following API endpoints.

Endpoints:
[PASTE ROUTE DEFINITIONS OR DESCRIBE THE ENDPOINTS]

For each endpoint, document:
- Summary and description
- Request parameters (path, query, header)
- Request body schema with field descriptions and validation rules
- Response schemas for each status code (200, 400, 401, 403, 404, 422, 500)
- Authentication requirement
- At least one request/response example

Also provide:
- Info block (title, version, description)
- Server block
- Security scheme definitions
- Reusable component schemas for shared data models

Output as valid YAML.
```

### 78. Inline Code Comments

```
Add meaningful inline comments to the following [LANGUAGE] code.

Code:
[PASTE CODE BLOCK]

Comment guidelines:
1. Explain WHY, not WHAT (the code already shows what — explain the reasoning, intent, or non-obvious consequence)
2. Comment complex algorithms, non-obvious optimizations, and important business rules
3. Flag known limitations, TODOs, or workarounds with TODO/FIXME/HACK markers and a brief explanation
4. Document any "why didn't you just do X?" decisions to prevent future refactoring of intentional code
5. Remove or replace any existing comments that just restate the code

Do not add comments to straightforward code that is self-explanatory. Quality over quantity.
```

### 79. Architecture Decision Record (ADR)

```
Write an Architecture Decision Record (ADR) for the following technical decision.

Decision: [WHAT WAS DECIDED — e.g., "Use PostgreSQL instead of MongoDB for the user data store"]
Date: [DATE]
Status: [PROPOSED / ACCEPTED / DEPRECATED / SUPERSEDED]

Context:
- What is the problem or opportunity we're addressing?
- What constraints exist (team expertise, existing infrastructure, budget, timeline)?
- What alternatives were considered?

Use the ADR template format:
1. Title: ADR [NUMBER]: [SHORT NOUN PHRASE]
2. Status
3. Context: background and problem statement
4. Decision: what we decided and the key reasoning
5. Consequences: what becomes easier, harder, or different as a result of this decision (both positive and negative)
6. Alternatives considered: [ALTERNATIVE 1] — why it was rejected; [ALTERNATIVE 2] — why it was rejected

Fill in: [DECISION DETAILS], [ALTERNATIVES], [CONSTRAINTS]. Keep it concise — an ADR should be readable in under 5 minutes.
```

### 80. Onboarding Guide for New Developers

```
Write an onboarding guide for a new developer joining a [LANGUAGE/FRAMEWORK] project.

Project overview: [WHAT THE PROJECT DOES]
Team: [TEAM SIZE AND STRUCTURE]
Developer's role: [ROLE]

The guide should cover:
1. Development environment setup (step-by-step, no assumed knowledge)
2. How to run the application locally
3. How to run tests
4. Codebase orientation: where to find key files, how the project is organized
5. The most important architectural patterns used in this codebase
6. The development workflow (branching, PR, review, merge)
7. Deployment basics: how code gets to production
8. The top 5 things the new developer should know before making their first PR
9. Who to ask for help on what

Format as a numbered guide they can follow on their first day. Target reading time: 20–30 minutes.
```

### 81. Function/Module JSDoc / Docstring

```
Write complete documentation strings for the following [LANGUAGE] functions/classes.

Code:
[PASTE CODE]

Documentation format: [JSDoc / Python docstrings (NumPy / Google / Sphinx) / Rustdoc / GoDoc / Javadoc / OTHER]

For each function/method, document:
- A one-sentence summary
- Longer description if the behavior isn't immediately obvious
- All parameters: name, type, description, whether optional, default value
- Return value: type and description
- Exceptions/errors thrown and when
- Example usage (at least one)
- Any important notes about performance, thread safety, or side effects

Make the documentation precise and useful — the kind a developer is glad they read before using the function.
```

### 82. CHANGELOG Entry Writer

```
Write CHANGELOG entries for the following code changes.

Format: [KEEP A CHANGELOG / CONVENTIONAL CHANGELOG / OTHER]
Version: [VERSION NUMBER]
Release date: [DATE]

Changes to document:
[DESCRIBE OR PASTE THE CHANGES — can be git log output, PR descriptions, or a list]

Categorize changes as:
- Added: new features
- Changed: changes to existing functionality
- Deprecated: soon-to-be removed features
- Removed: now removed features
- Fixed: bug fixes
- Security: security vulnerability patches

Write clear, user-focused descriptions — not developer-internal language. Each entry should tell a user what changed and why they should care (if relevant).
```

### 83. Runbook / Incident Response Documentation

```
Write a runbook for responding to the following incident scenario.

System: [DESCRIPTION OF THE SYSTEM]
Scenario: [E.g., "The API response time p99 exceeds 5 seconds," "The background job queue is backing up," "Database CPU is at 100%"]

The runbook should include:
1. Detection: what alert fires, what dashboard to check first
2. Initial assessment (5 minutes): what information to gather immediately
3. Diagnosis: decision tree — what to check to narrow down the cause
4. Common causes and their fixes:
   - Cause A → steps to resolve
   - Cause B → steps to resolve
   - Cause C → steps to resolve
4. Escalation: when and to whom to escalate
5. Communication: what to post in the incident channel and when
6. Resolution and verification: how to confirm the issue is resolved
7. Post-incident: what to document in the post-mortem

Write in clear imperative language (do this, then do that). No ambiguity.
```

### 84. Code Review Checklist

```
Create a code review checklist for [LANGUAGE/FRAMEWORK] pull requests at [COMPANY/TEAM NAME].

The checklist should be organized by category and practical enough to actually use during a review:

1. Correctness: does the code do what it claims to do?
2. Testing: is it adequately tested?
3. Security: are there any security issues?
4. Performance: could this cause performance problems at scale?
5. Readability: will the next person understand this?
6. Error handling: are failures handled gracefully?
7. Documentation: is there sufficient documentation?
8. Architecture: does this fit the system's patterns?
9. Dependencies: are new dependencies justified?
10. Observability: can we monitor and debug this in production?

For each category, provide 3–5 specific yes/no questions a reviewer should ask. Add a "blockers vs. nits" section that clarifies which findings require changes before merge.
```

### 85. Postmortem Template

```
Write a blameless postmortem document for the following incident.

Incident summary: [BRIEF DESCRIPTION]
Date/time: [START] — [END]
Duration: [DURATION]
Impact: [USER-FACING IMPACT — number of users affected, what they experienced]
Severity: [SEV1 / SEV2 / SEV3]

Write the postmortem following this structure:
1. Executive summary (3 sentences: what happened, why, how it was resolved)
2. Timeline (format as: [TIME] — [WHAT HAPPENED])
3. Root cause analysis (use the "5 Whys" structure)
4. Contributing factors (conditions that made the incident possible)
5. What went well (what helped us detect and resolve faster)
6. What went poorly (what slowed us down or made it worse)
7. Action items: owner, description, due date (leave as [OWNER] placeholder)
8. Lessons learned

Tone: blameless and analytical. Focus on systems and processes, not individuals.
```

---

## Category 7: DevOps and Deployment (10 Prompts)

### 86. Dockerfile Creation

```
Write a production-ready Dockerfile for a [LANGUAGE/FRAMEWORK] application.

Application details:
- Language version: [VERSION]
- Entry point: [MAIN FILE OR COMMAND]
- Port: [PORT]
- Build dependencies (only needed for building): [LIST]
- Runtime dependencies: [LIST]
- Environment variables needed: [LIST WITH DESCRIPTIONS]
- Static assets or build step required: [YES/NO — describe]

Requirements:
1. Multi-stage build to minimize final image size
2. Non-root user for security
3. Proper .dockerignore guidance (list what to exclude)
4. Layer caching optimization (dependencies installed before application code is copied)
5. Health check instruction
6. Explicit version pinning on base images

Also write: a docker-compose.yml for local development that includes this service plus [DATABASE / CACHE / ANY OTHER DEPENDENCIES].
```

### 87. CI/CD Pipeline (GitHub Actions)

```
Write a GitHub Actions CI/CD pipeline for a [LANGUAGE/FRAMEWORK] application.

Application:
- Language: [LANGUAGE VERSION]
- Test command: [COMMAND]
- Build command: [COMMAND]
- Deployment target: [AWS / GCP / AZURE / HEROKU / VPS — describe]
- Docker registry: [ECR / GCR / DOCKER HUB / OTHER]
- Environments: development, staging, production

Pipeline requirements:
1. On every pull request: lint, test, build, coverage report
2. On merge to main: run all checks, build and push Docker image, deploy to staging
3. On release tag: deploy to production (with manual approval gate)
4. Secrets management: what secrets are needed and where to store them
5. Caching for dependencies and Docker layers
6. Notifications on failure

Write the complete .github/workflows/ci-cd.yml file with comments explaining each section.
```

### 88. Kubernetes Deployment Manifests

```
Write Kubernetes deployment manifests for [APPLICATION NAME].

Application:
- Container image: [IMAGE:TAG PLACEHOLDER]
- Port: [PORT]
- Environment variables: [LIST — mark which are secrets]
- Resource requirements: CPU [REQUEST/LIMIT], Memory [REQUEST/LIMIT]
- Replicas: [NUMBER] minimum, scaling to [NUMBER] maximum
- Health checks: liveness endpoint [PATH], readiness endpoint [PATH]
- Dependencies: [DATABASE / CACHE / OTHER SERVICES]

Write the following manifests:
1. Deployment with rolling update strategy
2. Service (type: ClusterIP for internal, LoadBalancer for public)
3. HorizontalPodAutoscaler (scale on CPU [X]% threshold)
4. ConfigMap for non-secret environment variables
5. Secret template (with placeholder values, instructions to populate with kubectl or external-secrets)
6. Ingress (with TLS placeholder)

Add annotations and labels following [COMPANY NAME / STANDARD] conventions.
```

### 89. Infrastructure as Code (Terraform)

```
Write Terraform configuration for [INFRASTRUCTURE DESCRIPTION].

Cloud provider: [AWS / GCP / AZURE]
Resources needed:
- [RESOURCE 1 — e.g., "VPC with public and private subnets"]
- [RESOURCE 2 — e.g., "ECS cluster with auto-scaling"]
- [RESOURCE 3 — e.g., "RDS PostgreSQL instance"]
- [RESOURCE 4 — e.g., "Application Load Balancer"]

Requirements:
1. Use Terraform modules where appropriate
2. Separate environments using workspaces or separate state files
3. All sensitive values from variables, not hardcoded
4. Output block for values needed by other configurations (e.g., DB endpoint, cluster ARN)
5. Resource tagging with environment and project name

Include:
- main.tf
- variables.tf (with descriptions and validation)
- outputs.tf
- A README snippet explaining how to initialize, plan, and apply
```

### 90. Monitoring and Alerting Setup

```
Write monitoring and alerting configuration for [APPLICATION] running on [INFRASTRUCTURE].

Monitoring stack: [PROMETHEUS + GRAFANA / DATADOG / CLOUDWATCH / NEW RELIC / OTHER]
Application: [LANGUAGE/FRAMEWORK, TYPE OF APPLICATION]
Key metrics to monitor:
- [METRIC 1 — e.g., "HTTP request rate and error rate"]
- [METRIC 2 — e.g., "Database connection pool saturation"]
- [METRIC 3 — e.g., "Background job queue depth"]
- [METRIC 4 — e.g., "Application memory usage"]

Configure:
1. Metric collection (what to instrument in the application code)
2. Alert rules for each metric (threshold, duration, severity)
3. A dashboard layout (describe panels and what each shows)
4. Runbook links for each alert
5. On-call escalation policy (PagerDuty / Opsgenie / Slack — placeholder)

Include: the instrumentation code for [LANGUAGE/FRAMEWORK] to emit the metrics.
```

### 91. Database Migration Script

```
Write a database migration for [DATABASE TYPE] to implement the following schema change.

Current schema (relevant tables):
[PASTE CURRENT SCHEMA]

Desired change:
[DESCRIBE WHAT NEEDS TO CHANGE — e.g., "Add an email_verified_at timestamp column to the users table," "Split the address field into street, city, state, and zip columns"]

Migration framework: [FLYWAY / LIQUIBASE / ALEMBIC / ACTIVE RECORD / KNEX / OTHER]
Is there existing data that needs to be migrated? [YES — describe / NO]

Write:
1. The UP migration (apply the change)
2. The DOWN migration (rollback — be explicit about data loss risks)
3. If data migration is needed: a safe data migration script that can run without locking the table
4. A verification query to confirm the migration ran correctly
5. Note any zero-downtime considerations (adding columns with defaults, index creation concurrently, etc.)
```

### 92. Docker Compose for Local Development

```
Write a docker-compose.yml for local development of [APPLICATION NAME].

Services needed:
- Application: [LANGUAGE/FRAMEWORK], port [PORT], watches for code changes
- Database: [POSTGRES / MYSQL / MONGODB / OTHER], with init script to create schema
- Cache: [REDIS / MEMCACHED — if needed]
- [OTHER SERVICE — e.g., Elasticsearch, Kafka, MailHog for email testing]

Requirements:
1. Volumes for local code (hot reload without rebuilding image)
2. Volumes for database persistence between restarts
3. Environment variable file (.env) for secrets (write a sample .env.example)
4. Health checks so services start in the right order
5. A Makefile with shortcuts: make up, make down, make logs, make test, make migrate
6. Instructions (as code comments) for first-time setup

Make it so a new developer can run `make up` and have a working local environment in under 5 minutes.
```

### 93. Nginx / Load Balancer Configuration

```
Write an Nginx configuration for serving a [APPLICATION TYPE] application in production.

Setup:
- Backend application server: [LOCATION AND PORT — e.g., "localhost:3000," "upstream app servers"]
- Domain: [DOMAIN PLACEHOLDER]
- SSL: [YES — Let's Encrypt / YES — custom cert / NO]
- Static assets: [YES — served by Nginx / NO — served by application]
- Features needed: [GZIP / RATE LIMITING / WEBSOCKET PROXY / BASIC AUTH ON STAGING / OTHER]

Write:
1. The Nginx server block configuration
2. Upstream block if load balancing multiple instances
3. SSL configuration following current best practices (TLS 1.2+, strong ciphers)
4. Security headers (HSTS, X-Frame-Options, CSP, etc.)
5. Gzip compression settings
6. Rate limiting configuration
7. Logging format

Include comments explaining non-obvious configuration choices.
```

### 94. Environment Variable Management

```
Design an environment variable management system for a [LANGUAGE/FRAMEWORK] application deployed to [ENVIRONMENT].

Environments: local development, CI/CD, staging, production

Variables I need to manage:
[LIST ALL ENV VARS WITH THEIR PURPOSE AND SENSITIVITY LEVEL — secret/non-secret]

Please design:
1. A naming convention for environment variables (consistency rules)
2. How variables are stored and injected in each environment:
   - Local: .env file + .env.example in repo
   - CI/CD: [PLATFORM] secrets
   - Staging/Production: [AWS SSM / Vault / K8s secrets / Doppler / OTHER — recommend]
3. Code to validate required environment variables at startup (fail loudly, not silently)
4. How to rotate secrets without downtime
5. An audit strategy: how to know which applications use which secrets

Provide: the validation code in [LANGUAGE] and the .env.example file.
```

### 95. Incident Response Runbook (Infrastructure)

```
Write an infrastructure incident response runbook for the following scenario.

Scenario: [E.g., "Production database CPU at 100%," "All application pods crash-looping," "AWS region outage affecting primary region"]
Infrastructure: [DESCRIBE YOUR STACK]

The runbook should be:
- Actionable: every step is a command to run or a decision to make
- Complete: a junior engineer who's never seen this system should be able to follow it
- Fast: ordered by "most likely fix first"

Include:
1. First 5 minutes: what to do immediately (communication + diagnosis)
2. Diagnosis steps with exact commands to run
3. Decision tree: IF [symptom] THEN [action]
4. The specific fix for the [NUMBER] most likely causes
5. How to verify the fix worked
6. Escalation triggers: when to wake up the database team, the CTO, etc.
7. Customer communication template

Format as a numbered checklist.
```

---

## Category 8: Learning and Exploration (5 Prompts)

### 96. Explain This Code

```
Explain the following [LANGUAGE] code to me. I am a [SKILL LEVEL: complete beginner / junior developer / mid-level developer] with [BACKGROUND: e.g., "experience in Python but not in JavaScript async patterns"].

Code:
[PASTE CODE BLOCK]

Please explain:
1. What this code does at a high level (plain English, no jargon)
2. A line-by-line (or logical block-by-block) breakdown of what each part does
3. Any concepts or patterns I should understand to fully grasp this (define them simply)
4. Why the code is written this way (what problem does this design solve?)
5. What would happen if I changed [SPECIFIC LINE OR PART] — help me build intuition

If there are industry terms, define them. If there's a simpler way to write this, show it side-by-side.
```

### 97. Compare Two Approaches

```
Compare these two approaches to solving [PROBLEM] in [LANGUAGE/FRAMEWORK].

Approach A:
[PASTE CODE]

Approach B:
[PASTE CODE]

Compare them across these dimensions:
1. Correctness: do they both solve the problem fully?
2. Performance: which is faster, and at what scale does the difference matter?
3. Memory usage: which uses less memory?
4. Readability: which is easier to understand and maintain?
5. Testability: which is easier to unit test?
6. Error handling: which fails more gracefully?
7. Idiomatic quality: which is more in line with [LANGUAGE] best practices?

Give me a recommendation: which would you choose and why? Under what circumstances would you choose the other?
```

### 98. Learning Roadmap for a Technology

```
Create a learning roadmap for [TECHNOLOGY / LANGUAGE / FRAMEWORK / CONCEPT] for someone with my current background: [DESCRIBE CURRENT SKILLS AND EXPERIENCE].

My goal: [WHAT I WANT TO BE ABLE TO BUILD OR DO WITH THIS TECHNOLOGY]
Available learning time: [HOURS PER WEEK]

The roadmap should include:
1. Prerequisites: what I need to know first (and how to know if I'm ready)
2. Phase 1 (foundation — [X] weeks): core concepts to learn first, with specific resources
3. Phase 2 (intermediate — [X] weeks): deepen and apply, with project ideas
4. Phase 3 (advanced/practical — [X] weeks): real-world patterns and production-level skills
5. For each phase: 2–3 specific, highly-rated learning resources (books, courses, docs)
6. Milestone projects: one project per phase to apply what I've learned
7. Common traps: the mistakes most people make learning [TECHNOLOGY] and how to avoid them

Be opinionated about what to learn and in what order. Don't give me a list of everything — tell me the fastest path.
```

### 99. Concept Deep Dive

```
Give me a deep technical explanation of [CONCEPT] in [LANGUAGE/SYSTEM CONTEXT].

I already understand: [WHAT YOU KNOW]
I'm confused about: [SPECIFIC ASPECT]

Explain:
1. What [CONCEPT] is and why it exists (what problem does it solve?)
2. How it works under the hood (not just what it does, but how)
3. A simple analogy that makes it click
4. A concrete [LANGUAGE] code example showing it in action
5. Common misunderstandings about [CONCEPT]
6. When to use it and when NOT to use it
7. How [CONCEPT] compares to [RELATED CONCEPT] — when would I choose one over the other?

Assume I'm a developer who learns best from concrete examples. Show me the code.
```

### 100. Career Growth Prompt for Developers

```
I'm a [CURRENT ROLE — e.g., "junior backend developer with 1 year of experience in Python and Django"] looking to grow into [TARGET ROLE — e.g., "senior engineer" or "engineering manager"].

Current strengths: [LIST 3–5 SKILLS]
Current gaps (that I know of): [LIST 3–5 GAPS]
Company context: [STARTUP / ENTERPRISE / AGENCY — team size, tech stack]

Please give me:
1. An honest assessment of what skills gap between my current level and [TARGET ROLE]
2. The 3 highest-leverage skills to develop first (most bang for my effort)
3. A 6-month action plan with specific, measurable milestones
4. How to get visibility and demonstrate growth within my current team
5. One specific project or initiative I could propose that would develop multiple skills at once
6. The non-technical skills (communication, leadership, mentorship) that matter most at [TARGET ROLE]

Be direct. Tell me what most people in my situation underestimate or avoid.
```

---

### 101. Code Kata / Practice Problem Generator

```
Generate [NUMBER] coding practice problems for a developer looking to improve their [SKILL: algorithms, system design, data structures, specific language feature] at the [BEGINNER / INTERMEDIATE / ADVANCED] level.

Focus area: [SPECIFIC TOPIC — e.g., "tree traversal," "dynamic programming," "concurrent programming in Go"]
Language: [LANGUAGE]

For each problem:
1. Problem title
2. Clear problem description with constraints
3. Example input/output (2–3 examples)
4. Difficulty level and estimated time
5. The key insight or concept that solving this teaches
6. One hint (a nudge without giving away the solution)
7. A follow-up challenge (a harder variant)

Order from easiest to hardest. Don't include the solutions — I want to work through them myself.
```

### 102. Code Review as a Learning Exercise

```
Review my code as a learning exercise. I want to understand not just what's wrong, but why — so I don't make the same mistakes again.

My skill level: [JUNIOR / MID / SENIOR]
Language: [LANGUAGE]
I'm trying to learn: [SPECIFIC CONCEPT OR PATTERN]

My code:
[PASTE CODE]

For each piece of feedback:
1. What the issue is (clear description)
2. Why it's an issue (the principle or concept this violates)
3. What the fix looks like (show corrected code)
4. A mental model or rule of thumb I can apply next time

At the end, summarize: what are the 2–3 most important lessons from this review that I should internalize? What should I read or practice to solidify them?
```

### 103. Interview Preparation — Technical Questions

```
Generate [NUMBER] technical interview questions relevant to the position: [JOB TITLE] at a [COMPANY TYPE — startup / FAANG / mid-size tech / agency] with a focus on [TECHNICAL DOMAIN — e.g., backend engineering, distributed systems, frontend performance].

For each question:
1. The question itself (exactly how an interviewer would ask it)
2. What the interviewer is really trying to assess (the underlying skill or knowledge)
3. What a strong answer looks like (key points to hit)
4. Common mistakes candidates make on this question
5. A follow-up question the interviewer might ask if the first answer is good

Balance: [NUMBER] conceptual questions, [NUMBER] coding problems (describe the problem, no solution), [NUMBER] system design questions, [NUMBER] behavioral questions relevant to technical roles.

Focus on the level: [JUNIOR / MID / SENIOR / STAFF].
```

### 104. Pair Programming Simulation

```
Act as my pair programming partner as I work through [PROBLEM DESCRIPTION] in [LANGUAGE/FRAMEWORK].

My current approach:
[PASTE YOUR CURRENT CODE OR DESCRIBE YOUR PLAN]

What I'm stuck on:
[DESCRIBE WHERE YOU'RE BLOCKED]

As my pair:
1. Don't solve it for me — ask me guiding questions that help me find the solution
2. If I'm going in the wrong direction, tell me plainly but don't take the keyboard
3. Point out potential issues you see in my current approach
4. Suggest concepts or functions I might not know about that are relevant
5. When I arrive at a solution, review it with me: what could be better? what did we learn?

Start by asking me a clarifying question about my current approach.
```

### 105. Technology Trade-off Analysis

```
Help me evaluate the trade-offs between [TECHNOLOGY A] and [TECHNOLOGY B] for [SPECIFIC USE CASE] given my context.

My context:
- Team: [SIZE, SKILL LEVEL, EXISTING EXPERTISE]
- Project: [DESCRIPTION, SCALE, TIMELINE]
- Constraints: [BUDGET, EXISTING INFRASTRUCTURE, COMPLIANCE REQUIREMENTS]
- Non-negotiables: [SPECIFIC REQUIREMENTS THAT MUST BE MET]

Analyze:
1. How each technology addresses the use case
2. Performance characteristics at [MY EXPECTED SCALE]
3. Operational complexity (hosting, maintenance, monitoring)
4. Learning curve for my team
5. Community, ecosystem, and long-term viability
6. Total cost of ownership (compute, licensing, engineering time)
7. Vendor lock-in risk

Give me a recommendation. Don't hedge — tell me what you would choose given my constraints and why. Then tell me what would need to be different about my situation for the other choice to be better.
```

---

*End of Coding Assistant AI Prompt Pack — 105 Prompts*
