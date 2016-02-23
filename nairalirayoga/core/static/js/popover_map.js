$(function(){

var gmap_content = '<script>$(function(){ var fenway = new google.maps.LatLng(-1.447106,-48.486899); $(".map-view").gmap3({  map:{options:{zoom: 17, mapTypeId: google.maps.MapTypeId.ROADMAP, streetViewControl: true, center: fenway } }, streetviewpanorama:{ options:{ container:$(".street-view"), opts:{ position:fenway, pov:{ heading:34, pitch: 10, zoom: 1 }}}}});});</script>';

var content_popover = '<div class="row">'+
                          '<div class="col-lg-6">'+
                              '<div class="street-view" id="streetView" style="width: 550px; height: 400px; float: left; display: block;"></div>'+
                            '</div>'+
                            '<div class="col-lg-6">'+
                               '<div class="map-view" id="map-view" style="width: 550px; height: 400px; float: right; display: block;"></div>'+
                            '</div>'+
                      '</div>';

var template_popover = '<div class="popover bottom" style="min-height: 50%; max-width: 100%; width: 100%; height: 70%; position: relative; display: block;">'+
                           '<div class="arrow"></div>'+
                           '<h3 class="popover-title">João</h3>'+
                           '<div class="popover-content">'+content_popover+gmap_content+'</div>'+
                       '</div>';

$("#popover_contato").popover({
                            placement : 'bottom',
                            html:true,
                            title:" ",
                            template: template_popover,
                            content: content_popover+gmap_content,
                            }).popover('show');

});