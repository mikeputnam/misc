<?php
// Load the stamp and the photo to apply the watermark to
$stamp = imagecreatefromjpeg('/home/dhmn/dhmn-150x104.jpg');
$webcamfile = '/home/dhmn/webcam01.jpg';
$im = imagecreatefromjpeg($webcamfile);

// Set the margins for the stamp and get the height/width of the stamp image
$marge_right = 10;
$marge_bottom = 10;
$sx = imagesx($stamp);
$sy = imagesy($stamp);

// Create some colors
$white = imagecolorallocate($im, 255, 255, 255);
$grey = imagecolorallocate($im, 128, 128, 128);
$black = imagecolorallocate($im, 0, 0, 0);

$font = '/usr/X11R6/lib/X11/fonts/TTF/DejaVuSans.ttf';
$text = 'Appleton Makerspace';
imagettftext($im, 20, 0, 11, 26, $grey, $font, $text);// Text shadow
imagettftext($im, 20, 0, 10, 25, $white, $font, $text);// Add the text

$timestamptext = date ("F d Y H:i:s", filemtime($webcamfile));
imagettftext($im, 10, 0, 11, 451, $grey, $font, $timestamptext);// Text shadow
imagettftext($im, 10, 0, 10, 450, $white, $font, $timestamptext);// Add the text
// Copy the stamp image onto our photo using the margin offsets and the photo 
// width to calculate positioning of the stamp. 
imagecopy($im, $stamp, imagesx($im) - $sx - $marge_right, imagesy($im) - $sy - $marge_bottom, 0, 0, imagesx($stamp), imagesy($stamp));

// Output and free memory
imagejpeg($im,'/home/dhmn/webcam.jpg');
imagedestroy($im);
?>

