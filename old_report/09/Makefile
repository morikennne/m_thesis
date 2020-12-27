
# Input target file info
TARGET_PREFIX = Mori_Progress_
TARGET_SUFFIX = .pdf

# Input source file name
SOURCE = main.tex

# Get current directory name and use it for file name
DIRNAME = $(notdir $(CURDIR))

# -> Mori_Progress_**.pdf
TARGET = $(addprefix $(TARGET_PREFIX),$(DIRNAME)$(TARGET_SUFFIX))

# remove suffix
SOURCE_BASENAME = $(basename $(SOURCE))

# Applicable suffix for "make clean"
# NOTE: NOT INCLUDE .tex, or you delete source file
REMOVE_SUFFIX_LIST = .aux .bbl .blg .dvi .log .xbb .toc .lof .lot

$(TARGET): compile_with_cite clean
no_cite: compile_with_nocite clean
	
compile_with_cite:
	platex -shell-escape $(SOURCE_BASENAME)
	pbibtex $(SOURCE_BASENAME)
	platex -shell-escape $(SOURCE_BASENAME)
	platex -shell-escape $(SOURCE_BASENAME)
	dvipdfmx -o $(TARGET) -f ptex-ipa.map $(SOURCE_BASENAME)

compile_with_nocite:
	platex -shell-escape $(SOURCE_BASENAME)
	dvipdfmx -o $(TARGET) -f ptex-ipa.map $(SOURCE_BASENAME)

clean:
	rm -f $(foreach suffix,$(REMOVE_SUFFIX_LIST),*$(suffix))
	rm -f src/*.aux
	rm -f figure/*.xbb
