# Reset & Revert

git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1

git revert <commit-hash>

# Recovery

git reflog

# Comparison tools

git log --oneline --graph --all