# Group - BlitzwerQ

This repository contains our group work for Lab 04. The activity focused on collaborative Git and GitHub workflows, pytest fixtures, shared test files, commits, pushes, pull operations, and resolving merge conflicts as a team.

---

## Team Contributions

Each member worked through their own GitHub account and contributed a separate part of the testing activity.

## Team Contributions

The project was completed collaboratively in the following order. The repository was first prepared with the core bank module and initial tests, followed by the shared pytest fixture and additional test files contributed by the remaining members.

| Member | Student ID | GitHub Username | Main Contributions |
|---|---|---|---|
| HEIN THANT | 6705142030 | 6705142030-design | Repository setup, `bank.py`, `.gitignore`, `test_deposit.py` |
| HAN HTOO THWIN | 6705142005 | Hinod3suuu | `conftest.py` shared fixture |
| SWAN HTET NAING | 6705142004 | AchiLeo-shn | `test_teardown.py` |
| AUNG KHANT NAING | 6705142003 | AungKhantNaing0 | `test_shared.py` |
| MIN MAUNG THEIN | 6705142023 | MinMaungThein | `test_withdraw.py` |

---

## Collaboration Process

We worked on one shared GitHub repository instead of creating separate forks. Each member cloned the repository, configured their own Git identity, worked on their assigned file, tested the project with pytest, and committed their changes using their own GitHub account.

Before pushing new work, we used `git pull` to retrieve the latest changes made by other members. This helped us keep our local repositories synchronized while working on the same project.

During the activity, we also updated this README collaboratively to record each member's contribution and document what we learned from the Git workflow.

---

## Push Permission Issue

One of our pushes was initially rejected because the team member did not yet have permission to push changes to the shared repository.

The repository owner added the member as a collaborator, the invitation was accepted, and the commit was then pushed successfully. This showed us that having a local copy of a repository does not automatically give a user permission to modify the remote repository.

---

## Our Merge Conflict

During our collaboration, more than one member edited the same section of `README.md` before pulling the latest changes from the shared repository. Because the changes affected the same area differently, Git could not automatically determine which version should be kept.

Git displayed conflict markers similar to the following:

```text
<<<<<<< HEAD
Our local README changes
=======
Changes pulled from the shared repository
>>>>>>> origin/main
```

We reviewed both versions instead of simply choosing one side. We kept the valid contributions from each member, combined the correct information into the final README, removed the conflict markers, and saved the resolved file.

After resolving the conflict, the corrected README was committed and pushed back to the shared repository.

---

## Reflection Questions

### 1. Why was your push rejected, and how did you fix it?  
**Member 1 - HEIN THANT (6705142030)**

The push was rejected because the team member did not yet have permission to push changes to the shared repository. We fixed this by adding the member as a collaborator, accepting the invitation, and then pushing the commit again.

### 2. Why could Git not resolve the README conflict automatically?  
**Member 2 - HAN HTOO THWIN (6705142005)**

Git could not resolve the conflict automatically because multiple members changed the same part of the README file differently. Since Git could not determine which version should be kept, the conflict had to be reviewed and resolved manually.

### 3. What is the difference between committing and pushing?  
**Member 3 - SWAN HTET NAING (6705142004)**

Committing saves changes to the local Git repository and records them in the project history. Pushing uploads those commits to the shared GitHub repository so other team members can access them.

### 4. How do fixtures reduce duplicated setup code in tests?  
**Member 4 - AUNG KHANT NAING (6705142003)**

Fixtures allow common setup code to be defined once and reused across multiple tests. This reduces repetition and makes the test files easier to maintain and update.

---

## Final Collaboration Review

**Member 5 - MIN MAUNG THEIN (6705142023)**

The collaborative workflow showed why pulling the latest changes before editing and pushing is important when several people are working in the same repository. It also demonstrated how Git tracks each member's work separately while allowing everyone to contribute to one shared project.

The merge conflict was useful for understanding how Git handles competing changes. Instead of automatically choosing one version, Git required us to review the changes and decide what should remain in the final file.

---

## Git Contribution Summary

The following output from `git shortlog -sn` shows the commits made by each contributor:

```text
10  HEIN THANT
5   AungKhantNaing0
4   Hinod3suuu
3   AchiLeo-shn
3   MinMaungThein
```

All five members contributed through their own Git identities and made at least three commits to the shared repository.

---

## Repository Contents

- `bank.py` - Bank account implementation used by the tests.
- `conftest.py` - Shared pytest fixtures.
- `test_deposit.py` - Tests for deposit behavior.
- `test_withdraw.py` - Tests for withdrawal behavior.
- `test_teardown.py` - Tests demonstrating fixture setup and teardown.
- `test_shared.py` - Tests using the shared fixture.
- `README.md` - Team contributions, collaboration documentation, conflict resolution, and reflections.

---

## Group - BlitzwerQ

Lab 04 completed collaboratively using Git, GitHub, and pytest.