# Job Openings 🎓💼

Hello and welcome! 🌟 This is a list of awesome full-time job / internship openings. We've got jobs in Software Engineering, Quantitative Analysis, Product Management, and more. Check them out!

**Make Git Watch for All Activity** 🔔: To stay up-to-date with the latest job postings and contributions, ensure you have Git set up to watch this repository. You can do this by clicking the "Watch" button at the top right of this repository page and selecting "Watching." This will notify you of new job openings and any updates made by the community.

🤝 **We welcome contributions from the community!** Feel free to submit a pull request, and we'll incorporate your updates.

***This project was inspired from [Daniel Maya](https://github.com/ReaVNaiL)***

## Table of Contents
2. [Explore Job Listings ⬇️](README.md#jobs)
3. [Useful Resources 🎯](README.md#resources)
4. [How to Get Involved 💬](Contribution.md)

## Running the job scrapper
This provides instructions on how to run the Python code that extracts job information from Lever and Greenhouse job listings.

  ### Prerequisites

  Before running the code, make sure you have the following prerequisites installed on your system:

  - Python 3.x: You can download and install Python from the official Python website (https://www.python.org/downloads/).

  - Required Python Packages: Ensure you have the necessary Python packages installed by running the following command in your terminal or command prompt:

    ```bash
    pip install requests beautifulsoup4
    ```
    ***If you getting warning while installing, add --user at the end of the command*** 

  ### Running the Code

  - **Navigate to the Code Directory**: Use the cd command to navigate to the directory where the code file is located.
    ```bash
    cd scraper
    ```
  - **Run the Code**: Execute the Python code using the following command:
    ```bash
    python job_scraper.py
    ```
  - **Review the Output**: The code will start running and display the job roles, company names, and URLs for both Lever and Greenhouse job listings. The results will be printed in the terminal or command prompt.
  - **Pagination (Optional)**: By default, the code retrieves a limited number of search results from Google. If you want to retrieve more results, you can modify the num_pages variable in the code to specify the number of pages of search results you want to fetch.
  - **Exit the Code**: You can exit the code execution by pressing Ctrl+C in the terminal or command prompt.

  ***Note: You can change search for different role by changing the search_query = 'site:lever.co OR site:greenhouse.io "Job Role"'. e.g. search_query = 'site:lever.co OR site:greenhouse.io "Associate Software Engineer"' or search_query = 'site:lever.co OR site:greenhouse.io "SDE Intern"', etc. Feel free to experiment as per your needs and don't forget to have fun.🎮***

  ***Please note that the code relies on Google search results, and the availability of job listings may vary depending on Google's search results and website changes.🍕***
## Resources

If you're seeking guidance on how to prepare for technical interviews, you might find these resources helpful:

- **[Cracking the Coding Interview](http://www.crackingthecodinginterview.com/)** by **Gayle Laakmann McDowell**:
  * A comprehensive book that provides guidance on how to prepare for technical interviews, covering essential topics like data structures, algorithms, and problem-solving techniques. It includes detailed explanations, example problems, and solutions to help you practice and excel in coding interviews.

- **[Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)** on **Educative**:
  * A comprehensive course that covers the key aspects of system design interviews. It provides a structured approach to understanding and mastering system design concepts, with interactive diagrams and real-world examples to help you prepare for system design interviews.

- **[Blind 75](https://leetcode.com/list/xi4ci4ig/)** on **LeetCode**:
  * A curated list of 75 frequently asked coding interview questions, often discussed on Blind, a popular platform for tech professionals. These questions cover a wide range of topics, including data structures, algorithms, and system design, making it a valuable resource for interview preparation.

- **Striver's DSA Playlist on YouTube**:
  * A comprehensive and well-structured playlist by **[Striver](https://www.youtube.com/watch?v=EAR7De6Goz4&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz)** covering essential topics in data structures and algorithms. This playlist is highly recommended for anyone preparing for coding interviews or looking to improve their DSA skills.


- **[Interview Guide](https://interviewguide.dev/)** by **[Nick Scialli](https://twitter.com/nas5w)**:
  * An all-encompassing website that delves into various topics like data structures, algorithms, system design, behavioral questions, and more. It also offers links to other beneficial resources and practice platforms.

- **[Resume Example](https://www.overleaf.com/latex/templates/modern-deedy/cxtjgrmpsrvh)**
  * This ATS friendly resume provides an example of an effective and well-structured resume format. It includes sections for contact information, summary or objective, work experience, education, skills, and more. You can use it as a reference to create your own professional resume. Additionally, you can view a my resume created using this format [here](https://drive.google.com/file/d/1OAmU02WNjXTY-uRYj_0d_QkcgQGNAVYr/view?usp=sharing).

- If you need personal mentorship, feel free to ping me on [LinkedIn](https://www.linkedin.com/in/azad-ali-49274a1a0/)

## For International Jobs

- **[h1bdata.info](https://www.h1bdata.info)**
  * Check if a company has sponsored H1B candidates previously.
- **[e-verify.gov](https://www.e-verify.gov)**
  * Verify if a company is e-verified, allowing for F-1 OPT STEM extension of 24 months.