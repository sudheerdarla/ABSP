#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# -------------------- Find website URLs that begin with http:// or https://. ---------------------

urlText = '''The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

the regular expression composed & commented
could be easily tweaked for RFC compliance,
it was expressly modified to fit & satisfy
these test for an URL shortener:

  http://mathiasbynens.be/demo/url-regex

Notes on possible differences from a standard/generic validation:

- utf-8 char class take in consideration the full Unicode range
- TLDs have been made mandatory so single names like "localhost" fails
- protocols have been restricted to ftp, http and https only as requested

Changes:

- IP address dotted notation validation, range: 1.0.0.0 - 223.255.255.255
  first and last IP address of each class is considered invalid
  (since they are broadcast/network addresses)

- Added exclusion of private, reserved and/or local networks ranges

- Made starting path slash optional (http://example.com?foo=bar)

- Allow a dot (.) at the end of hostnames (http://example.com.)

Compressed one-line versions:'''




urlRegex = re.compile(r'''
	http[s]?                   	# for http or https
	://							# for ://
	(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
	''', re.VERBOSE)

urls = urlRegex.findall(urlText)

for i in range(len(urls)):
	urls[i] = urls[i].rstrip(')')

print(urls)