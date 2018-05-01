#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from __future__ import print_function
import PyPDF2
import glob
import os


def get_all_pdf_file(path):
    all_pdfs = glob.glob("{0}/*.pdf".format(path))
    all_pdfs.sort(key=str.lower)
    return all_pdfs


def main():
    all_pdfs = get_all_pdf_file(os.path.expanduser('~/lmx/'))
    if not all_pdfs:
        raise SystemExit('No pdf file found!')
    merger = PyPDF2.PdfFileMerger()
    with open(all_pdfs[0], 'rb') as first_obj:
        merger.append(first_obj)

    for pdf in all_pdfs[1:]:
        with open(pdf, 'rb') as obj:
            reader = PyPDF2.PdfFileReader(obj)
            merger.append(fileobj=obj, pages=(1, reader.getNumPages()))

    with open('merger-pdfs.pdf', 'wb') as f:
        merger.write(f)


if __name__ == '__main__':
    main()

