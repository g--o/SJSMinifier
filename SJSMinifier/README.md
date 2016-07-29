# SJSMinifier

## What can it do?

All it does is wrapping uglifyJS so you can build your compact your js library with ease.

* UglifyJS wrapper (https://github.com/mishoo/UglifyJS)
* Python based (https://python.org)

(tested on python 2.7)

## Usage
In terminal/script:
> $  python buildJS.py [dir] [output js file]

It would compact any .js file under dir into output js file.<br/>
It's useful to make some bash/batch script to generate your js build.<br/>

For example:

Single directory:
> python buildJS.py libfiles lib.js

Several directories / parts:

> python buildJS,py dir1 part1.js<br/>
> python buildJS.py dir2 part2.js<br/>
> ...<br/>
> python buildJS.py . build.js

## License
This is merely some python snippet with batch/bash examples.
Just enjoy yourselves and thank UglifyJS.
