django.jQuery(function($) {
    
    // Reference to each map and reference clone
    // Construct useful closure per map instance
    var map = $(".google-map[type=text]").each(function(evt) {
        var map, data,
            orig = $(this),
            clone = orig.clone(true).attr("type", "hidden"),
            defaults = {
                size: ["500px", "350px"],
                coordinates: [-34.397, 150.644]
            };

        // Replace map with clone
        orig.replaceWith(clone);

        // Set new map div
        map = $("<div class='map'/>");

        // Place after clone
        clone.after(map);

        // Parse data
        try {
            data = $.parseJSON(orig.val());
            data = $.extend({}, defaults, data);
        } catch(ex) {
            data = defaults;
        }

        // Set width/height
        map.css({ width: data.size[0], height: data.size[1] });

        // Assign coordinates
        var coordinates = new google.maps.LatLng(data.coordinates[0], data.coordinates[1]),
            // Init the map
            gmap = new google.maps.Map(map[0], {
                zoom: 8,
                center: coordinates,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            });
        
        // Add marker used for center positioning the map
        var center = new google.maps.Marker({
            position: coordinates,
            map: gmap,
            draggable: true,
            title: "Centered Here"
        });

        // Center map on marker drop
        google.maps.event.addListener(center, "mouseup", function(evt) {
            gmap.setCenter(center.position);
            data.coordinates = [ center.position.va, center.position.wa ];
            clone.val( JSON.stringify(data) );
        });

    });

});
