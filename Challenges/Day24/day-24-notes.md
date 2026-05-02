# Day 24 – Advanced Git

## Fast-forward merge

A fast-forward merge happens when the main branch has no new commits and Git simply moves the pointer forward.

## Merge commit

Git creates a merge commit when branches have diverged (both have new commits).

## Merge conflict

Occurs when the same line is modified in two branches. Git cannot decide which one to keep.

---

## Rebase

Rebase moves your branch commits on top of another branch.

### Difference from merge

* Merge → keeps history with branches
* Rebase → creates linear history

### Why not rebase shared commits?

Because it rewrites history and breaks collaboration.

### When to use?

* Rebase → clean history
* Merge → safe collaboration

---

## Squash merge

Combines multiple commits into a single commit.

### Trade-off

* Clean history but loses commit details

---

## Stash

Temporarily saves uncommitted work.

### pop vs apply

* pop → apply + delete stash
* apply → apply only

### Use case

Switch tasks without committing incomplete work.

---

## Cherry-pick

Copies a specific commit from one branch to another.

### Use case

Apply hotfix without merging full branch

### Risk

Can cause duplicate commits or conflicts
