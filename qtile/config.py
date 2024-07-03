
#          
#              _          _  _   ___  
#  __   _____ (_) ___ ___| || | / _ \ 
#  \ \ / / _ \| |/ __/ _ \ || || (_) |
#   \ V / (_) | | (_|  __/__   _\__, |
#    \_/ \___/|_|\___\___|  |_|   /_/ 
                                   



import os
import re
import socket
import subprocess
from libqtile import qtile
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule 
from libqtile.widget import Spacer
#from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
from typing import List  # noqa: F401
#from spotify import spotify
#from qtile_extras import widget ##global  menu 

mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
subprocess.call([home + '/.config/qtile/autostart.sh'])

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def jls_extract_def(key):
    return key


keys = [

# Most of our keybindings are in sxhkd file - except these

# SUPER + FUNCTION KEYS

    Key([mod], "a", lazy.spawn('xfce4-appfinder')),
    Key([mod], "b", lazy.hide_show_bar()),
    Key([mod], "d", lazy.spawn('discord'),lazy.group["9"].toscreen()),
    Key([mod], "e", lazy.spawn('thunar'),lazy.group["6"].toscreen()),
    Key([mod], "c", lazy.spawn('caprine')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
  # Key([mod], "m", lazy.spawn('')),
    Key([mod], "p", lazy.spawn('pamac-manager')),
    Key([mod], "q", lazy.spawn(home + '/.config/rofi-quicklinks/quicklinks.sh')),
    Key([mod], "t", lazy.spawn('xfce4-terminal')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "w", lazy.spawn('brave'),lazy.group["1"].toscreen()),
  # Key([mod], "x", lazy.spawn('')),
    Key([mod], "x", lazy.spawn(home + '/.config/rofipower/rofipower.sh')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "F1", lazy.spawn('brave')),
    Key([mod], "F2", lazy.spawn('thunderbird'),lazy.group["10"].toscreen()),
    Key([mod], "F3", lazy.spawn('inkscape')),
    Key([mod], "F4", lazy.spawn('gimp')),
    Key([mod], "F5", lazy.spawn('geany')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('rhythmbox')),                             
    Key([mod], "F8", lazy.spawn("spotify"),lazy.group["10"].toscreen()),
    Key([mod], "F9", lazy.spawn(home + '/.config/rofi/rofi-sound2.sh')),
    #Key([mod], "F10",lazy.spawn('rofi -show drun -show-icons')),
    #Key([mod], "F11",lazy.spawn('rofi -show run')),
    Key([mod], "F12",lazy.spawn(' xfce4-terminal --drop-down')),
    # SCREENSHOTS
    Key([mod], "Print", lazy.spawn('xfce4-screenshooter')),
    
# SUPER + SHIFT KEYS
#   KeyChord([mod],"e", [ ]),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    
#   Key([mod, "shift"], "d", lazy.spawn('morc_menu')),
     
 # SUPER + CONTROL KEYS
 
 # CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')), 
 
 # CONTROL + ALT KEYS
 
 #CONTROL + ALT KEYSQ
  # Key(["mod1", "control"], "')),
  # Key(["mod1", "control"], "')),
  # Key(["mod1", "control"], "a", lazy.spawn('')),
  # Key(["mod1", "control"],"b", lazy.spawn('thunar')),
 
   Key(["mod1", "control"],"f", lazy.spawn('firefox'),lazy.group["2"].toscreen()),
   Key(["mod1", "control"],"g", lazy.spawn("setxkbmap gr")),
  Key(["mod1", "control"],"i", lazy.spawn('nitrogen')),
  # Key(["mod1", "control"], "k", lazy.spawn('')),
  # Key(["mod1", "control"], "l", lazy.spawn('thunar')),
    Key([mod], "c", lazy.spawn('caprine')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
  # Key([mod], "m", lazy.spawn('')),
    Key([mod], "p", lazy.spawn('pamac-manager')),
    Key([mod], "q", lazy.spawn(home + '/.config/rofi-quicklinks/quicklinks.sh')),
    Key([mod], "r", lazy.sawn('xfce4-settings-manager')),
   
   Key(["mod1", "control"],"o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
   #Key(["mod1", "control"], "p", lazy.widget['notify'].prev()),
   Key(["mod1", "control"],"r", lazy.spawncmd()),
   Key(["mod1", "control"],"r", lazy.spawn('rofi-theme-selector')),
   Key(["mod1", "control"],"s", lazy.spawn('spotify')),
   Key(["mod1", "control"],"t", lazy.spawn('xfce4-terminal')),
   Key(["mod1", "control"],"u", lazy.spawn("setxkbmap us")),
    #Key(["mod1", "control"], "y", lazy.widget['notify'].toggle()),
   
 
 # CONTROL + KEYS     
     
    Key(["mod1"], "c", lazy.spawn('xfce4-terminal -e cava ')),
   # Key(["mod1"], "k", lazy.spawn('')),
   # Key(["mod1"], "f", lazy.spawn('vfrom spotify import spotifyriety -n')),
   # Key(["mod1"], "p", lazy.spawn('variety -p')),
   # Key(["mod1"], "t", lazy.spawn('variety -t')),
   # Key(["mod1"], "Up", lazy.spawn('variety --pause')),
   # Key(["mod1"], "Down", lazy.spawn('variety --resume')),
   # Key(["mod1"], "Left", lazy.spawn('variety -p')),
   # Key(["mod1"], "Right", lazy.spawn('variety -n')),
    Key(["mod1"], "F1", lazy.spawn('rofi -show filebrowser -show-icons')),   #Alt+Shift+2
    Key(["mod1"], "F2", lazy.spawn('gmrun')),
    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),
   #Key(["mod1"], "F4", lazy.spawn('qpaeq')),
   #Key(["mod1"], "F5", lazy.spawn('balena-etcher-electron')),
    Key(["mod1"], "Shift_R" , lazy.widget['keyboardlayout'].next_keyboard()),
   #Key(["mod1"], "Tab", lazy.spawn('rofi -show window -show-icons')),
    Key(["mod1"], "Tab", lazy.spawn(home + '/.config/rofi/rofi-sound1.sh')),
   
   

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

  
     
# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod,  "mod1"], "space", lazy.prev_layout()),


# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

#FOCUS ON SCREEN

   Key(["mod1", "control"],"1",   ##### Keyboard focus screen(0) =screen number 1
    lazy.to_screen(0),
    ),
 Key(["mod1", "control"],"2",      ##### Keyboard focus screen(1) =screen number 2
    lazy.to_screen(1),
    ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

#move  to  treetab
  Key([mod, 'control'], "u", lazy.layout.section_up()),   # Move up a section in treetab
  Key([mod, 'control'], "d",lazy.layout.section_down()),  # Move down a section in treetab

# LAYOUT COLUMNS
   Key([mod], "j", lazy.layout.down()),
   Key([mod], "k", lazy.layout.up()),
   Key([mod], "h", lazy.layout.left()),
   Key([mod], "l", lazy.layout.right()),
   Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
   Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
   Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
   Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
   Key([mod, "control"], "j", lazy.layout.grow_down()),
   Key([mod, "control"], "k", lazy.layout.grow_up()),
   Key([mod, "control"], "h", lazy.layout.grow_left()),
   Key([mod, "control"], "l", lazy.layout.grow_right()),
   Key([mod], "s", lazy.layout.toggle_split()),
   Key([mod], "n", lazy.layout.normalize()),
   
    ]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]
group_labels = [ "➊", "➋", "➌", "➍", "➎", "➏", "➐", "➑", "➒", "➓" ]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "floating",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#ff79c6",
            "border_normal": "#44475a"
            }

layout_theme = init_layout_theme()


layouts = [
    #layout.MonadTall(margin=8, border_width=2, border_focus=" "#bd93f9", border_normal="#44475a"),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(margin=8, border_width=2, border_focus=" "#bd93f9", border_normal="#44475a"),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.TreeTab(
    	        font = "Ubuntu",
                fontsize = 12,
                sections = ["1", "2", "3"],
                section_fontsize = 12,
                section_fg ="#ff79c6"	,
                bg_color = "#282a36"	,
                active_bg = "#bd93f9"	,
                active_fg = "#f8f8f2",
                inactive_bg = "#282a36",
                inactive_fg = "#f8f8f2	",
                padding_y = 5,
                section_top = 10,
                panel_width = 120,
                **layout_theme
                ),
    layout.Stack(
    	num_stack=2 ,
    	**layout_theme
    	),
   # layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# COLORS FOR THE BAR
#Theme name : ArcoLinux Default
def init_colors():
    return [["#282a36", "#282a36"], # color 0 bg
            ["#f8f8f2", "#f8f8f2"], # fg
            ["#000000", "#000000"], # color01
            ["#f1fa8c", "#f1fa8c"], # color 3 fg
            ["#bd93f9", "#bd93f9"],  # color 4 fg
            ["#f3f4f5", "#f3f4f5"], # color 5 fg
            ["#ff5555", "#ff5555"], # color 6 fg
            ["#50fa7b", "#50fa7b"], # color 7
            ["#9aedfe", "#9aedfe"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9

colors = init_colors()


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Ubuntu Bold",
                fontsize = 12,
                padding = 2,
                background=colors[0])
                
widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/python.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(home + '/.config/rofi/rofi-sound1.sh')}
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/streamee.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(home + '/.config/qtile/scripts/streamee.sh')}
                       ),
             widget.Image(
                       filename = "~/.config/qtile/icons/chatgpt-icon.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(home + '/.config/qtile/scripts/chatgpt.sh')}
                       ),        
                widget.GroupBox(
               	            font="Ubuntu Bold",
                            fontsize = 10,
                            margin_y = 4,
                            margin_x = 0,
                            padding_y = 6,
                            padding_x = 5,
                            borderwidth = 0,
                            disable_drag = True,
                            active = colors[9],
                            inactive = colors[8],
                            rounded = False,
                            highlight_method = "text",
                            this_current_screen_border = colors[1],
                            foreground = colors[2],
                            background = colors[0]
                             ),
                widget.TextBox(
                            font="Ubuntu Bold",
                            text=" | ",
                            foreground=colors[6],
                            background=colors[0],
                            padding = 0,
                            fontsize=14
                                    ),
                widget.CurrentScreen(
                            active_color = '#50fa7b',
                            active_text =   '❗',
                            background =colors[0],
                            font="JoyPixel",
                            fontsize = 12,
                            foreground = colors[2],
                            inactive_color = '#ff5555',
                            inactive_text  = '❌',
                            markup = True,
                            padding = 2
                             ),
                widget.Prompt(foreground = '#ff79c6',
                            background = colors[0],),
                widget.TextBox(
                            font="Ubuntu Bold",
                            text=" | ",
                            foreground=colors[6],
                            background=colors[0],
                            padding = 0,
                            fontsize=14
                                ),
                # widget.Global  foreground = colors[2],
               #             background = colors[0]corations=[]	,
                #            fmt='{}'	,
                #            font="Ubuntu Bold",	
                #            fontshadow=None,	
                #            fontsize=  12,
                #            foreground= colors[2],	
                #            hide_after= 0.5,	
                #            highlight_colour="#bd93f9",	
                #            markup= True,
                #            max_chars=	0 ,	
                #            menu_background= colors[0],
                #            menu_font=	"Ubuntu Bold",	
                #            menu_fontsize=	14	,
                #            menu_foreground= colors[2],	
                #            menu_row_height= None,	 
                #            menu_width= 200,
                #            padding=	4,
                #            scroll = True,
                #            scroll_clear= False,	
                #            scroll_delay=2,	
                #            scroll_hide=	False,	
                #            scroll_interval= 0.1,	    
                #            scroll_repeat=	True,	
                #            scroll_step= 1,
                #            show_menu_icons= True,
                #            separator_colour=colors[5]
                #            ),
                widget.WindowName(
               	            font="Ubuntu Bold",
                            fontsize = 10,
                            foreground = colors[4],
                            background = colors[0],
                              ),
                    #  Spotify(    
                    #         font="Ubuntu Bold",
                    #         fontsize = 10,
                    #         foreground = colors[4],
                    #         background = colors[0]
                    #         ),
                 widget.Mpris2(
                             font="Ubuntu Bold",
                             fontsize = 10,
                             name='spotify',
                             foreground = colors[3],
                             objname="org.mpris.MediaPlayer2.spotify",
                             display_metadata=['xesam:title', 'xesam:artist'],
                             stop_pause_text = 'Player paused',
                             scroll_interval = 0.3,
                                ),
                # widget.TextBox(
                #             font="Ubuntu Bold",
                #             text=" 🎵 ",
                #             foreground=colors[6],
                #             background=colors[0],
                #             padding = 0,
                #             fontsize=10
                #              ),
                widget.TextBox(
                            font="Ubuntu Bold",
                            text=" 🖮 ",
                            background=colors[0],
                            padding = 0,
                            fontsize=10
                                     ),
                widget.KeyboardLayout(
                            configured_keyboards=['us','gr'] ,
                            font="Ubuntu Bold",
                            foreground = colors[7],
                            fontsize = 12,
                            background = colors[0],
                            update_interval= 0.1
                              ),
                widget.TextBox(
                            font="Ubuntu Bold",
                            text="  ",
                            background=colors[0],
                            padding = 0,
                            fontsize=2
                                           ),
                widget.CapsNumLockIndicator(
                            font="Ubuntu Bold",
                            fontsize = 10,
                            foreground = colors[8],
                            background = colors[0],
                            fmt= '{}',
                            padding= None,
                            update_interval= 0.5
                                        ),
               widget.Wttr(
                            lang='en',
                            location={
                            'GALATSI': 'γαλάτσι',
                            '38.01783515,23.7542517323474': 'γαλάτσι',
                            },
                            format='%t,',
                            units='m',
                            markup = True ,
                            xml = False ,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(home + '/.config/qtile/scripts/wttr.sh')},
                           foreground=colors[6],
                           background=colors[0],
                           user_agent = 'voice49',
                          update_interval=3000,
                     ),
                widget.CurrentLayoutIcon(
                            font="Ubuntu Bold",
                            foreground = colors[4],
                            fontsize = 6,
                            background = colors[0],
                            scale= 0.5,
                            markup = True
                                    ),
                widget.CurrentLayout(
                            font="Ubuntu Bold",
                            foreground = colors[4],
                            fontsize = 10,
                            background = colors[0]
                              ),
                widget.TextBox(
                            font="Ubuntu Bold",
                            text="🎧",
                            background=colors[0],
                            padding = 1,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
                            fontsize=10
                              ),
                widget.Volume(
                           font="Ubuntu Bold",
                           foreground = colors[3],
                           fontsize=12
                             ),
                # widget.Notify(
                #            fmt="  {} ",              
                #            font="Ubuntu Bold",
                #            fontsize = 10,
                #            markup = True,
                #            padding = 10
                #               ),
             
                widget.TextBox(
                            font="Ubuntu Bold",
                            text="⏰",
                            foreground=colors[3],
                            background=colors[0],
                            padding = 1,
                             mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(home + '/.config/qtile/scripts/.sh')},
                            fontsize=10
                            ),
                widget.Clock(
                            foreground = colors[5],
                            background = colors[0],
                            fontsize = 10,
                            font="Ubuntu Bold" ,
                            format="%H:%M %d/%m/%Y"
                               ),
                widget.TextBox(
                            font="Ubuntu Bold",
                            text="  ",
                            foreground=colors[6],
                            background=colors[0],
                            padding = 0,
                            fontsize=12
                              ),
                widget.Systray(
                           background=colors[0],
                           icon_size=20,
                           padding = 4
                           ),
              ]
    return widgets_list

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[20:24]
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.8)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.8))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='tilix'),

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True
focus_on_window_activation = "smart" # or smart #focus
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

#wmname = "LG3D"
wmname = "qtile"


