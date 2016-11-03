#!/bin/bash

#========================================================================
# TODO: to produce filtered transcriptome annotation information 

# call Transcriptome annotation
# @yln^16Oct30

#export LD_LIBRARY_PATH=/opt/python/lib:$LD_LIBRARY_PATH
# ==== env
PIPE_HOME=$(dirname `readlink -f -- $0` | sed s/scripts//)
top_hits="$PIPE_HOME/scripts/get_top-hits.py"
length="$PIPE_HOME/scripts/count_length.py"
add_length="$PIPE_HOME/scripts/merge_output.py"
redundant="$PIPE_HOME/scripts/get_redundant.py"
toptop_hits="$PIPE_HOME/scripts/toptophit_annotation.py"
top_name="$PIPE_HOME/scripts/get_1column.py"
toptop_dtseq="$PIPE_HOME/scripts/toptop_dtseq.py"

show_help() {
cat << EOF
Usage:
    ${0##*/} [-h] [-i <FASTA>] [-b <BLASTX>]

Options:
    -h    show Transcriptome annotation help info
    -i    input nucleotide sequence file in FASTA format
	-b    input mpiBLASTX output file

Notes:
	0.  assembled nucleotide sequences in FASTA format should be
	prepared prior to running the pipeline;
    1.  "blast_output.txt" should be generated prior to running the
	pipeline.


Examples:
    $0  
EOF
}

# ==== argparse
KEEP_TEMP=0
#[[ $# -eq 0 ]] && show_help && exit 0
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -h) show_help
            exit 0; ;;
		-i) FASTA="$2"
			shift; ;;
		-b) BLASTX="$2"
		    shift; ;;
        *)  show_help
            exit 1; ;;
    esac
    shift
done


echo -e ">>!START PIPELINE: ${0##*/} @$(date)\n"

#=======================top-hits======================= 
echo -e ">>Start Step 1: get the top hit annotation information from
mpiBLASTX output: ${0##*/} @$(date)\n"
python $top_hits $BLASTX
echo -e ">>Finish Step 1: ${0##*/} @$(date)\n"

#=======================prepare for the merged output======================= 
echo -e ">>Start Step 2: add raw data sequence length and ratio: ${0##*/} @$(date)\n"
python $length $FASTA
python $add_length length_output.txt output.txt 	 
echo -e ">>Finish Step 2: ${0##*/} @$(date)\n"

#=======================delete redundant annotation======================= 
echo -e ">>Start Step 3: get redundant sequenceѕ: ${0##*/} @$(date)\n"
python $redundant merge_output.txt > toptophit_names
python $toptop_hits merge_output.txt
python $top_name toptophit_names
python $toptop_dtseq $FASTA top_1_column.txt
echo -e ">>Finish Step 3: ${0##*/} @$(date)\n"

#=======================clear useless information=======================
rm deleted_dtnames.txt gmon.out length_output.txt merge_output.txt output.txt top_1_column.txt toptophit_names

echo -e ">>!FINISH CONSENS Step 1-3: ${0##*/} @$(date)\n"
#================================================END===========================================================
