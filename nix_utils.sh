## replace spaces in all file names with underscore

find $1 -name "* *.xml" -type f -print0 | \
  while read -d $'\0' f; do mv -v "$f" "${f// /_}"; done
