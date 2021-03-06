# Chef-Workstation-Installer-Script

Python Script that assists in installing Chef Workstation on Mac OS.

## Requirements 

- **Git**
  - Must be installed and configured, link provided:
  https://git-scm.com/download/mac
  
  - To configure for the first time enter the following commands with your information that you signed up for GitHub.com with:
  
  `git config --global user.name "Your Name Here"`
  
  `git config --global user.email "your_email@youremail.com"`
  
  - If you don't know if you have it and you are on a mac just type `git version` into terminal and if it comes back with a version you already have it.

- **Chef Server**
- **Chef Server Login and Password**
  - Must log into *YOUR* account on the Chef Server when prompted or you will reset whatever user's credentials you are signed in with.

## Instructions

1. Download the repo to your machine
  - If it is zipped, unzip it by double clicking it.
  
2. Open Terminal and `cd` to the path the repo was saved.

   `cd Downloads/Chef-WorkStation-Installer-Script-master`
   
3. Now change your url in the script (line 9) to reflect your Chef Server's IP.

  `vi Chef-WorkStation-Installer-Script-master`
  
4. Make sure you have met all the Requirments above before the next step.

5. In terminal run the script Chef-Workstation-Installer-Script.py

   `python Chef-Workstation-Installer-Script.py`
  
6. Follow the prompts and enter yes or no for your answers.

## License & Authors

**Author:** Steve Christian
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
