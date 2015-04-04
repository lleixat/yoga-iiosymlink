#!/bin/bash
dest=$HOME/bin/iiosymlink

parentdir=$(dirname "${dest}")

function _install(){
    cp ./iiosymlink.py ${dest}
    chmod u+x ${dest}
    echo "iiosymlink properly installed in ${parentdir}"
}

if [ -f $dest ]; then
    echo "iiosymlink already installed in ${parentdir}, overwrite it (y/n)?"
    read a
    case "$a" in
        y|Y)
            rm ${dest} && echo "${dest} was removed"
            ;;
        *)
            echo "exit" && exit
            ;;
    esac
fi

_install

exit
