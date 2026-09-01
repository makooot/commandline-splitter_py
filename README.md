# commandline-splitter_py

> ⚠️ **Disclaimer: This is a learning-oriented project.**
> This repository is built strictly for personal learning and practicing Python library development. It is **not actively maintained for public production use**. Bug reports, feature requests, or Pull Requests may not be reviewed or addressed. Feel free to fork the repository for your own use under the MIT License.

Split the command line like bash.

## Installation

coming soon

## Quick Start

Here is a simple example of how to use the library:

```python
from commandline_splitter import splitter

splitter.splitter(r"""-d 'commandline splitter' -l mit commandline-splitter_py""")
# [
#     '-d',
#     'commandline splitter',
#     '-l',
#     'mit',
#     'commandline-splitter_py'
# ]
```

## Contributing

Please refer to CONTRIBUTING.md for details on how this repository handles issues, pull requests, and forks.

## License

MIT License
