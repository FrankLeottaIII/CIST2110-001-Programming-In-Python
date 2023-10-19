
### Using pip and Python Virtual Environments

#### I. Introduction to `pip` (20 mins)
   A. Explanation and Importance of `pip` (5 mins)
   B. Installing `pip` (5 mins)
   C. Basic `pip` Commands (10 mins)
      1. Installing a package: `pip install package_name`
      2. Uninstalling a package: `pip uninstall package_name`
      3. Listing installed packages: `pip list`
      4. Upgrading a package: `pip install --upgrade package_name`
   D. Hands-On Exercise (10 mins)
      - Students install a simple package (like `requests`) and use it to make a basic HTTP request.

#### II. Introduction to Virtual Environments (20 mins)
   A. Why Virtual Environments are Needed (5 mins)
   B. Creating a Virtual Environment (5 mins)
      - Using `venv`: `python -m venv myenv`
   C. Activating and Deactivating the Virtual Environment (5 mins)
      - Windows: `myenv\Scripts\activate`
      - Unix/MacOS: `source myenv/bin/activate`
      - Deactivating: `deactivate`
   D. Using `pip` within a Virtual Environment (5 mins)
   E. Hands-On Exercise (10 mins)
      - Students create a virtual environment, activate it, install a package, and use it within the environment.

#### III. Practical Application: Developing a Simple Project using `pip` and Virtual Environments (40 mins)
   A. Explanation and Setup of the Practical Task (10 mins)
      - Students will create a simple web scraper using `BeautifulSoup`.
   B. Step-by-Step Guide Through the Project (15 mins)
      1. Creating a virtual environment and activating it.
      2. Installing `requests` and `beautifulsoup4` using `pip`.
      3. Writing a simple script to scrape and print the title of a webpage.
   C. Independent Working Time & Troubleshooting (10 mins)
      - Students work on their projects, instructor helps troubleshoot issues.
   D. Review and Discussion of the Task (5 mins)

#### IV. Best Practices and Additional Tips (5 mins)
   A. Keeping Dependencies Organized with a `requirements.txt` file.
   B. Ignoring virtual environment folders in version control using `.gitignore`.

#### V. Q&A and Wrap-Up (5 mins)
   A. Recap of Key Points
   B. Open Floor for Questions

### Example for Section III:

#### III-B-3. Writing a Simple Web Scraper

```python
# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Sending an HTTP request
url = 'https://www.example.com'
response = requests.get(url)

# Parsing the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting and printing the title of the webpage
page_title = soup.title.string
print(f'Title of the webpage: {page_title}')
```
