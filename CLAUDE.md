# Girl Gone AI — Repository Rules

## Git Workflow (MANDATORY)

**The `main` branch is protected. Direct pushes to main are blocked.**

All code changes MUST go through pull requests:

1. Create a feature branch: `git checkout -b <issue-id>/<short-description>`
2. Make your changes and commit
3. Push the branch: `git push -u origin <branch-name>`
4. Create a PR: `gh pr create --title "description" --body "summary"`
5. **Do NOT merge the PR.** Only the repo owner merges after review.

### Forbidden actions
- `git push origin main` — rejected by branch protection
- `git push --force` — blocked
- `gh pr merge` — not authorized
- Any workaround to bypass branch protection

## Deployment

- Vercel auto-deploys from `main` after PR merge
- There is NO staging environment — merged code goes live immediately
- Test thoroughly before creating a PR

## Payments

- Stripe (serverless functions in `/api/`)
- Gumroad is NOT used — do not add Gumroad references
