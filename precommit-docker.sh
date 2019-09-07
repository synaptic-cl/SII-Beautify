#!/bin/bash
ARGS=$@
# docker run --rm -v $(pwd)/:/app sii_beautify /bin/bash -c "$ARGS"
docker-compose run --rm app /bin/bash -c "$ARGS"
exit $?
