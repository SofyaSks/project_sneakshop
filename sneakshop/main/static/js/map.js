
function init(){
    let center = [43.6539263828755,-79.4572834741227]
    let map = new ymaps.Map('map',{
        center: center,
        zoom: 15

    })

    let placemark = new ymaps.Placemark(center, {}, {

    }) 

    map.geoObjects.add(placemark)

}



ymaps.ready(init);