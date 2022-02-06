Title: Gitlab Scripts for automatic release notes(CHANGELOG.md) generation
Date: 2022-02-05 02:53
Author: sdontireddy
Category: CI/CD
Tags: GIT, Pipeline , CI/CD , Release Notes , Changelog.md
Slug: gitlab-generate-release-notes-automatically-on-the-tag-creation-CICD
Status: published

# Gitlab Sample Script to generate Release Notes(CHANGELOG.md) autotmatically as part of the CI/CD pipeline

Very Common Usecase is genrate Release Notes(CHANGELOG.md) automatically.
Below use case here has two jobs underr release-creation stage. One to generate CHANGELOG.md and other to generate release automatically.
 i.e Whenever a tag is created on any project a release with corresponding release notes , artifacts are generated automatically.


```

stages:
  - build
  - .......
  - release-creation
  
  
prepare:
  stage: release-creation
  allow_failure: true
  image:
    name: docker.repo.frg.tech/alpine/git:latest
    entrypoint: [""]
  script:
    - echo RELEASE_TAG=$CI_COMMIT_TAG >> variables.env
    - echo '## Changelog' >> CHANGELOG.md
    - git tag -l -n9 $CI_COMMIT_TAG >> CHANGELOG.md
    - echo '## Commits' >> CHANGELOG.md 
    - git log --pretty="- %s (%h)" $(git tag --sort=-creatordate | head -2)...$(git tag --sort=-creatordate | head -1) >> CHANGELOG.md
    - echo '## Merges' >> CHANGELOG.md 
    - git log --merges --pretty="- %s (%h)" $(git tag --sort=-creatordate | head -2)...$(git tag --sort=-creatordate | head -1) >> CHANGELOG.md
    - echo '## AUTHORS' >> CHANGELOG.md
    - git log --pretty="- %an%n- %cn" $(git tag --sort=-creatordate | head -2)...$(git tag --sort=-creatordate | head -1) | sort | uniq >> CHANGELOG.md
  artifacts:
    paths:
      - CHANGELOG.md
  only:
    - tags
    
release_creation:
  stage: release-creation
  allow_failure: true
  image: docker.repo.frg.tech/gitlab-org/release-cli:latest  
  only:
    - tags
  needs:
    - job: prepare
      artifacts: true
  artifacts:
    paths:
    - CHANGELOG.md
    expire_in: never
  release:
    name: $CI_COMMIT_TAG
    description: CHANGELOG.md
    tag_name: $CI_COMMIT_TAG 
    
```

Important point to note here is - we are generate CHANGELOG,md and during release , pls pay attention to the description where we are directly specificying the CHANGELOG.md file as the descriptions

```
  release:
    name: $CI_COMMIT_TAG    
    description: CHANGELOG.md
```

**Notes**:
>> Release notes description from official documentation
Every release has a description. You can add any text you like, but we recommend including a changelog to describe the content of your release. This helps users quickly scan the differences between each release you publish.


> This has the following behavior of the **description** filed
> if the description contains spaces between words: it is treated as a string,
> if the description is a single word and is a file or a symlink to a file inside $CI_PROJECT_DIR: the file's contents will be read as the release description,
> if the description is a single word and is a file or a symlink to a file outside $CI_PROJECT_DIR, or if the target file does not exist: it is treated as a string.

Please see this [link](https://gitlab.com/gitlab-org/release-cli/-/merge_requests/67) for more details
