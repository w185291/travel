const fs = require('fs');
const path = require('path');

const filePath = path.join('c:/workspace/travel/index.html');
let content = fs.readFileSync(filePath, 'utf8');

// The placeholder container usually looks like this:
// <div class="lg:w-2/5 relative bg-slate-100 overflow-hidden min-h-[300px]">
//     <div class="w-full h-full flex flex-col items-center justify-center p-8 text-center text-slate-400 min-h-[250px]">
//         ... svg ... button ...
//     </div>
//     <div class="absolute top-4 left-4 ..."> ... </div>
// </div>

// We want to replace the INNER div (flex flex-col ...) with an IMG tag.
// We must do this sequentially.

const regex = /<div\s+class="w-full h-full flex flex-col items-center justify-center p-8 text-center text-slate-400 min-h-\[250px\]">[\s\S]*?<\/div>/i;

let day = 1;

while (day <= 9) {
    // Determine image file
    // 1-7 are .jpg, 8-9 are .png
    let ext = (day >= 8) ? 'png' : 'jpg';
    let imgTag = `<img src="assets/${day}.${ext}" alt="Day ${day} Image" class="w-full h-full object-cover transition-transform duration-700 hover:scale-110">`;

    if (regex.test(content)) {
        content = content.replace(regex, imgTag);
        console.log(`Replaced Day ${day} placeholder with ${imgTag}`);
    } else {
        console.warn(`Could not find placeholder for Day ${day}`);
    }
    day++;
}

// Remove the script that handles the button if it exists, or just leave it (it won't find buttons anymore)
// But we should clean up the script.js reference if we want to be thorough.
// The user didn't ask to delete script.js, just "replace images".

fs.writeFileSync(filePath, content, 'utf8');
console.log("Finished replacing images.");
