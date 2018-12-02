rapydscript background.py > background.js
rm -r build/background.js
mv background.js build


rapydscript content.py > content.js
rm -r build/content.js
mv content.js build
