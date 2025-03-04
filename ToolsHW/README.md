### Clean Code Tools Assignment (8%)

- **Objective:**  
  Refactor the code in `ToolsHW/hw.py` following Clean Code principles and integrate SonarQube to assess code quality.

- **Instructions & Steps:**  
  1. **Refactor `hw.py`:**  
     - The program should compute `1 * 1` and, if the result is correct, play a video.
     - Standardize the code style (follow PEP 8 guidelines).
     - Remove unnecessary variables, functions, and duplicate code.
     - Simplify conditional structures and ensure function names are meaningful.
  2. **Integrate SonarQube for Code Quality Testing:**  
     - **Deploy SonarQube Locally:**  
       - Run the command:  
         ```bash
         docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community
         ```
       - Access SonarQube via [http://localhost:9000](http://localhost:9000) and log in using username and password: `admin`.
     - **Generate and Run Scanner Command:**  
       - Follow the manual setup: “Manually -> Set Up -> Locally -> Generate -> Choose Other.”
       - Copy the generated command (similar to below) and run it in your project directory:  
         ```bash
         sonar-scanner.bat -D"sonar.projectKey=dfs" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=your_token"
         ```
       - Consult the [SonarQube Scanner Documentation](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner/) if needed.
     - **Analyze and Improve:**  
       - Review the SonarQube report for bugs, code smells, and duplicate code.
       - Further improve your code based on the report.
  
- **Grading Criteria:**  
  - SonarQube Analysis: 4%  
  - Achieving a grade of A or above: 4%

- **Submission Requirements:**  
  Commit and push your refactored `hw.py` along with the SonarQube integration setup to your repository.