# Card Genius Backend
This is the backend for the Card Genius app, built using FastAPI.

## Prerequisites
- [Python 3.13](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## To install:
[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.

## Developers' Guide
### Initial setup
0. [Clone the repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) if you haven't yet
1. Navigate to the BackEnd directory
2. Get the most recent changes from Github: `git pull`
3. Don't work on the main branch. You can use the dev branch or create a specific branch for the feature you are working on: `git checkout dev` or `git checkout -b $BRANCH_NAME`

### To get new changes into your branch
(These instructions assume you're working on the "dev" branch)
1. Switch to main: `git checkout main`
2. Get the most recent version of main: `git pull`
3. Switch to your branch: `git checkout dev`
4. Incorporate the changes from main into your branch: `git merge main` 

### Workflow
0. Application code goes in the src/card_genius/ directory, tests (if we write any) go in the test/ directory, configuration files (like pyproject.toml) go in the root directory
1. When you have a change you want to keep, enter `git add .` (to stage all changes) or `git add $FILENAME` (to stage a specific file or directory)
2. Then enter `git commit -m "commit message"` to finalize the changes locally. By convention, commit messages start with a present-tense verb, e.g. "Update readme"
3. To push changes to the repo, enter `git push origin $BRANCH_NAME`. This sends the changes to Github. Usually we don't push on each commit but when we've finished a session or some discrete unit of progress.
4. Navigate to the [Github repo](https://github.com/cardgenius25/BackEnd) in your browser. There should be a banner with green button telling you there have been changes and asking if you want to open a pull request. Click it. (Sometimes the banner doesn't show up, in which case you can open a PR manually by going to the Pull Requests tab, clicking New Pull Request, then clicking your branch name)
5. Now your PR is open. Please do not click the Merge Pull Request button, as this will merge it with main (assuming there are no conflicts). Try to get someone else in the project to review your PR first. You can add a reviewer via the Reviewers tab on the page of your PR, or you could just contact someone through Disco etc.

### About uv
[uv](https://docs.astral.sh/uv/) is somewhat new, but is being very quickly adopted all over the Python world. It automatically handles lots of aspects of project management that used to have to be done manually using a bunch of different tools. For example, it will handle dependencies and managing the virtual environment.
- To add a dependency: `uv add $DEPENDENCY_NAME`
- To remove a dependency: `uv remove $DEPENDENCY_NAME`
These commands update the pyproject.toml file, which is the main project configuration file.
To run things in a uv project, you need to type `uv run` before any commands. So instead of typing `python main.py`, you would type:
```uv run python main.py```
Then uv will run main.py using the dependencies and Python version specified in pyproject.toml.

## To run the FastAPI backend:
1. ```uv run fastapi dev src/card_genius/main.py```
2. Ctrl-click http://127.0.0.1:8000 (or other default localhost url) in your terminal to open in a browser
3. Go to http://127.0.0.1:8000/docs to see the autogenerated API documentation.


## To run agent.py locally using ollama:
1. Install [ollama](https://ollama.com/)
2. Start the ollama server: `ollama serve`
3. In a separate terminal, get the llama3.2 model (recommended because relatively lightweight): `ollama fetch llama3.2`
4. Run agent.py: `uv run python src/card_genius/agent.py`
5. If all goes well you should see the following output:```city='London' country='United Kingdom'
Usage(requests=1, request_tokens=176, response_tokens=21, total_tokens=197, details=None)```