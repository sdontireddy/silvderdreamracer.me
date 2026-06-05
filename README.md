# silverdreamracer.me

Personal blog built with Pelican where Markdown files are the source of truth and deployment is automated through GitHub Actions to AWS S3.

## Content Source Model

- Blog posts and pages are authored as Markdown files under the `content/` folder.
- Pelican reads Markdown metadata (title, date, category, tags, slug, status) and renders a static site into `output/`.
- This keeps content editing simple and version-controlled while avoiding CMS hosting overhead.

## CI/CD Flow (Single Push)

A single push to the `main` branch triggers the GitHub Actions workflow:

- Workflow file: `.github/workflows/github-workflow-pelican-publish-to-s3.yml`
- Trigger: `on.push.branches = [main]`
- Build steps:
  - checkout code
  - install Python + Pelican + Markdown support
  - run `make publish` to render static pages
- Deploy steps:
  - upload generated `output/` as workflow artifact
  - download artifact in deploy job
  - configure AWS credentials
  - sync static files to S3 using `aws s3 sync`

## AWS Serving Model

- S3 hosts the static website files.
- Route 53 manages DNS records for the custom domain.
- End users access the blog through the domain configured in Route 53.

## Low-Cost Personal Site Approach

This architecture is effective for a personal site because it is static-first, automation-driven, and operationally lightweight.

Cost model in practice:

- Recurring DNS hosting cost via Route 53 hosted zone.
- Domain registration/renewal cost (separate from Route 53 hosted zone).

Related post (implementation details and rationale):

- [Host a Static Site using Pelican, Amazon S3 for less than $1](https://www.silverdreamracer.me/pelican-static-site-amazon-s3-using-githib-action-CICD.html)
