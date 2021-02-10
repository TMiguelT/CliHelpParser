Changelog
=========
3.0.1 (2021-02-10)
------------------
* Pin spacy dependency above 3.x.x
* Remove support for older spacy versions

3.0.0 (2021-01-27)
------------------
Breaking Changes
****************
* Rework of executors
    * `explore` is now a method on the executor object
    * Add a `man`-page executor
    * `aclimatise.explore` is now deprecated
* Replaces ``dataclasses`` with ``attrs`` throughout

New Features
************
* Add ``docker_image`` field to ``Command``
* The ``DockerExecutor`` has been updated to automatically set this field based on the Docker image being used by it
* Add `Janis <https://janis.readthedocs.io/en/latest/index.html>`_ converter (`#73 <https://github.com/aCLImatise/CliHelpParser/issues/73>`_)

Bug Fixes
*********
* Support ``/`` as a synonym delimiter (`#67 <https://github.com/aCLImatise/CliHelpParser/issues/67>`_)
* Use the optional/required status of each flag appropriately in the downstream CWL/WDL (`#68 <https://github.com/aCLImatise/CliHelpParser/issues/68>`_)


2.2.0 (2020-09-26)
------------------
* Add ``command.reanalyse()``, which re-analyses the help text stored in the command, using the current parser
* Add ``command['sort']`` which lets you access subcommands by name

2.1.0 (2020-09-22)
------------------
* Add `bedtools random` as a test case
* Use a simple metric to exclude flags unless they have a somewhat valid description text, this should result in less false-positive flags being detected
* Fixed the `id` field in the CWL tool definitions including some path elements (like `..`)
* Use `cwltool` as a command-line tool instead of via the Python API (it is supposed to be more stable)

2.0.0 (2020-09-16)
------------------
* Rename the package from ``acclimatise`` to ``aclimatise``, to be consistent with the naming elsewhere. This is a breaking change, and will require you to ``pip install aclimatise`` from now on.
* Similarly, rename the module to ``aclimatise``. This will require you to ``import aclimatise``
* Rename the CLI utility from ``acclimatise`` to ``aclimatise``.

1.2.0 (2020-09-13)
------------------
User-Facing Changes
*******************
* Add output generation for CWL and WDL

Fixes
*****
* Fix the railroad diagrams not building

Internal Changes
****************
* Upgrade wdlgen to 3.0.0
* Delete `hash.py`, which was unused
* Add `Command.outputs`, which is a property that returns all outputs
* Add (rudimentary) prioritisation for types, ensuring we don't always choose the type derived from the argument (this is an initial attempt at #37)
* Support more complex assertions for test cases, including the number of outputs
* Small improvements to the infer_type regexes
* Refactor test case assertions into the `HelpText` class

1.1.1 (2020-09-10)
------------------

* Fix the README file in PyPI

1.1.0 (2020-09-10)
------------------

User-Facing Changes
*******************

* Better distinction between description blocks and flags, allowing us to successfully parse flags of this form::

    --use_strict (enforce strict mode)
          type: bool  default: false
    --es5_readonly (activate correct semantics for inheriting readonliness)
          type: bool  default: true

* Support parsing multiple usage blocks, and add the ``UsageInstance`` class, which provides access to all these usage examples in the help. For example after parsing the text below, we would have 4 ``UsageInstance`` instances. The instances are provided on ``Command.usage``::

    Usage:
      shell [options] -e string
        execute string in V8
      shell [options] file1 file2 ... filek
        run JavaScript scripts in file1, file2, ..., filek
      shell [options]
      shell [options] --shell [file1 file2 ... filek]
        run an interactive JavaScript shell

* Add flag and positional de-duplication, ensuring we don't have duplicate options in the final ``Command``
* Add the ``max_length`` parameter to ``parse_help``:  If the input text has more than this many lines, no attempt will be made to parse the file (as  it's too large, will likely take a long time, and there's probably an underlying problem if this has happened).        In this case, an empty Command will be returned
* Enforce that a ``Positional`` must have at least 2-character names, in the parser
* Enforce that a ``Positional`` must have a description, in the parser

Internal Changes
****************

* Rewrite of both the flag and usage parser
* Added more customizable indent tokens, meaning we no longer need the ``customIndentedBlock``
* Refactor both the usage parser and the flag parser into subclasses of ``IndentParserMixin``, which provides useful common parsing logic that relates to indentation
* Use ``MatchFirst`` instead of ``MatchLongest`` logic in most places in the parser. This should result in more consistent behaviour.
* Add ``typeHLA.js`` text, which is derived from the ``bwa-kit`` container.

Fixes
*****

* Always strip out newlines from the WDL description

1.0.3 (2020-08-26)
------------------
* Add a hard timeout to the ``DockerExecutor``, even if it's producing output, e.g. the ``yes`` command.

1.0.2 (2020-08-25)
------------------
* Ensure we never return ``None`` from the ``DockerExecutor``
* Add initial parsing of "output inputs". Thanks to `@bernt-matthias <https://github.com/bernt-matthias>`_ (`#15 <https://github.com/aCLImatise/CliHelpParser/pull/15>`_). However this information is not yet used in the converters.

1.0.1 (2020-08-22)
------------------
* Enforce timeouts for all executors, including Docker
* Restructure the executors such that the parameters are all set in the constructor, not in the ``execute()`` call

1.0.0 (2020-08-19)
------------------
Since the creation of executors is actually a breaking change, this is now a new major version

User-Facing
***********
* Support executables that have a file extension e.g. samtools.pl
* Refactor the command execution code into a new ``Executor`` class, and add a docker executor, allowing you to aCLImatise
  executables in a Docker image
* Fix for usage parsing when usage is in the middle of the line

Internal
********
* Run CI on pull requests
* Remove ``cwlgen`` as a dependency, thanks to `@illusional <https://github.com/illusional>`_ (`#26 <https://github.com/aCLImatise/CliHelpParser/pull/26>`_)
* Make ``infer_type`` return ``None`` if it can't determine a type, allowing better handling behaviour. Thanks to `@bernt-matthias <https://github.com/bernt-matthias>`_ (`#25 <https://github.com/aCLImatise/CliHelpParser/pull/25>`_)

0.2.2 (2020-07-22)
------------------
* Add support for Python 3.6 again
* Parse positionals by default from the CLI
* Fix bug involving name generation using different-length strings
* Add ``samtools bedcov`` test case
* Add a ``get_subclasses`` method for WrapperGenerator

0.2.1 (2020-07-04)
------------------
* Add automatic railroad diagram generation for grammar
* Add names to many of the parser elements to facilitate diagram generations
* Add genomethreader test

0.2.0 (2020-05-25)
------------------
Features
********
* Add ``parameter_meta`` (parameter documentation) generation back into WDL definitions
* Add :py:meth:`acclimatise.model.Command.depth`, and :py:attribute:`acclimatise.model.Command.parent` to :py:class:`acclimatise.model.Command` to facilitate the traversal of the command tree
* Add ``dinosaur`` and ``mauveAligner`` as test cases in ``test/test_data``
* Convert tests into a series of test case objects that can be used to parameterize each test function
* Add the option to parallelize tests using pytest-parallel
* Better conversion of symbols to variable names, for example "/" is now "slash" rather than "solidus"
* Add logging to the high level functions like ``explore_command``, using the ``acclimatise`` logger. This should make tracking errors and progress a tad easier.
* By default, re-use the best help command from the parent on the child. For example if we determine that ``samtools --help`` is the most accurate help command for ``samtools``, then we use ``samtools sort --help`` without having to test out every possible flag here
* Add ``generated_using`` field to the ``Command`` class, which tracks the flag used to generate it

Changes
*******
* Set the default command depth to 3
* ``aCLImatise`` now only supports Python >= 3.7.5, due to `this bug <https://bugs.python.org/issue37424>`_

Fixes
*****
* Avoid variable naming collisions using a generator-based iteration method in ``acclimatise.name_generation.generate_names``
* Keep a global ``spacy`` instance to minimize memory footprint. This is available in :py:module:`acclimatise.nlp`
* Fix infinite loops in explore, e.g. tools like ``dinosaur`` and ``mauve`` by adding more advanced subcommand detection in ``acclimatise.is_subcommand``
* Make cmd optional for validators
* Always run commands in a pseudo-TTY so that commands like ``samtools`` will output help
* Various other fixes

0.1.5 (2020-05-18)
------------------
* Bugfix for when we have no help text
* Add a test for a program that we know fails

0.1.4 (2020-05-18)
------------------
* Choose best command using length of help text, if everything else is equal

0.1.3 (2020-05-15)
------------------
* ``Command`` types now contain a ``help_text`` field which records the string that was used to generate them. This should enable efficient re-parsing, and can also be displayed downstream by BaseCamp
* Rewrite tests into a parametrized, consolidated end-to-end test
* Fix "OPTIONS" being considered a positional argument, when really it's a placeholder for flags
* Remove positional arguments that precede the main command, so ``dotnet Pisces.dll`` will be removed from the entire command

0.1.2 (2020-05-15)
------------------
* Generating YAML output now produces one file for each subcommand, to match other converters

0.1.1 (2020-05-13)
------------------
* Make ``explore -o`` flag default to current working directory, for simplicity
* Updated the readme
* Add installation instructions

0.1.0 (2020-05-13)
------------------
* Fix the doubled variable names like ``bytesBytes``
* Smarter POS-based algorithm for generating names from descriptions
* Automatically choose a description based name when we have only short named flags like ``-n``
* Add changelog
* Add comprehensive testing for CWL and WDL generation
* Fix for variable names with symbols in them
* Use regex library for faster and more concise regex
