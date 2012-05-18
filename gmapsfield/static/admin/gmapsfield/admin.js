(function(window, document) {
	var jQ = window.jQuery || (window.django && window.django.jQuery);

	jQ(function($) {
		/**
		 * Plugin like access
		 */
		$.fn.setPosition = function(lat, lng) {
			var o = $(this[0]);
			console.log("Updating", o);
			var currentVal = $(o).val()
			var data = $.parseJSON( (currentVal == "None")?('{}'):(currentVal));
			if (!data) {
				data = {};
			}
			var pos = new google.maps.LatLng(lat, lng);
			var gmap = $(o).data('map');
			gmap.setCenter(pos);
			$(o).data('marker').setPosition(pos);
			
			data.coordinates = [ pos.lat(), pos.lng()];
			data.zoom = gmap.zoom;
			var map = $(gmap.getDiv());
			data.size = [map.width(), map.height()];
			
			$(o).val(JSON.stringify(data));
			console.log("Data =", JSON.stringify(data));
		}
		
		// Construct useful closure per map instance
		$(".google-map[type=text]").live("initialize-map", function(evt, data) {
			var map, data, orig = $(this), clone = orig.clone(true).attr("type", "hidden"), defaults = {
				size : ["500px", "400px"],
				coordinates : [-44.185408825666336, -68.983685546875],
				zoom : 8,
				markers : [],
				frozen : false
			};
			defaults = $.extend({}, defaults, data);

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
				for(var i in data) {
					if(data[i] == null) {
						data[i] = defaults[i];
					}
				}
			} catch(ex) {
				data = defaults;
			}

			// Set width/height
			map.css({
				width : data.size[0],
				height : data.size[1],
				border : "1px solid #ccc"
			});

			// Assign coordinates
			var coordinates = new google.maps.LatLng(data.coordinates[0], data.coordinates[1]),
			// Init the map
			gmap = new google.maps.Map(map[0], {
				zoom : data.zoom,
				center : coordinates,
				mapTypeId : google.maps.MapTypeId.ROADMAP
			});

			// Add marker used for center positioning the map
			var center = new google.maps.Marker({
				position : coordinates,
				map : gmap,
				draggable : true,
				title : "Centered Here"
			});

			// Allow resizing
			map.resizable({
				maxHeight : 480,
				maxWidth : 640,
				minHeight : 120,
				minWidth : 200,
				resize : function() {
					google.maps.event.trigger(gmap, 'resize');
					update();
				}
			});

			// Update function
			function update(evt) {
				gmap.setCenter(center.position);
				data.coordinates = [center.position.lat(), center.position.lng()];
				data.zoom = gmap.zoom;
				data.size = [map.width(), map.height()];
				clone.val(JSON.stringify(data));
			}

			// Used to attach a map to the instance
			$(".add-map").bind("click", function() {
				var that = $(this), widget = $("<input class='google-map' type='text' name='" + that.attr("data-name") + "' value='" + that.attr("data-value") + "' type='text' />");

				that.replaceWith(widget);
				widget.trigger("initialize-map");
				return false;
			});
			// Used to remove a map from the instance
			$(".remove-map").bind("click", function() {
				var that = $(this);
				$(".google-map").attr("value", "");

				return false;
			});
			// Used to remove a map from the instance
			$(".freeze-map").toggle(function() {
				$(this).text("Unfreeze");
				data.frozen = true;

				return false;
			}, function() {
				$(this).text("Freeze");
				data.frozen = false;

				return false;
			});
			// Center map on marker drop
			google.maps.event.addListener(center, "mouseup", update);
			// When zoom changed
			google.maps.event.addListener(gmap, "zoom_changed", update);
			$(clone).data('map', gmap);
			$(clone).data('marker', center);
		});
		// Reference to each map and reference clone
		var map = $(".google-map[type=text]").each(function(evt) {
			var defaults = $(".defaults").val();
			defaults && ( defaults = $.parseJSON(defaults));
			$(this).trigger("initialize-map", [defaults]);
		});
	});
})(this, this.document);
