IPyNotebookReport
=================

## What it is

It's my IPython notebook latex template for nbconvert.

## Getting started

Clone this repository.
Run ipython notebook

    ipython notebook

Create your ipython notebooks. When you are happy with the result, run

    ipython nbconvert

in the same folder. A .tex file should be generated. You should be able to generate the PDF from there directly (all dependencies should be there already).

## Configuration

To change the homework title, author, date and class, modify:

```latex
\newcommand{\hmwkTitle}{Exercise 1.1}
\newcommand{\hmwkSubTitle}{}
\newcommand{\hmwkDueDate}{\today}
\newcommand{\hmwkClass}{16.S499 Fundamentals of Planning Algorithms}
\newcommand{\hmwkAuthorName}{Enrique Fernandez}
\newcommand{\hmwkAuthorEmail}{efernan@mit.edu}
```

in ```latex_homework.tplx```. If you want to prevent certain cells from being included in the latex document, add ```{"homeworkReport": {"showCell": "nothing"}}``` to the metadata of each cell to be omitted.

## How this works

The configuration file ```ipython_nbconvert_config.py``` tells nbconvert to convert every ipython notebook (.ipynb) to latex using template ```latex_homework```. The ```latex_homework``` template inherits from ```efernan_article.tplx```. This is where the main LaTeX template is defined.

Before converting the file, the notebook is preprocessed with ```efernan_preprocessor.py```. This file iterates through every cell looking for the metadata ```{"homeworkReport": {"showCell": "nothing"}}```. If the metadata is found, the cell is removed and not included in the latex report.


## Modifying the template

Modify file ```efernan_article.tplx```.
For inspiration, look at the [nbconvert examples repository](https://github.com/ipython/nbconvert-examples). Also, have a look at ```base.tplx``` from the IPython sourcecode.

## Dependencies

- ipython (tested with 2.0dev)
- inkscape (to convert SVGs to PDF)
- pandoc (needed to convert markdown to latex)



