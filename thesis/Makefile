
# Input target file info
TARGET = mori-m20.pdf
# TARGET = main.pdf

# Input main source file name
SOURCE = main.tex
SOURCE_BASENAME = $(basename $(SOURCE))  # Remove suffix

# Specify suffix that is applied at "make clean"
REMOVE_SUFFIX_LIST = aux bbl blg log xbb toc lof lot dvi out

all: $(TARGET) clean

$(TARGET): main.dvi
	dvipdfmx -o $(TARGET) -f ptex-ipa.map $<

main.dvi: $(SOURCE)
	platex -shell-escape $(SOURCE_BASENAME)
	# andolab2 を使う場合は bibtex を pbibtex に変更する
	bibtex $(SOURCE_BASENAME) > transcript
	# pbibtex $(SOURCE_BASENAME) > transcript
	platex -shell-escape $(SOURCE_BASENAME) > /dev/null
	platex -shell-escape $(SOURCE_BASENAME) >> transcript


# Remove intermediate file (this hardly affect compile-time)
clean:
	rm -f $(foreach suffix,$(REMOVE_SUFFIX_LIST),*.$(suffix))
	rm -f src/*.aux
	rm -f figure/*.xbb
