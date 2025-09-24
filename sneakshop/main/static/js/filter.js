window.addEventListener(
    'load',
    Main
)

function Main(){
    let radios = document.body.querySelectorAll('input[type="radio"]')
    const form = document.body.querySelector('.filter-form')
    radios.forEach(radio => {

        radio.addEventListener(
            'change',
            ()=>{
                form.submit();
            }
        )
    });
}