#!/usr/bin/perl

# This script takes a votes file and a file cotaining the seg_id \t source seg
# and outputs a list of the best translations and source segments, sorted by 
# doc id and seg id.  It omits lines for which there were no votes.

open(VOTES, $ARGV[0]) or die("Couldn't open votes file $ARGV[0]");
open(SEGID_SOURCE, $ARGV[1]) or die("Couldn't open hindi file with segIDs from $ARGV[1]");

%bestTranslations = ();
while($line = <VOTES>) {
    chomp $line;
    @fields = split(/\t/, $line);
    $doc_seg_ids = $fields[0];
    ($docID, $segID) = split(/_/, $doc_seg_ids);
    $bestTranslation = $fields[2];
    $bestTranslations{$docID}{$segID} = $bestTranslation;
}
close(VOTES);

%sourceSentences = ();
while($line = <SEGID_SOURCE>) {
    chomp $line;
    @fields = split(/\t/, $line);
    $doc_seg_ids = $fields[0];
    ($docID, $segID) = split(/_/, $doc_seg_ids);
    $source = $fields[1];
    $sourceSentences{$docID}{$segID} = $source;
}
close(SEGID_SOURCE);

foreach $docID (sort { $a <=> $b } keys %bestTranslations) {
    foreach $segID (sort { $a <=> $b } keys %{$bestTranslations{$docID}}) {
	if($sourceSentences{$docID}{$segID}) {
	    print $docID . "\t" . $segID . "\t" . $sourceSentences{$docID}{$segID} . "\t" . $bestTranslations{$docID}{$segID} . "\n";
	}
    }
}
