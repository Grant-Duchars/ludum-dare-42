if(global.dialcount<10)
{
	if ((mouse_x>800 && mouse_x<865) && (mouse_y>350 && mouse_y<414))
		{
			global.dial = global.dial + "1";
			global.dialcount += 1;
		}
}
show_debug_message(global.dial);