use strict;
use Bio::SeqIO;
 
my $input_file = shift;
 
my $seq_in  = Bio::SeqIO->new(
                              -format => 'fasta',
                              -file   => $input_file,
                              );
 
# loads the whole file into memory - be careful
# if this is a big file, then this script will
# use a lot of memory
 
my $seq;
my @seq_array;
while( $seq = $seq_in->next_seq() ) {
    push(@seq_array,$seq);
}
 
# now do something with these. First sort by length,
# find the average and median lengths and print them out
 
@seq_array = sort { $a->length <=> $b->length } @seq_array;
 
my $total = 0;
my $count = 0;
foreach my $seq ( @seq_array ) {
    my $slen = $seq->length;
    my $name = $seq->id;
    print "$name\t$slen\n";
}
