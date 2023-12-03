const comands = () => {
    const xmlhttp = new XMLHttpRequest()
    const url = 'http://10.5.0.5:4201/commands'
    xmlhttp.open('GET', url, true)
    xmlhttp.send()
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            const data = JSON.parse(xmlhttp.responseText)
            console.log(data)
            let div = document.getElementById('data')
            for (let i = 0 ; i < data.lComandas; i++) {
                anadirDatos(data.lComandas[i].primerPlato, data.lComandas[i].segundoPlato, data.lComandas[i].nMesa)
            }

        }
    }
}

const anadirDatos = (primerPlato, segundoPlato, nMesa) => {
    div=document.createElement('data')
    const node = document.createElement('li')
    const textnode = document.createTextNode(primerPlato + ' , ' + segundoPlato + ' , ' + nMesa)
    node.appendChild(textnode)
    div.appendChild(node)
}

const nuevaComanda = () => {
    let primerPlato =document.getElementById('primerPlato').value;
    let segundoPlato =document.getElementById('segundoPlato').value;
    let nMesa =document.getElementById('nMesa').value;

    console.log(primerPlato +',' + segundoPlato + ',' + nMesa)

    if (primerPlato != ' ' && segundoPlato != ' ' && nMesa != ' ') {
        
        const resq = new XMLHttpRequest();
        const url = 'http://10.5.0.5:4201/nuevacomanda';
        resq.open('POST', url, true);
        resq.setRequestHeader('Content-Type', 'application/json');  // Usar JSON en lugar de form-urlencoded

        // Define el cuerpo de la solicitud como un objeto JSON
        const requestBody = {
            primerPlato: primerPlato,
            segundoPlato: segundoPlato,
            nMesa: nMesa
        };
        resq.onreadystatechange = function () {
            if (resq.readyState == 4 && resq.status == 200) {
                
                anadirDatos(primerPlato, segundoPlato, nMesa)
            }
           else {
            console.error('Error al enviar la solicitud:', resq.statusText);
            }
        }
        resq.send(JSON.stringify(requestBody));
    } else {
        console.log("Alguno de los campos está vacío");
    }
}

