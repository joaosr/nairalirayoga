var fenway = new google.maps.LatLng(-1.453860,-48.485118);

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
                          heading: 34,
                          pitch: 10,
                          zoom: 1
                    }
              }
        }
    }
});