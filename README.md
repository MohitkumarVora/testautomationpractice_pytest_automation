# testautomationpractice_pytest_automation

we are doing automation on the "https://testautomationpractice.blogspot.com/"

Steps for work flow: 
- Create new ticket in Issues section with Story description
- In local create seperate branch for every issue using this format "{issue no}-{issue name using '-' instead of space in small case}"
- After working on ticket raised a NEW PR using following git command 
   - git status
   - git add <file>
   - git commit -m "commit message"
   - git push
- After then go to Pull requests section you will found new PR
- Create new PR Using following format "{issue no} {Title of PR}"
- And ones confirm then move this PR to code review. 
---------------------------------------------------------------------------------------
Language :- Python
Web Automation Tool :- Playwright
Framework :- Pytest BDD
Installed Dependencies :- 
    - pytest 
    - pytest-bdd 
    - playwright 
    - pyyaml 
    - pytest-html 
    - pytest-xdist 
    - allure-pytest
Files :-
conftest.py — fixtures for browser & page
helpers/utils.py — to load config   
pytest.ini - is a configuration file for the pytest test runner.
     - where to find your tests,
     - what options or markers to use by default,
     - how to format output,
     - and which plugins or settings are active.
