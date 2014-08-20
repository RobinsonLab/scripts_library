# this replaces .profile, which contains enthought python stuff
export PATH="/usr/local/bin:/usr/local/sbin:~/bin:$PATH"
# IMP installs into /usr/local/lib/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages
alias showFiles='defaults write com.apple.finder AppleShowAllFiles YES; killall Finder /System/Library/CoreServices/Finder.app'
alias hideFiles='defaults write com.apple.finder AppleShowAllFiles NO; killall Finder /System/Library/CoreServices/Finder.app'
eval "$(rbenv init -)"

# export PATH=/Users/jmrobinson/.ssh:$PATH

export EDITOR='subl -w'

export PATH="$PATH:~/Documents/scripts:."

