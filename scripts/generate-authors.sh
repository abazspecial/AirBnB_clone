#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# alsoo see".mailmap" for how email addresses and names are deduplicated

{
	cat <<-'EOH'
		# This particular file lists all individuals having contributed content to the repository.
		# For how it is generated, see `hack/generate-authors.sh`.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} >AUTHORS
