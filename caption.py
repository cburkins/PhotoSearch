#!/usr/bin/perl
use warnings;
use strict;
use Image::ExifTool qw(ImageInfo);

my $exifTool = new Image::ExifTool;


my $filename = "/home3/cburkins/test.jpg";

# Load EXIF data for new Picture
my $info = $exifTool->ImageInfo($filename);

# Get the caption from the picture
my $Picture_Caption = $exifTool->GetValue('Caption-Abstract');
if (! defined $Picture_Caption) { $Picture_Caption = ""; };

print $Picture_Caption;
