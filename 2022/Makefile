TEMPLATE := .template.py
SUBMISSION := .submit.py

all:
%:
	mkdir -p $@
	cp $(TEMPLATE) $@/solve1.py
	cp $(TEMPLATE) $@/solve2.py
	cp $(SUBMISSION) $@/submit.py

	touch $@/input
	touch $@/sample
	code $@ -g $@/input $@/sample $@/solve1.py $@/solve2.py

.PHONY: all
