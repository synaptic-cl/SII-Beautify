#!/bin/bash
ARGS=$@
docker run --rm -v $(pwd)/:/app sii_xml_to_pdf /bin/bash -c "$ARGS"
exit $?
