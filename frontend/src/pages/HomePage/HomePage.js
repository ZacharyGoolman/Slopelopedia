import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";
import { GoogleMap, useJsApiLoader, Marker} from '@react-google-maps/api';


const containerStyle = {
  width: '100%',
  height: '400px'
};

const center = {
  lat: 47.116386,
  lng: -101.299591
};

function MyComponent() {
  const [map, setMap] = useState(null)
  const [searchResults, setSearchResults] = useState([])
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "AIzaSyC4kj_CKRPE0oVTsnq-IRtqBypLebgaA-g"
  })



  useEffect(() => {
    getAllLocations()
      
  }, [])
  
      async function getAllLocations(){
      let response = await axios.get(`http://127.0.0.1:8000/api/slopelopedia/all/`)
      console.log(response.data)
      setSearchResults(response.data)                    
  
  }

  const onLoad = React.useCallback(function callback(map) {
    const bounds = new window.google.maps.LatLngBounds(center);
    map.fitBounds(bounds);
    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null)
  }, [])

  const position = {
    lat: 27.9881,
    lng: 86.9250
  }

  return (
      <GoogleMap
        mapContainerStyle={ {
          width: '100%',
          height: '400px'
        }}
        center={ {
          lat: 47.116386,
          lng: -101.299591
        }}
        zoom={50}
    
      >
   
          {searchResults.length>0 && searchResults.map((el) => {
            console.log(el.latitude)
            return <Marker position={{lat:el.latitude, lng:el.longitude }}/>
          } )}
        
        <></>
      </GoogleMap>
   
  ) 
}

export default React.memo(MyComponent)

