/*! Lazy Load 1.9.5 - MIT license - Copyright 2010-2015 Mika Tuupola */
!function(a,b,c,d){var e=a(b);a.fn.lazyload=function(f){function g(){var b=0;i.each(function(){var c=a(this);if(!j.skip_invisible||c.is(":visible"))if(a.abovethetop(this,j)||a.leftofbegin(this,j));else if(a.belowthefold(this,j)||a.rightoffold(this,j)){if(++b>j.failure_limit)return!1}else c.trigger("appear"),b=0})}var h,i=this,j={threshold:0,failure_limit:0,event:"scroll",effect:"show",container:b,data_attribute:"original",skip_invisible:!1,appear:null,load:null,placeholder:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC"};return f&&(d!==f.failurelimit&&(f.failure_limit=f.failurelimit,delete f.failurelimit),d!==f.effectspeed&&(f.effect_speed=f.effectspeed,delete f.effectspeed),a.extend(j,f)),h=j.container===d||j.container===b?e:a(j.container),0===j.event.indexOf("scroll")&&h.bind(j.event,function(){return g()}),this.each(function(){var b=this,c=a(b);b.loaded=!1,(c.attr("src")===d||c.attr("src")===!1)&&c.is("img")&&c.attr("src",j.placeholder),c.one("appear",function(){if(!this.loaded){if(j.appear){var d=i.length;j.appear.call(b,d,j)}a("<img />").bind("load",function(){var d=c.attr("data-"+j.data_attribute);c.hide(),c.is("img")?c.attr("src",d):c.css("background-image","url('"+d+"')"),c[j.effect](j.effect_speed),b.loaded=!0;var e=a.grep(i,function(a){return!a.loaded});if(i=a(e),j.load){var f=i.length;j.load.call(b,f,j)}}).attr("src",c.attr("data-"+j.data_attribute))}}),0!==j.event.indexOf("scroll")&&c.bind(j.event,function(){b.loaded||c.trigger("appear")})}),e.bind("resize",function(){g()}),/(?:iphone|ipod|ipad).*os 5/gi.test(navigator.appVersion)&&e.bind("pageshow",function(b){b.originalEvent&&b.originalEvent.persisted&&i.each(function(){a(this).trigger("appear")})}),a(c).ready(function(){g()}),this},a.belowthefold=function(c,f){var g;return g=f.container===d||f.container===b?(b.innerHeight?b.innerHeight:e.height())+e.scrollTop():a(f.container).offset().top+a(f.container).height(),g<=a(c).offset().top-f.threshold},a.rightoffold=function(c,f){var g;return g=f.container===d||f.container===b?e.width()+e.scrollLeft():a(f.container).offset().left+a(f.container).width(),g<=a(c).offset().left-f.threshold},a.abovethetop=function(c,f){var g;return g=f.container===d||f.container===b?e.scrollTop():a(f.container).offset().top,g>=a(c).offset().top+f.threshold+a(c).height()},a.leftofbegin=function(c,f){var g;return g=f.container===d||f.container===b?e.scrollLeft():a(f.container).offset().left,g>=a(c).offset().left+f.threshold+a(c).width()},a.inviewport=function(b,c){return!(a.rightoffold(b,c)||a.leftofbegin(b,c)||a.belowthefold(b,c)||a.abovethetop(b,c))},a.extend(a.expr[":"],{"below-the-fold":function(b){return a.belowthefold(b,{threshold:0})},"above-the-top":function(b){return!a.belowthefold(b,{threshold:0})},"right-of-screen":function(b){return a.rightoffold(b,{threshold:0})},"left-of-screen":function(b){return!a.rightoffold(b,{threshold:0})},"in-viewport":function(b){return a.inviewport(b,{threshold:0})},"above-the-fold":function(b){return!a.belowthefold(b,{threshold:0})},"right-of-fold":function(b){return a.rightoffold(b,{threshold:0})},"left-of-fold":function(b){return!a.rightoffold(b,{threshold:0})}})}(jQuery,window,document);


//INSTANSIATE THE ISC OBJECT
var ISC = {};

jQuery(document).ready(function($) {
	
	$( '.slick' ).each( function() {
		
		var props = {
			prevArrow: '<div data-role="none" class="slick-prev fa fa-arrow-circle-left" aria-label="Previous" tabindex="0" role="button"></div>',
			nextArrow: '<div data-role="none" class="slick-next fa fa-arrow-circle-right" aria-label="Next" tabindex="0" role="button"></div>',
			adaptiveHeight: true,
			pauseOnHover: false,
 			cssEase: 'linear',
			autoplay: true,
  			autoplaySpeed: 0,
  			speed: 6000
		};
		
		if ( typeof sprops !== 'undefined' ) {
			var id = $( this ).attr( 'id' );
			if ( sprops[ id ] ) {
				for ( i in sprops[ id ] ) {
					props[ i ] = sprops[ id ][ i ];	
				}
			}
		}

		if ( $( this ).find( '> article' ).length ) {
			props['slide'] = 'article';
			$( this ).slick( props );
			$( this ).find( '> article' ).show().on( 'setPosition', function( event, slick ) {
				$( this ).find( '.slick-list' ).show();
				$( this ).find( 'article' ).show();
			});
		} else if ( $( this ).find( '> .elements' ).length ) {
			$( this ).find( '> .elements' ).slick( props ).on( 'setPosition', function( event, slick ) {
				$( this ).find( '.slick-list' ).show();
			});
		}
	});
	
	/* *
	* Mobile Menu Toggle
	* ================================== */
	$( '.nav-toggle' ).click( function() {
		$( 'body' ).toggleClass( 'open-nav' );
		if ( $( 'body' ).hasClass( 'open-nav' ) ) {
			$( 'html,body' ).animate( { scrollTop: 0 }, 500);	
		}
	});
	$( '.menu-toggle' ).click( function() {
		
		$( this ).closest( '.menu' ).find( 'ul.menu' ).toggle();
	});
	$( window ).bind( 'scroll', function( e ) {
		$( '.menu.burgered' ).each( function() {
			bl = $(this).offset().top + $(this).outerHeight(true);
			$( this ).find( ' > div:last-of-type' ).css( 'top', ( bl - $( window ).scrollTop() ) + 'px' );
		});
		
	});
	$( '.mobile-header-menu a' ).click( function() {
		$( 'body' ).removeClass( 'open-nav' );	
	});
	
	/* *
	* Mobile Toggle Full/Mobile Site
	* ================================== */
	$( '#view-full-site' ).click( function() {
		document.location = '' == document.location.search ? '?vfs=1' : document.location.href + '&vfs=1';
	});
	$( '#view-mobile-site' ).click( function() {
		document.location = '' == document.location.search ? '?vfs=0' : document.location.href + '&vfs=0';
	});
	
	//GOOGLE TRACK BUTTON CLICKS
	$( 'a.button' ).click( function() {
		var lbl = $( this ).attr( 'data-label' ) ? $( this ).attr( 'data-label' ) : $( this ).attr( 'title' );
		if ( typeof( ga ) == 'function' ) {
			ga( 'send', 'event', 'button', 'click', lbl ); 
			console.log( 'event-sent' );
		}
	});
	
	$( window ).bind( 'scroll', function( e ) {
		//STICKY MENU
		var sel = $( 'header .header-menu' ).length > 0 ? 'header .header-menu' : 'header';
		if ( $( window ).scrollTop() >= $( sel ).offset().top && $( window ).scrollTop() > 40 ) {
			$( '.sticky-menu' ).show();
			if ( $( '.sticky-menu' ).hasClass( 'sticky-init' ) )
				setTimeout( function() { $( '.sticky-menu' ).removeClass( 'sticky-init' ) }, 10 );
		} else {
			$( '.sticky-menu' ).addClass( 'sticky-init' ).hide();
		}
	});
	
	$( window ).bind( 'load resize', function( e ) {	
	
		//ADD MOBILE/DESKTOP CLASS TO BODY
		$( 'body' ).removeClass( 'd_mobile d_desktop' );
		$( 'body' ).addClass( window.innerWidth < 768 ? 'd_mobile' : 'd_desktop' );
		
		if ( navigator.userAgent.match(/iPad/i) != null ) {
			$( 'body' ).addClass( 'view_tablet' );
			return false;
		}
		
		var views = { 
			'general' : {
				'mobile'  : 480,
				'tablet'  : 900,
				'desktop' : 5000,
			},
			'specific' : {
				'mobile_vertical'  : 320,
				'mobile_landscape' : 480,
				'tablet_vertical'  : 760,
				'desktop_small'    : 1024,
				'desktop_medium'   : 2000,
				'desktop_large'    : 5000,
			}
		};
		
		for ( i in views ) {
			for ( j in views[ i ] ) {
				$( 'body' ).removeClass( 'view_' + j );
			}
		}
		
		for ( i in views ) {
			for ( j in views[ i ] ) {
				if ( window.innerWidth < views[ i ][ j ] ) {
					$( 'body' ).addClass( 'view_' + j );
					break;
				}
			}
		}
		
		$( '.menu.auto-burger' ).each( function() {
			var pmenu = $( this );
			if ( $( this ).find( 'ul.menu > li:first-of-type' ).offset().top != $( this ).find( 'ul.menu > li:last-of-type' ).offset().top ) {
				$( this ).addClass( 'burgered' );
				$( this ).removeClass( 'auto-burger' );
			}
		});
	});
	
	var sdr = 0;
	
	if ( $( 'subheader .slidedeck_frame' ).length > 0 ) {
		var s = $( 'subheader .slidedeck_frame' ).attr( 'style' );
		s = s.substring( 0, s.indexOf( 'height' ) );
		s = s.replace( 'width:', '' );
		var w = parseInt( s.trim() );

		if ( w ) {
			var h = parseInt( $( 'subheader .slidedeck_frame' ).css( 'height' ) );	
			sdr   = parseInt( w ) / h;
		}

		/* *
		* Maintain Subheader Slidedeck Ratio
		* ================================== */
		if ( sdr ) {
			$( window ).bind( 'load resize', function( e ) {
				var aw = parseInt( $( 'subheader .slidedeck_frame dl > dd:first' ).css( 'width' ) );
				var ah = aw / sdr;
				$( 'subheader .slidedeck_frame' ).css( 'height', ah + 'px' );
				$( 'subheader .slidedeck_frame .slidedeck' ).css( 'height', ah + 'px' );
				$( 'subheader .slidedeck_frame .slidedeck dd' ).css( 'height', ah + 'px' );
			});
		}
	}
	
	function set_ratio( el ) {
		pic--;
		$( this ).parent().attr( 'data-ratio', ( parseInt( this.width ) / parseInt( this.height ) ) );
		
		if ( 0 === pic ) {
			window_resize();
			$( document ).scroll();
		}
	}
	
	var pis = $( '.parallax-img img' );
	var pic = pis.length;

	pis.each( function() {
		if ( this.complete ) {
            set_ratio.call( this );
        } else {
            $( this ).one( 'load', set_ratio );
        }
	});
	
	var resizes = [];
	var rimages = [];
	$( '.iscsb-section.resize' ).each( function() {
		
		var p = $( this );
    	atfb = $( this ).css( 'background-image' );
		atfb = atfb.slice( 4, -1 );
		atfb = atfb.replace( /"/g, '' );
		atfb = atfb.replace( /'/g, '' ); 
		 
		if ( '' != atfb && ( atfb.indexOf( '.jpg' ) >= 0 || atfb.indexOf( '.png' ) >= 0 ) ) {
			resizes.push( $( this ) );
			rimages.push( atfb );
		}
	});
	
	function iscsb_loop_resize( els, imgs ) {
		
		var el  = els.pop();
		var src = imgs.pop();
		
		if ( src ) {
			img = new Image();
			img.src = src;
			img.onload = function () {
				iscsb_setbg_ratio( el, this.width, this.height );
				if ( els.count > 0 ) {
					iscsb_loop_resize( els, imgs );
				}
			};
		}
	}

	iscsb_loop_resize( resizes, rimages );
	
	function iscsb_setbg_ratio( el, w, h ) {
		console.log(el);
		el.attr( 'data-ratio', ( parseInt( w ) / parseInt( h ) ) );
	}
	
	$( '.parallax-img' ).parallax({
		speed : 0.40
	});

	if ( $( '.mobile-header' ).is( ':visible' ) || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test( navigator.userAgent ) ) {
		$( '.iscsb-section' ).css( 'background-size', 'cover' ).css( 'background-attachment', 'scroll' );
	}
	
	var tables = {};
	$( '.pb-area' ).find( '.block[class*="table-"]' ).each( function() {
		var cl = $( this ).attr( 'class' ).split(/\s+/);
		for ( i in cl ) {
			if ( cl[ i ].indexOf( 'table-' ) >= 0 ) {
				tables[ $( this ).attr( 'id' ) ] = parseInt( cl[ i ].replace( 'table-', '' ) );
			}
		}
	});

	$( window ).bind( 'load resize', function( e ) {
		window_resize();
		

		for ( p in tables ) {
			if ( is_mobile() ) {
				$( '#' + p ).find( '> .elements > div' ).css( 'height', 'auto' );
			} else {
				for ( i = 0; i < $( '#' + p ).find( '> .elements > div' ).length; i = i + tables[ p ] ) {
					var sel = 0 == i ? '#' + p + ' > .elements > div:lt(' + ( i + tables[ p ] ) + ')' : '#' + p + ' > .elements > div:gt(' + ( i - 1 ) + '):lt(' + ( i + tables[ p ] ) + ')';				
					var mh  = Math.max.apply( null, $( sel ).map( function (){
						return $( this ).outerHeight();
					}).get());
					$( sel ).css( 'height', mh + 'px' );
				}
			}
		}
		
		$( '.has-fullsize' ).each( function() {
			do_fullsize( '#' + $( this ).attr( 'id' ) );
		});
		
		$( '.has-vertical-align' ).each( function() {
			do_vertical_align( $( this ) );
		});
	});
	
//	$( window ).bind( 'load', function( e ) {
//		$( document ).resize();
//		$( document ).scroll();
//		
//		if ( $( ':target' ).length ) {
//			$( "html, body" ).animate({ scrollTop: $( ':target' ).offset().top - 100 }, 1000 );
//		}
//	});
	
	$( document ).scroll( function() {
		$( '#content' ).find( '.parallax-image' ).each( function() {
			var p = Math.round( ( $( window ).scrollTop() - $( this ).offset().top ) * .4 );
			$( this ).css( 'top', ( p ) + 'px');
		});
	});
	
	function window_resize() {
		
		$( '.iscsb-section.resize' ).each( function() {
			if ( undefined != $( this ).attr( 'data-ratio' ) ) {
				var h = ( ( $( this ).outerWidth() / $( this ).attr( 'data-ratio' ) ) );
				var p = h;
				if ( $( 'body' ).hasClass( 'logged-in' ) ) {
					p = h - 32;	
				}
				$( this ).css( 'min-height', p + 'px' ).css( 'background-size', '100% ' + h + 'px' );
			}
		});
		$( '.parallax-img' ).each( function() {
			var r  = $( this ).attr( 'data-ratio' );

			if ( ! r || ( ! $( this ).hasClass( 'resize' ) && ! $( 'img', $( this ) ).attr( 'src' ) ) ) {
				return;	
			}
			
			var p = $( this ).closest( '.iscsb-section' );

			if ( ! p.length ) {
				p = $( this ).closest( '#atf' );	
			}
			
			var pr = $( p ).outerWidth() / $( p ).outerHeight();
			var o  = 0;
			
			if ( $( p ).hasClass( 'resize' ) || 'atf' == $( p ).attr( 'id' ) ) {
				var pad = ( parseInt( $( p ).css( 'padding-top' ) ) + parseInt( $( p ).css( 'padding-bottom' ) ) );
				$( p ).css( 'min-height', ( ( $( p ).outerWidth() / r ) - pad ) + 'px' );
			}
			if ( r > pr ) {
				$( 'img', $( this ) ).css( 'width', 'auto' ).css( 'height', '100%' ).css( 'max-width', 'none' ).css( 'left', 'auto' );
			} else {
				$( 'img', $( this ) ).css( 'width', '100%' ).css( 'height', 'auto' ).css( 'max-width', '100%' ).css( 'left', '0px' );
			}
		});
	}

	

	/* *
	* Fix for Date Picker
	* ================================== */
	try {
		$( '.datepicker' ).datepicker();
	} catch( e ) {}
	
	//DECLARE COMMON HELPER FUNCTIONS
		
	/* *
	* Makes dropdown display to the left if it is to extend past the window.
	* ================================== */
	ISC.shift_dropdown_left = function() {
		$( '.menu>li' ).hover( function() {
			$( 'ul', $( this ) ).each( function() {
				var p = $( this ).offset();
				if ( p.left + $( this ).outerWidth() > document.body.offsetWidth ) {
					$( this ).css( 'right', '0px' ).css( 'overflow', 'hidden' );
				} else {
					$( this ).removeAttr( 'style' );
				}
			});
		});	
	};
	
	
	/* *
	* Move label to placeholder in sidebars to save room
	* ================================== */
	ISC.hide_empty_choices = function() {
		$( '.gform_wrapper .gfield').each( function() {
			
			if ( $( '.gfield_label .gfield_required', $( this ) ).length != 0 ) {
				lbl = $( '.gfield_label', $( this ) ).clone();
				
				$( '.gfield_required', $( lbl ) ).remove();
				
				if ( '' == $( lbl ).html().trim() ) {
					$( '.gfield_label .gfield_required', $( this ) ).remove();
				}	
			}
		});
	}
	
	/* *
	* Move label to placeholder in sidebars to save room
	* ================================== */
	ISC.submit_search_form = function() {
		$( '.searchform .fa-search' ).click( function() {
			$( this ).closest( 'form' ).submit();
		});
	}
	/* *
	* Move label to placeholder in sidebars to save room
	* ================================== */
	ISC.form_label_to_placeholder = function() {
		
		var test = document.createElement( 'input' );
		
    	if ( ! ( 'placeholder' in test ) ) {
			$( '.gform_widget .gform_wrapper label' ).show();		
		} else {			
			$( '.gform_wrapper:not(.default_wrapper) .gfield' ).each( function() {		
				if ( $( '.ginput_complex', $( this ) ).length != 0 ) {
					$( 'label', this ).hide();
					$( '.ginput_complex span', $( this ) ).each( function() {
						var lbl = $( 'label', this ).html();
						$( 'input[type=text], textarea', $( this ) ).attr( 'placeholder', lbl );
					});
				} else if ( $( '.ginput_container ul', $( this ) ).length == 0 ) {			
					$( 'label', this ).hide();
					
					var lbl = $( 'label', $( this ) ).html();
					if ( lbl && lbl.indexOf( '<' ) > -1 )
						lbl = lbl.substr( 0, lbl.indexOf( '<' ) );
					if ( $( this ).hasClass( 'gfield_contains_required' ) ) {
						lbl = lbl + ' *';	
					}
					$( 'input[type=text], textarea', this ).attr( 'placeholder', lbl );
				}
			});
		}
	};
	/* *
	* Scroll to the top
	* ================================== */
	ISC.to_top = function() {
		$( '#to_top' ).click( function() {
			$( 'html,body' ).animate( { scrollTop: 0 }, 500);
		});
	};
	
	/* *
	* Remove tabindex from sidebar & footer forms
	* ================================== */
	ISC.remove_tabindex = function() {
		$( '.sidebar input, .sidebar textarea, .sidebar select, #footer input, #footer textarea, #footer select' ).removeAttr( 'tabindex' );
	};
	
	
	
	/* ========================================================================
	* INIT FUNCTIONS FOR ALL TEMPLATES
	* ========================================================================= */
	ISC.to_top();
	ISC.submit_search_form();
	ISC.hide_empty_choices();
	ISC.shift_dropdown_left();
	ISC.form_label_to_placeholder();
	ISC.remove_tabindex();
	
	//$( '.lazy' ).lazyload({effect : "fadeIn"});
	function is_mobile() {
		return $( '.mobile-header' ).is( ':visible' ) || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test( navigator.userAgent );	
	}
	
	

	if ( 'function' == typeof( ga ) ) {
		var pers = [ .5, .9 ];
		
		$( window ).scroll( function() {
			
			if ( ! pers.length ) {
				return false;	
			}
			
			var wintop = $( window ).scrollTop(), docheight = $( document ).height(), winheight = $( window ).height();
	
			for ( i in pers ) {
				p = pers[i];
				if  ( ( wintop / ( docheight - winheight ) ) > p ) {				
					pers.splice( i, 1 );
				   	ga( 'send', 'event', 'scroll', String( p * 100 ) + '%' ); 
				}
			}
		});
	}
});


function showNextQuote( q, qi ) {
	++qi;
	q.eq( qi % q.length )
		.fadeIn(2000)
		.delay(2000)
		.fadeOut(2000, function() { showNextQuote( q, qi ) });
}



(function($) {

    $.fn.parallax = function(options) {

        var windowHeight = $(window).height();

        // Establish default settings
        var settings = $.extend({
            speed        : 0.15
        }, options);

		var on_scroll = function( el ) {
			var scrollTop = $(window).scrollTop();
			var offset    = el.offset().top;
			var height    = el.outerHeight();
			var speed     = settings.speed;
			var to = -20;
			
			if ( $( 'body' ).hasClass( '.loggedin' ) ) {
				to += parseInt( $( 'html #wpadminbar' ).outerHeight() );
			}
			
			if ( 'fixed' == el.css( 'position' ) ) {
				offset = 0;
				speed  = speed * -1;
			}
			
			var yBgPosition = Math.round((scrollTop - offset ) * speed);// + to;
			
			if ( yBgPosition < 0 ) {
				//yBgPosition = 0;	
			}

			el.css('top', yBgPosition + 'px').css('bottom',( yBgPosition * -1 ) + 'px');
		}

        // Iterate over each object in collection
        return this.each( function() {

			// Save a reference to the element
			var $this = $(this);

			if ( $( '.mobile-header' ).is( ':visible' ) || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test( navigator.userAgent ) ) {
//				$( document ).on( 'swipe', function(){
//					on_scroll( $this );
//				});
			} else {
				$( document ).scroll( function(){
					on_scroll( $this );
				});
			}
		});
    }
}(jQuery));