if(global.dialcount<10)
{
	if ((mouse_x>800 && mouse_x<865) && (mouse_y>352 && mouse_y<417))
		{
			global.dial = global.dial + "1";
			global.dialcount += 1;
		}
	else if ((mouse_x>928 && mouse_x<993) && (mouse_y>352 && mouse_y<417))
		{
			global.dial = global.dial + "2";
			global.dialcount += 1;
		}
	else if ((mouse_x>1056 && mouse_x<1121) && (mouse_y>352 && mouse_y<417))
		{
			global.dial = global.dial + "3";
			global.dialcount += 1;
		}
	else if ((mouse_x>800 && mouse_x<865) && (mouse_y>480 && mouse_y<545))
		{
			global.dial = global.dial + "4";
			global.dialcount += 1;
		}
	else if ((mouse_x>928 && mouse_x<993) && (mouse_y>480 && mouse_y<545))
		{
			global.dial = global.dial + "5";
			global.dialcount += 1;
		}
	else if ((mouse_x>1056 && mouse_x<1121) && (mouse_y>480 && mouse_y<545))
		{
			global.dial = global.dial + "6";
			global.dialcount += 1;
		}
	else if ((mouse_x>800 && mouse_x<865) && (mouse_y>736 && mouse_y<801))
		{
			global.dial = global.dial + "7";
			global.dialcount += 1;
		}
	else if ((mouse_x>928 && mouse_x<993) && (mouse_y>736 && mouse_y<801))
		{
			global.dial = global.dial + "8";
			global.dialcount += 1;
		}
	else if ((mouse_x>1056 && mouse_x<1121) && (mouse_y>736 && mouse_y<801))
		{
			global.dial = global.dial + "9";
			global.dialcount += 1;
		}
}
show_debug_message(global.dial);