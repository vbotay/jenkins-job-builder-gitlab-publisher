import xml.etree.ElementTree as XML
from jenkins_jobs.modules.helpers import convert_mapping_to_xml


def gitlab_notifier(registry, xml_parent, data):
    """yaml: gitlab-notifier
    Set build status on GitLab commit.
    Requires the Jenkins :jenkins-wiki:`GitLab Plugin <GitLab+Plugin>`.

    :arg str name: Name of build to show in GitLab (default 'jenkins')
    :arg bool unstable-as-success: Mark unstable build as success if true
                                   (default false)
    Example:

    .. literalinclude:: /../../tests/publishers/fixtures/gitlab-notifier.yaml
       :language: yaml
    """
    gitlab = XML.SubElement(
        xml_parent,
        'com.dabsquared.gitlabjenkins.publisher.GitLabCommitStatusPublisher'
        )

    mapping = [('build-name', 'name', None)]
    convert_mapping_to_xml(gitlab, data, mapping, fail_required=False)



def gitlab_vote(registry, xml_parent, data):
    """yaml: gitlab-vote
    Set vote for build status on GitLab merge request.
    Requires the Jenkins :jenkins-wiki:`GitLab Plugin <GitLab+Plugin>`.
    """
    XML.SubElement(
        xml_parent,
        'com.dabsquared.gitlabjenkins.publisher.GitLabVotePublisher')

def gitlab_message(registry, xml_parent, data):
    """yaml: gitlab-message
    Add note with build status on GitLab merge request.
    Requires the Jenkins :jenkins-wiki:`GitLab Plugin <GitLab+Plugin>`.
    
    :arg bool failure-only: 
    
    :arg bool success-note:
    :arg bool failure-note:
    :arg bool abort-note:
    :arg bool unstable-note:
    
    :arg str success-note-text:
    :arg str failure-note-text:
    :arg str abort-note-text:
    :arg str unstable-note-text:

    Example:

    .. literalinclude:: /../../tests/publishers/fixtures/gitlab-message.yaml
       :language: yaml
    """
    gitlab = XML.SubElement(
        xml_parent,
        'com.dabsquared.gitlabjenkins.publisher.GitLabMessagePublisher'
        )

    mapping = [('failure-only', 'onlyForFailure', False),
               ('success-note', 'replaceSuccessNote', False),
               ('failure-note', 'replaceFailureNote', False),
               ('abort-note', 'replaceAbortNote', False),
               ('unstable-note', 'replaceUnstableNote', False)]

    if data.get('success-note', False):
        mapping.append(('success-note-text', 'successNoteText', ''))
    if data.get('failure-note', False):
        mapping.append(('failure-note-text', 'failureNoteText', ''))
    if data.get('abort-note', False):
        mapping.append(('abort-note-text', 'abortNoteText', ''))
    if data.get('unstable-note', False):
        mapping.append(('unstable-note-text', 'unstableNoteText', ''))

    convert_mapping_to_xml(gitlab, data, mapping, fail_required=True)
