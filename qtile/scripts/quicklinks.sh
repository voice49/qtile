#!/usr/bin/env bash

## Author : Aditya Shakya (adi1090x)
## Mail : adi1090x@gmail.com
## Github : @adi1090x
## Reddit : @adi1090x

rofi_command="rofi - quicklinks.rasi"

# Links 
google=" google"
facebook=" facebook"
instagram=" instagram"
github=" github"
gitlab=" gitlab"
netflix=" netflix"
skroutz=" skroutz"
eshop=" eshop"
youtube=" youtube"
efood="🌭 efood "



# Variable passed to rofi
options="$google\n$facebook\n$instagram\n$youtube\n$efood\n$netflix\n$skroutz\n$eshop\n$github\n$gitlab"

chosen="$(echo -e "$options" | $rofi_command -p "  " -dmenu -selected-row 0)"
case $chosen in
    $google)
        google-chrome-stable --new-tab https://www.google.com
        ;;
    $facebook)
        google-chrome-stable --new-tab https://www.facebook.com
        ;;
    $instagram)
        google-chrome-stable --new-tab https://www.instagram.com/?hl=el
        ;;
    $github)
        google-chrome-stable --new-tab https://www.github.com
        ;;
    $gitlab)
        google-chrome-stable --new-tab https://gitlab.com/dwt1
        ;;
    $netflix)
        google-chrome-stable --new-tab https://www.netflix.com/browse
        ;;
    $skroutz)
        google-chrome-stable --new-tab https://www.skroutz.gr/
        ;;   
    $eshop)
        google-chrome-stable --new-tab https://www.e-shop.gr/
        ;;      
    $youtube)
        google-chrome-stable --new-tab https://www.youtube.com
        ;;
    $efood)
        google-chrome-stable --new-tab https://www.e-food.gr
        ;;        
esac
