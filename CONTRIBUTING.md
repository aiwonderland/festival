# Contributing Guide
Thank you for your interest and support in this project! This guide will help you quickly understand how to contribute to the project and make it better together.

## Preparation before Contribution
1.  **Read Prerequisite Documents**: Please read `README.md` (Project Introduction) and `CODE_OF_CONDUCT.md` (Code of Conduct) first, and abide by the community norms.
2.  **Environment Setup**:
    - Clone the project repository: `git clone https://github.com/aiwonderland/festival.git`
    - Install dependencies: `npm install` (adjust according to the project tech stack, e.g., `pip install -r requirements.txt`)
    - Run local tests: `npm run test` (ensure the local environment is working properly)
3.  **Branch Instructions**:
    - Main branch: `main`/`master` (stable version, direct code submission to this branch is prohibited)
    - Development branch: `develop` (daily development, all PRs should be submitted to this branch)
    - Feature branch: `feature/xxx` (when developing new features, create from the `develop` branch, naming format: `feature/feature-name`)
    - Bug fix branch: `fix/xxx` (when fixing bugs, create from the `develop` branch, naming format: `fix/bug-description`)
4.  **Code Style Requirements**:
    - Follow the code formatting standards in the project (e.g., use ESLint, Prettier for formatting)
    - Add comments for core functions and complex logic to facilitate understanding by others
    - New features must be accompanied by corresponding test cases to ensure functional stability

## Common Contribution Methods and Steps
### Method 1: Submit an Issue (Report Bugs / Propose New Feature Suggestions)
1.  First check the existing Issues in the project to avoid submitting duplicate content
2.  Select the corresponding Issue template (e.g., Bug Report, Feature Request)
3.  Fill in the content as required by the template:
    - Bug Report: Specify the environment (system, version, dependencies), reproduction steps, expected results, actual results, screenshots (optional)
    - Feature Request: Explain the functional requirements, usage scenarios, and expected effects
4.  After submission, wait for a reply and discussion from the core maintainers, please do not repeatedly urge

### Method 2: Submit a Pull Request (PR, Modify Code / Improve Documentation)
1.  Fork this project repository to your own GitHub account
2.  Create the corresponding feature/fix branch from the `develop` branch of your own repository
3.  Develop and modify locally, and submit the code after completion: `git commit -m "feat: add xxx feature"` (commit messages follow the Conventional Commits specification)
4.  Push the branch to your own Fork repository: `git push origin feature/xxx`
5.  Open the GitHub repository of this project, initiate a Pull Request, and select the target branch as `develop`
6.  Fill in the PR description, explain the modified content and the problem solved (associate the corresponding Issue number, e.g., `Fix #123`)
7.  Wait for review by the core maintainers, modify the code according to the review comments until it is approved and merged

### Method 3: Improve Documentation
Project documentation (e.g., `README.md`, usage tutorials) is also an important part. You can modify typos, supplement explanations, optimize the structure through the above PR process to make the documentation clearer and easier to understand.

## Contribution Review Criteria
1.  Comply with the project's code style and specifications
2.  The modified content is consistent with the submitted Issue/PR description and has a clear purpose
3.  New features or bug fixes must pass local tests without new errors
4.  Documentation modifications must ensure accurate content and unified formatting
5.  Abide by the community code of conduct in `CODE_OF_CONDUCT.md`, no malicious submission behavior

## Notes
- If you are a first-time contributor, you can pay attention to the "good first issue" label in the project. These issues are less difficult and suitable for beginners
- If you have any questions, you can consult the core maintainers or other contributors in the community chat group