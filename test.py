import os

file_name = input('Enter file name: ')
commit_message = input('Enter commit message: ')

init = 'git init'
add = 'git add .'
commit = 'git commit -m %s' % (commit_message)
remote_add = 'git remote add origin https://github.com/dmoore90/%s.git' % (file_name)
push = 'git push -u origin master'

os.system(init)
os.system(add)
os.system(commit)
os.system(remote_add)
os.system(push)

#l = (init, add, commit, remote_add, push)

#for i in l:
#	os.system(str(i))
