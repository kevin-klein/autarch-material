Running

Install AutArch first using the provided README.

Start docker desktop.

Use your favorite command line to run this:
$ cd [current folder]

$ docker build . -t autarch-figure-1
$ docker run --rm -it --mount src="$(pwd)/output",target="/workspace/output",type=bind autarch-figure-1

The output will be found in the output folder. 