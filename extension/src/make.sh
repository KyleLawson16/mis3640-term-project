rapydscript hello.py > hello.js
rm -r build/hello.js
mv hello.js build

rapydscript content.py > content.js
rm -r build/content.js
mv content.js build
