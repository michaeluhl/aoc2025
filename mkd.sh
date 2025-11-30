#!/bin/bash

make_day() {
  dname=$(printf "d%02d" $1)
  cp -r tmpl "${dname}"
  cd "${dname}"
  FILES=$(find ./ -regex '.*\.\(py\|md\)')
  for FILE in $FILES; do
    sed -ri 's/\{day\}/'${1}'/g' ${FILE}
  done
}

while getopts "d:" flag; do
  case "${flag}" in
  d) DAY=${OPTARG} ;;
  esac
done

if [[ ! -v DAY ]]; then
  echo "Day value must be supplied"
  exit 1
fi

make_day ${DAY}
