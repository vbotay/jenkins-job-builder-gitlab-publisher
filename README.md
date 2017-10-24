# jenkins-job-builder-gitlab-publisher
Plugin for Jenkins Job Builder which extends gitlab publishers


## NB
-
## Installation
Install it in additional to installed [Jenkins Job Builder](https://github.com/openstack-infra/jenkins-job-builder)
```bash
pip install -e git+git://github.com/vbotay/jenkins-job-builder-gitlab-publisher.git#egg=jjb-gitlab-publisher
```
Or specify the package in requirements.txt if you install JJB from sources

## Usage
### Gitlab Notifier
Originaly [JJB](https://github.com/openstack-infra/jenkins-job-builder) has implementation of this publisher,
but it doesn't provide to specify a build name to show on Gitlab

* **name**(*optional*) - name of the build wich will be shown on GitLab

Gitlab Message Example:
```yaml
publishers:
  - gilab-notifier:
      name: "My Jenkins Check"
  - gitlab-vote
  - gitlab-message
```

### Gitlab Vote
Jenkins will set a vote on merge request in GitLab

Example:
```yaml
publishers:
  - gitlab-vote
```

### Gitlab Message
This publisher provides Jenkins to comment merge request on GitLab

* **failure-only**(*optional*) - if set, Jenkins will comment merge request only if build failed

* **success-note**(*optional*) - comment on success (default, false)
* **failure-note**(*optional*) - comment on failure (default, false)
* **abort-note**(*optional*) - comment on abort (default, false)
* **unstable-note**(*optional*) - comment on unstable (default, false)

In case of any option above set to true, user can specify the appropriate option below.
Otherwise they will be ignored
* **success-note-text**(*optional*) - text of comment for publishing
* **failure-note-text**(*optional*) - text of comment for publishing
* **abort-note-text**(*optional*) - text of comment for publishing
* **unstable-note-text**(*optional*) - text of comment for publishing

Example:
```yaml
publishers:
  - gitlab-message:
      success-note: true
      failure-note: true
      abort-note: true
      unstable-note: true
      success-note-text: "SUCCESS"
      failure-note-text: "FAILURE
      abort-note-text: "Job was aborted"
      unstable-note-text: "Unstable build"      
```