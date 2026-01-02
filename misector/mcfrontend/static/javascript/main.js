document.addEventListener('DOMContentLoaded', init)

//Leaflet Map
function init(){
    const map = L.map('map').setView([18.50, -69.95], 14)
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);



//Fetch API 
    const fetchGetRequest = async (url, funcion) => {
        try {
            const response = await fetch (url)
            const json = await response.json()
            return funcion(json)
        } catch (error){
            console.log(error.message)
        }
    }

    const polygonStyle = {
        stroke:true,
        radious: 11,
        color: 'black',
        weight: 2,
        opacity: 1,
        fillColor: 'green',
        fillOpacity:1,
    }

    const selectedPolygonStyle = {
        stroke:true,
        radious: 11,
        color: 'orange',
        weight: 2,
        opacity: 1,
        fillColor: 'white',
        fillOpacity:1,
    }

    const stylesGeoJSONOnClick = (lugares)=>{
        let lastClickedFeature;
        lugares.on('click', (e)=> {
            if(lastClickedFeature){
                lugares.resetStyle(lastClickedFeature)
            }
    
            lastClickedFeature = e.layer;
            e.layer.setStyle(selectedPolygonStyle)
        })
    }

    const addNearByCities = (geoJSON) =>{
        console.log(geoJSON)
    }

    const addNearByCitiesLogic = (id) =>{
        let url = `http://127.0.0.1:8000/api/v1/ciudades/?lugarID=${id}`;//Referencia: Models.py
        fetchGetRequest(url, addNearByCities)
    }

    const placeImageElement = document.getElementById('placeimage');
    const menuTitleElement = document.getElementById('menu_title');
    const menuTextElement = document.getElementById('menu_text');

    const onEachFeatureHandler = (feature, layer) => {
        let nombreLugar = feature.properties.nombre_lugar
        layer.bindPopup(`El nombre de este lugar es <br/><center><b>${nombreLugar}</b></center`)

        let noImageAvailable = './media/imagen_lugar/imagen_no_disponible.jpg';
        layer.on('click', (e) => {
            let featureImage = feature.properties.campo_imagen ? feature.properties.campo_imagen : noImageAvailable
            let featureDescription = feature.properties.descripcion

            menuTitleElement.innerHTML = `Nombre del Lugar Popular del Barrio: ${nombreLugar}`;
            placeImageElement.setAttribute('src', featureImage);
            menuTextElement.innerHTML = featureDescription;
            
            let featureID = feature.properties.pk;
            addNearByCitiesLogic(featureID)
        })
    }

    const addAllPlacesToMap = (json) => {
        let lugares = L.geoJSON(json,{
            style: polygonStyle,//Para cambiar estilo de de poligonos al estilo definido 

            onEachFeature:(feature, layer) => {
                onEachFeatureHandler(feature,layer)
            }
        }).addTo(map)

        stylesGeoJSONOnClick(lugares)
    }

    fetchGetRequest('/api/v1/lugares', addAllPlacesToMap)

}