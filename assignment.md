# Week 10 Exercise

**Green Run Screenshot:**

<img width="1670" height="614" alt="image" src="https://github.com/user-attachments/assets/e5516a1a-9e44-4c77-a391-df743da1d2a8" />

This run was triggered when the ci.yml file was pushed, so it was indirectly triggered by me.

**My Prediction of Which Test Would Fail:** test_boundary_exactly_24_hours_is_free() - **Was I Right?:** Yes

**Red Run Screenshot:**

<img width="1679" height="885" alt="image" src="https://github.com/user-attachments/assets/446c9556-7c56-4279-a8d7-2fb406c5d78b" />

**Green-Again Screenshot:**

<img width="1674" height="665" alt="image" src="https://github.com/user-attachments/assets/72ca5388-f837-4350-a557-5e7ab96e7bb8" />

If there was no pipeline, this bug could have been missed in manual testing as it will only show up for 24, and could have resulted in clients being charged when they shouldn't be - this costs clients' trust as well as developer time to now fix that bug. 

**AI Check & Reflection:**

*AI Response:*
```yml
name: CI

on:
  push:
  pull_request:

permissions:
  contents: read

concurrency:
  group: ci-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test:
    name: Test (Python 3.12)
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      # 1. Get repository code
      - name: Checkout repository
        uses: actions/checkout@v4

      # 2. Set up Python and cache pip dependencies
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: pip
          cache-dependency-path: requirements.txt

      # 3. Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements.txt
          python -m pip install pytest ruff

      # 4. Check code quality
      - name: Lint with Ruff
        run: ruff check .

      # 5. Run tests
      - name: Run tests
        run: pytest -v --tb=short
```

*AI Check:*

One improvement the AI suggested: To be triggered upon a pull request as well as a push, which automates testing before a branch is merged.

The gate in its version: Ruff, PyTest

Would I merge its version? Yes, I would. I think the quality checks, configuration, and triggers look at a higher level of relevant detail and would constitute a more well-rounded workflow.

*Reflection:*
- Why is a pipeline that skips its tests worse than no pipeline?

  With no pipeline, there will still be manual testing done and various cases will be looked at by an individual. However, with an automated pipeline, we're losing some of that visibility. If a pipeline looks like it is successful, a team may go ahead and push that code to production - but with skipped tests, that 'success' can be misleading. It is possible that the skipped tests would have succeeded and everything is working correctly. However, it could also be that those test would have failed and some bug that the team thought they accounted for will now show up in production. 
- What did the red run teach you that the green run could not?

  The red run taught me how to actually look into the code, what was failing, and see what it looks like when part of a pipeline does fail. The green run can only tell us that the pipeline was successful - this is great, but when it comes to production level code, I want to be prepared for the harder scenarios as well. The workflow pointed out exactly where the failure in the tests occurred, and it overall just helped me see how I would go about debugging an application in the future. 
- One rule you will follow when a pipeline guards code you care about.

  When a pipeline guards code I care about, I will make sure that no tests were skipped in a successful pipeline run. 
