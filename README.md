# CICD_pipeline
Learning to build CI CD pipeline using Github Actions

**uses**: Specifies the trigger for this workflow. This example uses the push event, so a workflow run is      triggered every time someone pushes a change to the repository or merges a pull request. This is triggered by a push to every branch; for examples of syntax that runs only on pushes to specific branches, paths, or tags, see "Workflow syntax for GitHub Actions."

**check-bats-version:*** Defines a job named check-bats-version. The child keys will define properties of the job.

**runs-on**: Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. For syntax examples using other runners, see "Workflow syntax for GitHub Actions"

**steps:** Groups together all the steps that run in the check-bats-version job. Each item nested under this section is a separate action or shell script.


**jobs**: Groups together all the jobs that run in the learn-github-actions workflow.

**uses: actions/setup-python@v5**
    **with:**
        **python-version: '3.9'**

          This step uses the actions/setup-node@v4 action to install the specified version of the Node.js. (This example uses version 20.) This puts both the node and npm commands in your PATH.