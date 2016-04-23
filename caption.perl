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
my $pictureCaption = $exifTool->GetValue('Caption-Abstract');
if (! defined $pictureCaption) { $pictureCaption = ""; };

my $pictureImageDescription = $$info->GetValue('ImageDescription');
if (! defined $pictureImageDescription) { $pictureImageDescription = ""; };

my $pictureDescription = $$info->GetValue('Description');
if (! defined $pictureDescription) { $pictureDescription = ""; };

printf "Caption: $pictureCaption\n";
printf "ImageDescription: $pictureImageDescription\n";
printf "Description: $pictureDescription\n";


my $Picture_Year = $exifTool->GetValue('DateTimeOriginal');
printf "Year: $Picture_Year\n";
