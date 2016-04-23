#!/usr/bin/perl
use warnings;
use strict;
use Image::ExifTool qw(ImageInfo);

my $exifTool = new Image::ExifTool;



my $filename = "/home3/cburkins/test.jpg";

if (-e $filename)
{ 
    print "File exists\n";
}

# Load EXIF data for new Picture
my $info = $exifTool->ImageInfo("$filename");

# Get the caption from the picture
my $pictureCaptionAbstract = $exifTool->GetValue('Caption-Abstract');
if (! defined $pictureCaptionAbstract) { $pictureCaptionAbstract = ""; };

my $pictureImageDescription = $exifTool->GetValue('ImageDescription');
if (! defined $pictureImageDescription) { $pictureImageDescription = ""; };

my $pictureDescription = $exifTool->GetValue('Description');
if (! defined $pictureDescription) { $pictureDescription = ""; };

printf "CaptionAbstract: $pictureCaptionAbstract\n\n";
printf "ImageDescription: $pictureImageDescription\n\n";
printf "Description: $pictureDescription\n\n";


my $Picture_Year = $exifTool->GetValue('DateTimeOriginal');
printf "Year: $Picture_Year\n";
