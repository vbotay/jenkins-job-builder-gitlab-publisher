from setuptools import setup

setup(
    name='jenkins-job-builder-gitlab-publisher',
    version='0.0.1',
    description='Jenkins Job Builder Gitlab Publishers',
    url='https://github.com/vbotay/jenkins-job-builder-gitlab-publisher.git',
    author='Vasily Gorin',
    author_email='vasilygorin@gmail.com',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.publishers': [
            'gitlab-notifier-plugin = '
            'jenkins_jobs_gitlab_publisher.gitlab_publishers:gitlab_notifier',
            'gitlab-vote = '
            'jenkins_jobs_gitlab_publisher.gitlab_publishers:gitlab_vote',
            'gitlab-message = '
            'jenkins_jobs_gitlab_publisher.gitlab_publishers:gitlab_message'
        ]
    },
    packages=['jenkins_jobs_gitlab_publisher'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])