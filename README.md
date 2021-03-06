# Anonfiles.com Unofficial Python API

This unofficial Python API was created to make uploading and downloading files from Anonfile.com simple, and effective for programming in Python. The goal of the project is to create an intuitive library for anonymous file sharing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3 is required to run this application, other than that there are no prerequisites for the project, as the dependencies are included in the repo along with a virtual environment.

### Installing

To install the library, is as simple as cloning the repo and then importing the module.

Simply clone the repository.

```
git clone https://github.com/nstrydom2/anonfile-api.git
```

Or, install the library via Pip.

```
pip install anonfile
```

And have fun!

```
from anonfile.anonfile import AnonFile

anon = AnonFile('api_key')
status, file_url = anon.upload_file('/home/guest/jims_paperwork.doc')
```

## Usage

Just import the module, and then instantiate the AnonFile() object. Finally, start uploading.

```
from anonfile.anonfile import AnonFile

anon = AnonFile('api_key')
status, file_url = anon.upload_file('/home/guest/jims_paperwork.doc')

anon.download_file(file_url)
```

And voilà, pain free anonymous file sharing. I am also working towards proxy support. If you want some info on the returning JSON object(its going to be the "file" object). Visit [Anonfiles.com](https://anonfiles.com/docs/api). However, the current version just returns the url instead of the full "file" JSON object.

## Built With

* [Requests](http://docs.python-requests.org/en/master/) - Http for Humans
* [Anonfiles.com](https://anonfiles.com/docs/api) - AnonFiles.com REST API

## Versioning

For the versions available, see the [tags on this repository](https://github.com/nstrydom2/anonfile-api/tags). 

## Authors

* **Nicholas Strydom** - nstrydom@gmail.com - [nstrydom2](https://github.com/nstrydom2)

See also the list of [contributors](https://github.com/nstrydom2/anonfile-api/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Joseph Marie Jacquard
* Charles Babbage
* Ada Lovelace
* My Dad
* Hat tip to anyone whose code was used
* Inspiration
* etc

