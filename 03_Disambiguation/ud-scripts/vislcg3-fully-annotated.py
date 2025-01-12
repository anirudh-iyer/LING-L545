#!/usr/bin/env python3

import sys, re;

rword = re.compile('"<(.+)>"');
rbase = re.compile('"(.+)"');
rcateg = re.compile(' ([_A-Za-z0-9]+)');
rnode = re.compile('#([0-9]+)->');
rparent = re.compile('->([0-9]+)');
rfunc = re.compile('@(.+) #');
rdep = re.compile('#[0-9]+->[0-9]+');

dissUnk = False;

if len(sys.argv) > 1: #{
	dissUnk = True;
#}

# Input:
#	"<Қала>"
#		"қала" n nom @nmod #1->2
#	"<халқы>"
#		"халық" n px3sp nom @subj #2->3
#	"<58,3%>"
#		"58,3" num percent nom @main #3->0
#			"е" cop aor p3 sg @cop #4->3
#	"<.>"
#		"." sent @punct #5->3

blokk = '';
sentcount = 0;
complete = 0;
cleantokens = 0;
for line in sys.stdin.readlines(): #{
		
	if line.strip() == '' or line.strip() == '¶' and blokk != '': #{
		print('# %d %d/%d %d' % (sentcount, len(rdep.findall(blokk)), blokk.count('\t"'), blokk.count('"\*')),file=sys.stderr);
		if dissUnk and blokk.count('"*') > 0: #{
			blokk = '';
			sentcount = sentcount + 1;
			continue;
		#}
		if blokk.count('\t"') == len(rdep.findall(blokk)): #{
			complete = complete + 1;
			#blokk = blokk + line;
			cleantokens = cleantokens + blokk.count('"<');	
			print(blokk);
			print('');
		#}
		#print(sentcount,file=sys.stderr);
		blokk = '';
		sentcount = sentcount + 1;
	#}
	
	blokk = blokk + line;
#}
line = '';
if blokk != '': #{
	print('# %d %d/%d' % (sentcount, len(rdep.findall(blokk)), blokk.count('\t"')),file=sys.stderr);
	if dissUnk and blokk.count('"*') > 0: #{
		print('')
		print(complete,'/',sentcount,file=sys.stderr);
		print(cleantokens, file=sys.stderr);
		sys.exit(0);
	#}
	if blokk.count('\t"') == len(rdep.findall(blokk)): #{
		blokk = blokk + line;
		cleantokens = cleantokens + blokk.count('"<');
		print(blokk);
		print('');
	#}
#}
print('')
print('%.2f\t%d/%d' % (complete/sentcount*100.0, complete, sentcount),file=sys.stderr);
print(cleantokens, file=sys.stderr);
