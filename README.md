# uctodata 0.10 CLST/ILK 2009 - 2024
	 https://github.com/LanguageMachines/uctodata/

Website and documentation: https://languagemachines.github.io/ucto

uctodata provides datafiles for the tokeniser ucto for several languages. The
language code can be supplied to ucto using the ``-L`` parameter (e.g. ``ucto
-L nld input.txt``):

 * ``eng`` - English
 * ``eng-twitter`` - English twitter texts
 * ``nld`` - Dutch
 * ``nld-historical`` - Historical Dutch texts
 * ``nld-twitter`` - Dutch twitter texts
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

To compile and install manually from source instead:

    $ bash bootstrap.sh
    $ ./configure
    $ make
    $ make install
