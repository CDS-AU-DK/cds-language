# Language Analytics - Spring 2021

This repository contains all of the code and data related to the Spring 2021 module _Language Analytics_ as part of the bachelor's tilvalg in [Cultural Data Science](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/) at Aarhus University.

This repository is in active development, with new material being pushed on a weekly basis. 

## Technicalities

For the sake of convenience, I recommend using our own JupyterHub server for development purposes. The first time you use the server, you'll need to create your own version of the repo and install relevant dependencies in a virtual environment:

```bash
git clone https://github.com/CDS-AU-DK/cds-language.git
bash ./create_lang_venv.sh
```

From then on, every time you use the server, make sure you update the repo and install any new dependencies:

```bash
cd lang101
git pull
bash ./create_lang_venv.sh
```

## Repo structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| A folder to be used for sample datasets that we use in class.
```notebooks``` | This is where you should save all exploratory and experimental notebooks.
```src``` | For Python scripts developed in class and as part of assignments.
```utils``` | Utility functions that are written by me, and which we'll use in class.


## Class times

This class takes place on Wednesday mornings from 8-12. Teaching will take place on Zoom, the link for which will be posted on Slack.

## Course overview and readings

A detailed breakdown of the course structure and the associated readings can be found in the [syllabus](syllabus.md). Also, be sure to familiarise yourself with the [_studieordning_](https://eddiprod.au.dk/EDDI/webservices/DokOrdningService.cfc?method=visGodkendtOrdning&dokOrdningId=15952&sprog=en) for the course, especially in relation to examination and academic regulations.

## Contact details

The instructor is me! That is to say, [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html).

All communication to you will be sent _both_ on Slack _and_ via Blackboard. If you need to get in touch with me, Slack should be your first port-of-call! 

