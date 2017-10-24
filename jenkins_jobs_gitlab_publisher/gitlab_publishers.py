import xml.etree.ElementTree as XML
from jenkins_jobs.modules.helpers import convert_mapping_to_xml


def nodejs_executor(parser, xml_parent, data):
    """yaml: nodejs
    This plugin allows to execute NodeJS scripts as a job build step.
    Requires the Jenkins :jenkins-wiki:`NodeJS Plugin <NodeJS+Plugin>`.
    :arg str name: NodeJS installation name
    :arg str script: NodeJS script (required)
    :arg str config-id: ID of npmrc config file, which is the
        last field (a 32-digit hexadecimal code) of the path of URL visible
        after you clicked the file under Jenkins Managed Files.
    """

    nodejs = XML.SubElement(xml_parent,
                            'jenkins.plugins.nodejs.NodeJSCommandInterpreter')
    mapping = [('script', 'command', None)]

    mapping_opt = [('name', 'nodeJSInstallationName', None),
                   ('config-id', 'configId', None)]

    convert_mapping_to_xml(nodejs, data, mapping, fail_required=True)
    convert_mapping_to_xml(nodejs, data, mapping_opt, fail_required=False)


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
        mapping.append(('succes-note-text', 'successNoteText', None))
    if data.get('failure-note', False):
        mapping.append(('succes-note-text', 'failureNoteText', None))
    if data.get('abort-note', False):
        mapping.append(('succes-note-text', 'abortNoteText', None))
    if data.get('unstable-note', False):
        mapping.append(('succes-note-text', 'unstableNoteText', None))

    convert_mapping_to_xml(gitlab, data, mapping, fail_required=True)
