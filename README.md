# Confirmit SOAP for Python

## Pre-requisites

* `git` should be installed
* `miniconda` (or anaconda) should be installed for creating virtual environments
* must use `bash` or any shell manager app (ConEmu/Cmder)

## Instructions

* Clone this repo `https://gitlab.com/rnssi/rnd/confirmit-soap.git`

  ```bash
  # Create folder structure in your desktop
  mkdir -p ~/Desktop/gitlab.com/rnssi/rnd
  
  # cd into the newly created folder
  cd ~/Desktop/gitlab.com/rnssi/rnd
  
  # clone the repo
  git clone https://gitlab.com/rnssi/rnd/confirmit-soap.git
  
  # cd into the repo folder
  cd confirmit-soap
  ```

* Create the virtual environment

  ```bash
  conda env create -f conda-env.yml
  source activate rnd-confirmit-soap
  # to exit out of the virtual environment, execute this command
  # source deactivate
  ```

  * This will create a virtual environment named `rnd-confirmit-soap` that has all the requirements
  * To list all available virtual environments, you can execute this command:

    ```bash
    conda env list
    ```

* Open this repo in VSCode
* Please refer to this link for all Confirmit WebService classes

  [https://extranet.confirmit.com/webdocs/html/8cc9b61e-fc32-c799-a5aa-2f49555824df.htm](https://extranet.confirmit.com/webdocs/html/8cc9b61e-fc32-c799-a5aa-2f49555824df.htm)

## TODO

* [x] Add `LogOn` class methods
* [x] Add `Authoring` class methods
* [x] Add `SurveyData` class methods
* [x] Add `TaskManagement` class methods
* [x] Add `QuotaManagement` class methods
* [x] Add `SurveyDeployer` class methods
* [x] Add `DataTransfer` class methods
* [x] Add `DatabaseDesigner` class methods
* [x] Add `SampleManagement` class methods
* [x] Add `PanelCredit` class methods
* [x] Add `CommunityPanel` class methods
* [x] Add `Capi` class methods
