In order to run this you will need to have Go installed in your system.

Because we are using some non-standard packages, from the webserver folder, run the following command before compiling:

'go get'

Then, in order to install the webserver, run

'go install github.com/okfn-brasil/queriDO/src/webserver/'

Assuming that the above path is inside your $GOPATH/src/ folder.
The binary will then be installed on $GOPATH/bin/webserver.exe (for Windows)
