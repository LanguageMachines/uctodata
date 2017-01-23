# uctodata 0.4 CLST/ILK/CLiPS 1998 - 2016
	 https://github.com/LanguageMachines/uctodata/

Website and documentation: https://languagemachines.github.io/ucto

uctodata provides datafiles for the tokeniser ucto for several languages. The
language code can be supplied to ucto using the ``-L`` paramater (e.g. ``ucto
-L nld input.txt``):

 * ``eng`` - English
 * ``nld`` - Dutch
 * ``deu`` - German
 * ``fra`` - French
 * ``ita`` - Italian
 * ``spa`` - Spanish
 * ``por`` - Portuguese
 * ``rus`` - Russian
 * ``swe`` - Swedish
 * ``tur`` - Turkish
 * ``fry`` - Frisian

uctodata is architecture independent.

To install uctodata, first consult whether your distribution's
package manager has an up-to-date package.
If not, for easy installation of ucto and uctodata, it is included
as part of our software distribution LaMachine:
https://proycon.github.io/LaMachine .

To compile and install manually from source instead:

    $ bash bootstrap.sh
    $ ./configure
    $ make
    $ make install
