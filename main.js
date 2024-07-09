const mineField = document.getElementsByClassName('mineField')

// const mineTile = document.createElement('div')

// for (let x = 0; x < 9; x++){
//     for (let y = 0; y < 9; y++){
//         const mineTile = document
//     }
// }

for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
        const newDiv = document.createElement('div');
        newDiv.className = `tile (${row},${col})`;
        
        const innerDiv = document.createElement('div');
        innerDiv.className = 'tile-inner';
        innerDiv.textContent = `(${row},${col})`;
        newDiv.appendChild(innerDiv);

        mineFiled.appendChild(newDiv);
    }
}