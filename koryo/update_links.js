const fs = require('fs');

function updateFile(file) {
    let content = fs.readFileSync(file, 'utf8');
    content = content.replace(/<a href="itinerary\.html#(day-02|day-paektu|day-03|day-05)"([\s\S]*?)<\/a>/g, '<div tabindex="0" onclick="void(0)" style="-webkit-tap-highlight-color: transparent;"$2</div>');
    fs.writeFileSync(file, content);
}

['index.html', '_7/code.html'].forEach(f => {
    try {
        updateFile(f);
        console.log(f + " updated");
    } catch (e) {
        console.error(e);
    }
});
