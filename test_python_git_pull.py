import git 
git_dir="https://github.com/qraft-technologies/AlphaJu"
g = git.cmd.Git(git_dir)
g.pull()