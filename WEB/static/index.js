const url = 'http://192.168.0.25:5000/control/'

function turn_on(){
    fetch(url + 'on').then((res) => {
        // alert('success')
    }).catch((e) => {
        alert(e)
    })
}

function turn_off() {
    fetch(url + 'off').then((res) => {
        // alert('success')
    }).catch((e) => {
        alert(e)
    })
}