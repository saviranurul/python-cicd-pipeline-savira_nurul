node {
    withDockerContainer('python:2-alpine') {
        stage('Build') {
            checkout scm
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    withDockerContainer('qnib/pytest') {
        stage('Test') {
            checkout scm
            sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            junit 'test-reports/results.xml'
        }
    }
    stage('Deliver') {
        checkout scm
        input message: 'Want to continue on the delivery process?'
        sh "docker run --rm -v /var/jenkins_home/workspace/python-cicd-pipeline-savira_nurul/sources:/src cdrx/pyinstaller-linux:python2 'pyinstaller -F add2vals.py'"
        archiveArtifacts artifacts: 'sources/add2vals.py', followSymlinks: false
        sh "docker run --rm -v /var/jenkins_home/workspace/python-cicd-pipeline-savira_nurul/sources:/src cdrx/pyinstaller-linux:python2 'rm -rf build dist'"
        sleep time: 1, unit: 'MINUTES'
    }
}