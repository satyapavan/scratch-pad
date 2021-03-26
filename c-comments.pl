#!/usr/bin/perl

#########################################################
# this script will grep out any "C-style" comments 	#
# from a file.  C-Style being /* */ or //          	#
#                                                  	#
# usage: comment_grep <filename>                   	#
#                                                  	#
# to recursively traverse a directory with this:   	#
# find ./ -name '*' -exec comment_grep {} > /tmp/foo \;	#
#                                                  	#
#########################################################

$infile = shift;

$/ = "";	# remove newline from the line delimiter

$found = 0;
while(<>)
{
#this pattern will match /* */ comments
   if(
      m{
      (/\*		# match the /*
      (?:[^*][^/])*	# match any number of characters that AREN'T */
      \*/)		# match the */
      }mx		# multi-line regex x option to allow comments
     )	
   { 
      unless($found)	# list what file you found this in, if you find anything 
      { 
	 print "\nfrom $infile:\n"; 
      }
      print "$1\n";	# print /* */ and anything in between
      $found = 1;
   } 
# this pattern will match // comments
   if(
      m{
      (//.*\n)		# match // then anything, up to a newline
      }x 		# x option to allow comments
     )
   { 
      unless($found)	# list what file you found this in, if you find anything 
      { 
	 print "\nfrom $infile:\n"; 
      }
      print "$1";	# print /* */ and anything in between
      $found = 1;
   } 
} 

