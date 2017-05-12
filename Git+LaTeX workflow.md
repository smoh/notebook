# Git+LaTeX workflow

[Git](https://git-scm.com/) with a hosting service such as [Github](https://github.com) provides an excellent platform for collaborative writing. In this post, I describe tips and tricks that make it easy to start a collaborative LaTeX document.

## Templating with cookiecutter

If you need the same kind of form over and over again, like the case of starting a journal article, it makes a lot of sense to _template_. Each time you start a new paper, you only want to change select portions such as title, filename, directory name (before writing the content, of course). Tools such as [cookiecutter](https://github.com/audreyr/cookiecutter) are built for that purpose.

Once I build a template such as [this one](https://github.com/smoh/cookiecutter-aasdraft) for a LaTeX document to be submitted to AAS, I can do

```sh
cookiecutter /url/to/template
```
which will prompt me to enter small number of customizing variables that I've defined (in `cookiecutter.json`), and start a paper instantly.

## Using Makefile to make stuff (and record how I made stuff)

[Makefiles](https://www.gnu.org/software/make/manual/make.html) are great to automate compiling the LaTeX document. Even when you think some action will likely not be repeated, it may be a good idea to record the rule of how you did it just in case.

Makefiles are also just plain text files, and plays nicely with git. Once you include a Makefile template that you can work with, you'll only have to make small changes depending on the project.

## Diffing with `latexdiff`

It will often be the case that you circulate your draft and modify according to feedback multiple times. In such cases, people will often find it convenient to have a marked-up version that only highlights changes from the last version. This might also be something that your referee wants.

As part of [MacTeX](http://www.tug.org/mactex/) distribution, a script `latexdiff` is available for this purpose. With the versioning history of git, you can just grab the tex file from e.g., the first circulation and diff it with the current version. [Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) are useful to record specific points in history.

## Using bibtex for citation

I use bibtex for citation, and [BibDesk](http://bibdesk.sourceforge.net/) to manage my bibliography with [ads2bibdesk](https://github.com/jonathansick/ads_bibdesk) osx service, which facilitates easily importing the bibtex entry and PDF file from the ADS webpage of a paper.

I setup an autocompletion of citekey in my text editor vim using [LaTeX-Box](https://github.com/LaTeX-Box-Team/LaTeX-Box). This way, I can type in part of title or author inside the cite bracket

```
\citealt{|
```
invoke autocompletion with `C-x C-o` and select the entry I want without the need to remember/lookup citekeys.

When using ads2bibdesk, BibDesk will add keys such as `Bdsk-File-1` or `Bdsk-Url-1` to keep track of the location of the PDF file or url for ADS webpage. This is very convenient to quickly open up the paper PDF and read, or to look up references/citations to articles on ADS. But it will only be useful on your local computer and not worth checking in to git shared with others. In order to clean the `.bib` file of these fields, you can use `bibexport` script to extract only necessary fields. For example, I put the following in my Makefile in order to generate the clean bibtex file called `ref.bib` from my local file `ref.local.bib` if it exists.

```Makefile
	if [ -a ref.local.bib ] ; \
	then \
		if [ -a ref.bib ] ; \
		then \
			${RM} ref.bib; \
		fi; \
		bibexport -a -o ref.bib ref.local.bib ; \
	fi;
```
