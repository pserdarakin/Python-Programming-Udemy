All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Description: CERates : Currency Exchange Rates
        =================================
        
        |build|  |repo|  |format|  |grade|  |coverage|
        
        .. |build| image:: https://travis-ci.org/aksbuzz/cerates.svg?branch=master
            :target: https://travis-ci.org/aksbuzz/cerates
        
        .. |repo| image:: https://img.shields.io/badge/source-GitHub-blue.svg?maxAge=3600
           :target: https://github.com/aksbuzz/cerates
        
        
        .. |format| image:: https://img.shields.io/pypi/format/cerates.svg?maxAge=3600
           :target: https://pypi.python.org/pypi/cerates
        
        .. |grade| image:: https://img.shields.io/codacy/grade/9b8c7da6887c4195b9e960cb04b59a91/master.svg?maxAge=3600
           :target: https://www.codacy.com/app/aksbuzz/cerates/dashboard
        
        .. |coverage| image:: https://img.shields.io/codacy/coverage/9b8c7da6887c4195b9e960cb04b59a91/master.svg?maxAge=3600
           :target: https://www.codacy.com/app/aksbuzz/cerates/files
        
        **What is it?**
        ****************
        
        CERates or Currency Exchange Rates is a foreign exchange rates and currency conversion tool. It provides a nice and quick interface for your python application.
        
        CERates requires python3 (3.3 or up).
        
        You can use CERates in two ways :
        
        	* As a module for your python app.
        	* As a CLI app.
        
        
        **Features**
        ************
        
        * No API key required.
        * Uses Fixer.io for fetching the data.
        * Provides a CLI app for quickly finding exchange rates.
        
        
        **Install**
        ***********
        
        Using PIP:
        
        ..code :: 
        	
        	$ pip3 install cerates
        
        
        Build from source
        
        .. code ::
        	
        	$ git clone https://github.com/aksbuzz/cerates.git
        
        	$ cd cerates
        
        	$ make
        
        
        **Usage**
        *********
        
        *As a Module*
        ^^^^^^^^^^^^^
        
        First Create an instance object.
        
        .. code :: python
        	
        	>>> import cerates
        
        	>>> cer = cerates.Cerates()
        
        To find the latest exchange
        
        .. code :: python
        
        	>>> cer.get_rates()
        
        You can provide external parameters.
        
        .. code :: python
        
        	>>> cer.get_rates(date="2009-02-25") # Get the rate for provided date.
        
        	>>> cer.get_rates(base="USD") # Get rates for provided base currency.
        
        	>>> cer.get_rates(symbols=["USD", "INR"]) # Get rates for only these symbols.
        
        *As a CLI app*
        ^^^^^^^^^^^^^^
        
        Todo...
        
        **Examples**
        ************
        
        You can find example usage in the examples folder.
        
        
        **Todo**
        ********
        
        - Add Python 2 support
        - Add detailed documentation
        
        
Platform: UNKNOWN
