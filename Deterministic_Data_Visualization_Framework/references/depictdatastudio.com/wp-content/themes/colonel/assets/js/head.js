function do_fullsize( sel ) {
		
	var el = jQuery( sel );
	
	if ( undefined != el.attr( 'data-ratio' ) ) {
		var ih = el.outerWidth() / el.attr( 'data-ratio' );
		el.css( 'min-height', ih + 'px' );
		if ( el.hasClass( 'has-parallax' ) ) {
			var wh = parseInt( window.innerHeight );
			var ph = ih + ( wh - ih ) * .4;
			var pw = ph * el.attr( 'data-ratio' );
			var pm = ( pw - el.outerWidth() ) / -2;
			
			el.find( '.parallax-image' ).height( ph + 'px' );
			el.find( '.parallax-image' ).width( pw + 'px' );
			el.find( '.parallax-image' ).css( 'left', ( pm > 0 ? 0 : pm ) + 'px' );
		}
		if ( el.hasClass( 'slick' ) ) {
			if ( el.find( '.slick-slide' ).length ) {
				el.find( '.slick-slide' ).css( 'min-height', ih + 'px' );
				
				if ( el.find( '.slick-slide > .elements > .block' ).length ) {
					el.find( '.slick-slide > .elements > .block' ).css( 'min-height', ih + 'px' );
				}
				
			} else if ( el.find( '> article > .elements > .block' ).length ) {
				el.find( '> article > .elements > .block' ).css( 'min-height', ih + 'px' );
			} else if ( el.find( '> article' ).length ) {
				el.find( '> article' ).css( 'min-height', ih + 'px' );
			} else if ( el.find( '> .elements' ).length ) {
				el.find( '> .elements > div' ).css( 'min-height', ih + 'px' );
			}
		}
	}
	if ( el.hasClass( 'has-slidedeck-background' ) ) {
		var oh = el.outerHeight();
		el.find( '.slidedeck-frame' ).css( { width: '100%', height : oh + 'px' } );
		el.find( '.slidedeck-frame > .slidedeck' ).css( { width: '100%', height : oh + 'px' } );
		el.find( '.slide' ).css( { width: '100%', height : oh + 'px' } );
	}
}

function do_vertical_align( el ) {
	var pp = ( el.outerHeight() - el.find( '> .elements' ).outerHeight() ) / 2;
	el.css( 'padding-top', ( pp < 25 ? 25 : pp ) + 'px' );
}

function do_burger( el ) {
	if ( el.hasClass( 'always-burger' ) ) {
		el.addClass( 'burgered' );
	}
}