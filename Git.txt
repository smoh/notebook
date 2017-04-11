# Git

* Prefixing `!` negates the pattern in .gitignore files. This is useful in e.g., data directory where you constantly add/remove stuff but only want to track scripts to download the data and what not.

```
# Ignore everything
*

# except these files
!.gitignore
!somescript
```

[link](http://stackoverflow.com/questions/987142/make-gitignore-ignore-everything-except-a-few-files)

* One can locally ignore files without corrupting `.gitignore` that would be shared with others by adding patterns to `.git/info/exclude`.

[link](http://stackoverflow.com/questions/1753070/how-to-ignore-files-only-locally-in-git)

* Revive deleted files in git [link](http://stackoverflow.com/questions/953481/find-and-restore-a-deleted-file-in-a-git-repository)