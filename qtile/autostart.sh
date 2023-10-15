#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#screen lauyout arandr
run $HOME/.screeenlayout/screenlayout.sh &

#change your keyboard if you need it
setxkbmap -layout "us,gr" -option  "grp:alt_shift_toggle"

xsetroot -cursor_name left_ptr &

run nm-applet &
picom --config $HOME/.config/qtile/picom.conf&
run pamac-tray &
run xfce4-power-manager &
numlockx on &			
#run mpv --no-video ~/Documents/bell.oga &
run ffplay -nodisp -autoexit  $HOME/Documents/bell.oga &
picom --config $HOME/.config/qtile/picom.conf &
#run picom -CGb &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#usr/lib/xfce-polkit &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
nitrogen --restore &
run xfce4-clipman &
run ffplay -nodisp -autoexit  $HOME/Music/stereo/desktop-logoff.oga
ckb-next  & 
		
