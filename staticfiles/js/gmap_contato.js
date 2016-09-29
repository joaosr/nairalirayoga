var fenway = new google.maps.LatLng(-1.4543319,-48.484464);

$(".contatos").gmap3({
    map:{
        options:{
              zoom: 17,
              mapTypeId: google.maps.MapTypeId.ROADMAP,
              streetViewControl: true,
              center: fenway
        }
    },
    streetviewpanorama:{
        options:{
              container: $(".streetviewpanorama"),
              opts:{
                    position: fenway,
                    pov: {
                          heading: 173.88,
                          pitch: 10,
                          zoom: 1
                    }
              }
        }
    }
});