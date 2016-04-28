#!/usr/local/bin/perl
$|=1;
print '<header>'; # placeholder for your whole HTML header block
print '<span id=Progress>Working...</span>';
print '<footer>'; # placeholder for the rest of your document until but without </body>
sleep 1; # Something is done here
print <<_EOT_;
<script language=JavaScript type=text/javascript><!--
document.getElementById('Progress').innerHTML='Still working...';
//--></script>
_EOT_
sleep 1; # Something is done here
print <<_EOT_;
<script language=JavaScript type=text/javascript><!--
document.getElementById('Progress').innerHTML='Sorry, still not finished...';
//--></script>
_EOT_
sleep 1; # Something is done here
print <<_EOT_;
<script language=JavaScript type=text/javascript><!--
document.getElementById('Progress').style.display='none';
//--></script>
_EOT_
print '</body></html>'; # Page finished
