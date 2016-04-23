#!/usr/bin/perl
use warnings;
use strict;
use Image::ExifTool qw(ImageInfo);

my $filename = "filename";

# Load EXIF data for new Picture
my $info = $exifTool->ImageInfo($filename);

# Get the caption from the picture
$Picture_Caption = $exifTool->GetValue('Caption-Abstract');
if (! defined $Picture_Caption) { $Picture_Caption = ""; };

