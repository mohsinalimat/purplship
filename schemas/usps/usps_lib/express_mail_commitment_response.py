#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat May 29 15:46:57 2021 by generateDS.py version 2.38.6.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './usps_lib/express_mail_commitment_response.py')
#
# Command line arguments:
#   ./schemas/ExpressMailCommitmentResponse.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./usps_lib/express_mail_commitment_response.py" ./schemas/ExpressMailCommitmentResponse.xsd
#
# Current working directory (os.getcwd()):
#   usps
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class ExpressMailCommitmentResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, OriginZIP=None, OriginCity=None, OriginState=None, DestinationZIP=None, DestinationCity=None, DestinationState=None, Date=None, Time=None, EffectiveAcceptanceDate=None, Commitment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.OriginZIP = OriginZIP
        self.OriginZIP_nsprefix_ = None
        self.OriginCity = OriginCity
        self.OriginCity_nsprefix_ = None
        self.OriginState = OriginState
        self.OriginState_nsprefix_ = None
        self.DestinationZIP = DestinationZIP
        self.DestinationZIP_nsprefix_ = None
        self.DestinationCity = DestinationCity
        self.DestinationCity_nsprefix_ = None
        self.DestinationState = DestinationState
        self.DestinationState_nsprefix_ = None
        self.Date = Date
        self.Date_nsprefix_ = None
        self.Time = Time
        self.Time_nsprefix_ = None
        if isinstance(EffectiveAcceptanceDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(EffectiveAcceptanceDate, '%Y-%m-%d').date()
        else:
            initvalue_ = EffectiveAcceptanceDate
        self.EffectiveAcceptanceDate = initvalue_
        self.EffectiveAcceptanceDate_nsprefix_ = None
        if Commitment is None:
            self.Commitment = []
        else:
            self.Commitment = Commitment
        self.Commitment_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExpressMailCommitmentResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExpressMailCommitmentResponse.subclass:
            return ExpressMailCommitmentResponse.subclass(*args_, **kwargs_)
        else:
            return ExpressMailCommitmentResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_OriginZIP(self):
        return self.OriginZIP
    def set_OriginZIP(self, OriginZIP):
        self.OriginZIP = OriginZIP
    def get_OriginCity(self):
        return self.OriginCity
    def set_OriginCity(self, OriginCity):
        self.OriginCity = OriginCity
    def get_OriginState(self):
        return self.OriginState
    def set_OriginState(self, OriginState):
        self.OriginState = OriginState
    def get_DestinationZIP(self):
        return self.DestinationZIP
    def set_DestinationZIP(self, DestinationZIP):
        self.DestinationZIP = DestinationZIP
    def get_DestinationCity(self):
        return self.DestinationCity
    def set_DestinationCity(self, DestinationCity):
        self.DestinationCity = DestinationCity
    def get_DestinationState(self):
        return self.DestinationState
    def set_DestinationState(self, DestinationState):
        self.DestinationState = DestinationState
    def get_Date(self):
        return self.Date
    def set_Date(self, Date):
        self.Date = Date
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def get_EffectiveAcceptanceDate(self):
        return self.EffectiveAcceptanceDate
    def set_EffectiveAcceptanceDate(self, EffectiveAcceptanceDate):
        self.EffectiveAcceptanceDate = EffectiveAcceptanceDate
    def get_Commitment(self):
        return self.Commitment
    def set_Commitment(self, Commitment):
        self.Commitment = Commitment
    def add_Commitment(self, value):
        self.Commitment.append(value)
    def insert_Commitment_at(self, index, value):
        self.Commitment.insert(index, value)
    def replace_Commitment_at(self, index, value):
        self.Commitment[index] = value
    def hasContent_(self):
        if (
            self.OriginZIP is not None or
            self.OriginCity is not None or
            self.OriginState is not None or
            self.DestinationZIP is not None or
            self.DestinationCity is not None or
            self.DestinationState is not None or
            self.Date is not None or
            self.Time is not None or
            self.EffectiveAcceptanceDate is not None or
            self.Commitment
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExpressMailCommitmentResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExpressMailCommitmentResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExpressMailCommitmentResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExpressMailCommitmentResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ExpressMailCommitmentResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExpressMailCommitmentResponse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExpressMailCommitmentResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.OriginZIP is not None:
            namespaceprefix_ = self.OriginZIP_nsprefix_ + ':' if (UseCapturedNS_ and self.OriginZIP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOriginZIP>%s</%sOriginZIP>%s' % (namespaceprefix_ , self.gds_format_integer(self.OriginZIP, input_name='OriginZIP'), namespaceprefix_ , eol_))
        if self.OriginCity is not None:
            namespaceprefix_ = self.OriginCity_nsprefix_ + ':' if (UseCapturedNS_ and self.OriginCity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOriginCity>%s</%sOriginCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OriginCity), input_name='OriginCity')), namespaceprefix_ , eol_))
        if self.OriginState is not None:
            namespaceprefix_ = self.OriginState_nsprefix_ + ':' if (UseCapturedNS_ and self.OriginState_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOriginState>%s</%sOriginState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OriginState), input_name='OriginState')), namespaceprefix_ , eol_))
        if self.DestinationZIP is not None:
            namespaceprefix_ = self.DestinationZIP_nsprefix_ + ':' if (UseCapturedNS_ and self.DestinationZIP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDestinationZIP>%s</%sDestinationZIP>%s' % (namespaceprefix_ , self.gds_format_integer(self.DestinationZIP, input_name='DestinationZIP'), namespaceprefix_ , eol_))
        if self.DestinationCity is not None:
            namespaceprefix_ = self.DestinationCity_nsprefix_ + ':' if (UseCapturedNS_ and self.DestinationCity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDestinationCity>%s</%sDestinationCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DestinationCity), input_name='DestinationCity')), namespaceprefix_ , eol_))
        if self.DestinationState is not None:
            namespaceprefix_ = self.DestinationState_nsprefix_ + ':' if (UseCapturedNS_ and self.DestinationState_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDestinationState>%s</%sDestinationState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DestinationState), input_name='DestinationState')), namespaceprefix_ , eol_))
        if self.Date is not None:
            namespaceprefix_ = self.Date_nsprefix_ + ':' if (UseCapturedNS_ and self.Date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDate>%s</%sDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Date), input_name='Date')), namespaceprefix_ , eol_))
        if self.Time is not None:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTime>%s</%sTime>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Time), input_name='Time')), namespaceprefix_ , eol_))
        if self.EffectiveAcceptanceDate is not None:
            namespaceprefix_ = self.EffectiveAcceptanceDate_nsprefix_ + ':' if (UseCapturedNS_ and self.EffectiveAcceptanceDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEffectiveAcceptanceDate>%s</%sEffectiveAcceptanceDate>%s' % (namespaceprefix_ , self.gds_format_date(self.EffectiveAcceptanceDate, input_name='EffectiveAcceptanceDate'), namespaceprefix_ , eol_))
        for Commitment_ in self.Commitment:
            namespaceprefix_ = self.Commitment_nsprefix_ + ':' if (UseCapturedNS_ and self.Commitment_nsprefix_) else ''
            Commitment_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Commitment', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OriginZIP' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'OriginZIP')
            ival_ = self.gds_validate_integer(ival_, node, 'OriginZIP')
            self.OriginZIP = ival_
            self.OriginZIP_nsprefix_ = child_.prefix
        elif nodeName_ == 'OriginCity':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OriginCity')
            value_ = self.gds_validate_string(value_, node, 'OriginCity')
            self.OriginCity = value_
            self.OriginCity_nsprefix_ = child_.prefix
        elif nodeName_ == 'OriginState':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OriginState')
            value_ = self.gds_validate_string(value_, node, 'OriginState')
            self.OriginState = value_
            self.OriginState_nsprefix_ = child_.prefix
        elif nodeName_ == 'DestinationZIP' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'DestinationZIP')
            ival_ = self.gds_validate_integer(ival_, node, 'DestinationZIP')
            self.DestinationZIP = ival_
            self.DestinationZIP_nsprefix_ = child_.prefix
        elif nodeName_ == 'DestinationCity':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DestinationCity')
            value_ = self.gds_validate_string(value_, node, 'DestinationCity')
            self.DestinationCity = value_
            self.DestinationCity_nsprefix_ = child_.prefix
        elif nodeName_ == 'DestinationState':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DestinationState')
            value_ = self.gds_validate_string(value_, node, 'DestinationState')
            self.DestinationState = value_
            self.DestinationState_nsprefix_ = child_.prefix
        elif nodeName_ == 'Date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Date')
            value_ = self.gds_validate_string(value_, node, 'Date')
            self.Date = value_
            self.Date_nsprefix_ = child_.prefix
        elif nodeName_ == 'Time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Time')
            value_ = self.gds_validate_string(value_, node, 'Time')
            self.Time = value_
            self.Time_nsprefix_ = child_.prefix
        elif nodeName_ == 'EffectiveAcceptanceDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.EffectiveAcceptanceDate = dval_
            self.EffectiveAcceptanceDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'Commitment':
            obj_ = CommitmentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Commitment.append(obj_)
            obj_.original_tagname_ = 'Commitment'
# end class ExpressMailCommitmentResponse


class CommitmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CommitmentName=None, CommitmentTime=None, CommitmentSequence=None, Location=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CommitmentName = CommitmentName
        self.CommitmentName_nsprefix_ = None
        self.CommitmentTime = CommitmentTime
        self.CommitmentTime_nsprefix_ = None
        self.CommitmentSequence = CommitmentSequence
        self.CommitmentSequence_nsprefix_ = None
        if Location is None:
            self.Location = []
        else:
            self.Location = Location
        self.Location_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CommitmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CommitmentType.subclass:
            return CommitmentType.subclass(*args_, **kwargs_)
        else:
            return CommitmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CommitmentName(self):
        return self.CommitmentName
    def set_CommitmentName(self, CommitmentName):
        self.CommitmentName = CommitmentName
    def get_CommitmentTime(self):
        return self.CommitmentTime
    def set_CommitmentTime(self, CommitmentTime):
        self.CommitmentTime = CommitmentTime
    def get_CommitmentSequence(self):
        return self.CommitmentSequence
    def set_CommitmentSequence(self, CommitmentSequence):
        self.CommitmentSequence = CommitmentSequence
    def get_Location(self):
        return self.Location
    def set_Location(self, Location):
        self.Location = Location
    def add_Location(self, value):
        self.Location.append(value)
    def insert_Location_at(self, index, value):
        self.Location.insert(index, value)
    def replace_Location_at(self, index, value):
        self.Location[index] = value
    def hasContent_(self):
        if (
            self.CommitmentName is not None or
            self.CommitmentTime is not None or
            self.CommitmentSequence is not None or
            self.Location
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CommitmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CommitmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CommitmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CommitmentType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CommitmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CommitmentType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CommitmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CommitmentName is not None:
            namespaceprefix_ = self.CommitmentName_nsprefix_ + ':' if (UseCapturedNS_ and self.CommitmentName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommitmentName>%s</%sCommitmentName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CommitmentName), input_name='CommitmentName')), namespaceprefix_ , eol_))
        if self.CommitmentTime is not None:
            namespaceprefix_ = self.CommitmentTime_nsprefix_ + ':' if (UseCapturedNS_ and self.CommitmentTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommitmentTime>%s</%sCommitmentTime>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CommitmentTime), input_name='CommitmentTime')), namespaceprefix_ , eol_))
        if self.CommitmentSequence is not None:
            namespaceprefix_ = self.CommitmentSequence_nsprefix_ + ':' if (UseCapturedNS_ and self.CommitmentSequence_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommitmentSequence>%s</%sCommitmentSequence>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CommitmentSequence), input_name='CommitmentSequence')), namespaceprefix_ , eol_))
        for Location_ in self.Location:
            namespaceprefix_ = self.Location_nsprefix_ + ':' if (UseCapturedNS_ and self.Location_nsprefix_) else ''
            Location_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Location', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CommitmentName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CommitmentName')
            value_ = self.gds_validate_string(value_, node, 'CommitmentName')
            self.CommitmentName = value_
            self.CommitmentName_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommitmentTime':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CommitmentTime')
            value_ = self.gds_validate_string(value_, node, 'CommitmentTime')
            self.CommitmentTime = value_
            self.CommitmentTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommitmentSequence':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CommitmentSequence')
            value_ = self.gds_validate_string(value_, node, 'CommitmentSequence')
            self.CommitmentSequence = value_
            self.CommitmentSequence_nsprefix_ = child_.prefix
        elif nodeName_ == 'Location':
            obj_ = LocationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Location.append(obj_)
            obj_.original_tagname_ = 'Location'
# end class CommitmentType


class LocationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ScheduledDeliveryDate=None, CutOff=None, Facility=None, Street=None, City=None, State=None, Zip=None, IsGuaranteed=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(ScheduledDeliveryDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(ScheduledDeliveryDate, '%Y-%m-%d').date()
        else:
            initvalue_ = ScheduledDeliveryDate
        self.ScheduledDeliveryDate = initvalue_
        self.ScheduledDeliveryDate_nsprefix_ = None
        self.CutOff = CutOff
        self.CutOff_nsprefix_ = None
        self.Facility = Facility
        self.Facility_nsprefix_ = None
        self.Street = Street
        self.Street_nsprefix_ = None
        self.City = City
        self.City_nsprefix_ = None
        self.State = State
        self.State_nsprefix_ = None
        self.Zip = Zip
        self.Zip_nsprefix_ = None
        self.IsGuaranteed = IsGuaranteed
        self.IsGuaranteed_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LocationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LocationType.subclass:
            return LocationType.subclass(*args_, **kwargs_)
        else:
            return LocationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ScheduledDeliveryDate(self):
        return self.ScheduledDeliveryDate
    def set_ScheduledDeliveryDate(self, ScheduledDeliveryDate):
        self.ScheduledDeliveryDate = ScheduledDeliveryDate
    def get_CutOff(self):
        return self.CutOff
    def set_CutOff(self, CutOff):
        self.CutOff = CutOff
    def get_Facility(self):
        return self.Facility
    def set_Facility(self, Facility):
        self.Facility = Facility
    def get_Street(self):
        return self.Street
    def set_Street(self, Street):
        self.Street = Street
    def get_City(self):
        return self.City
    def set_City(self, City):
        self.City = City
    def get_State(self):
        return self.State
    def set_State(self, State):
        self.State = State
    def get_Zip(self):
        return self.Zip
    def set_Zip(self, Zip):
        self.Zip = Zip
    def get_IsGuaranteed(self):
        return self.IsGuaranteed
    def set_IsGuaranteed(self, IsGuaranteed):
        self.IsGuaranteed = IsGuaranteed
    def hasContent_(self):
        if (
            self.ScheduledDeliveryDate is not None or
            self.CutOff is not None or
            self.Facility is not None or
            self.Street is not None or
            self.City is not None or
            self.State is not None or
            self.Zip is not None or
            self.IsGuaranteed is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LocationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LocationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LocationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LocationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LocationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LocationType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LocationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ScheduledDeliveryDate is not None:
            namespaceprefix_ = self.ScheduledDeliveryDate_nsprefix_ + ':' if (UseCapturedNS_ and self.ScheduledDeliveryDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScheduledDeliveryDate>%s</%sScheduledDeliveryDate>%s' % (namespaceprefix_ , self.gds_format_date(self.ScheduledDeliveryDate, input_name='ScheduledDeliveryDate'), namespaceprefix_ , eol_))
        if self.CutOff is not None:
            namespaceprefix_ = self.CutOff_nsprefix_ + ':' if (UseCapturedNS_ and self.CutOff_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCutOff>%s</%sCutOff>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CutOff), input_name='CutOff')), namespaceprefix_ , eol_))
        if self.Facility is not None:
            namespaceprefix_ = self.Facility_nsprefix_ + ':' if (UseCapturedNS_ and self.Facility_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFacility>%s</%sFacility>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Facility), input_name='Facility')), namespaceprefix_ , eol_))
        if self.Street is not None:
            namespaceprefix_ = self.Street_nsprefix_ + ':' if (UseCapturedNS_ and self.Street_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStreet>%s</%sStreet>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Street), input_name='Street')), namespaceprefix_ , eol_))
        if self.City is not None:
            namespaceprefix_ = self.City_nsprefix_ + ':' if (UseCapturedNS_ and self.City_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCity>%s</%sCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.City), input_name='City')), namespaceprefix_ , eol_))
        if self.State is not None:
            namespaceprefix_ = self.State_nsprefix_ + ':' if (UseCapturedNS_ and self.State_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sState>%s</%sState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.State), input_name='State')), namespaceprefix_ , eol_))
        if self.Zip is not None:
            namespaceprefix_ = self.Zip_nsprefix_ + ':' if (UseCapturedNS_ and self.Zip_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sZip>%s</%sZip>%s' % (namespaceprefix_ , self.gds_format_integer(self.Zip, input_name='Zip'), namespaceprefix_ , eol_))
        if self.IsGuaranteed is not None:
            namespaceprefix_ = self.IsGuaranteed_nsprefix_ + ':' if (UseCapturedNS_ and self.IsGuaranteed_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIsGuaranteed>%s</%sIsGuaranteed>%s' % (namespaceprefix_ , self.gds_format_integer(self.IsGuaranteed, input_name='IsGuaranteed'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ScheduledDeliveryDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.ScheduledDeliveryDate = dval_
            self.ScheduledDeliveryDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'CutOff':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CutOff')
            value_ = self.gds_validate_string(value_, node, 'CutOff')
            self.CutOff = value_
            self.CutOff_nsprefix_ = child_.prefix
        elif nodeName_ == 'Facility':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Facility')
            value_ = self.gds_validate_string(value_, node, 'Facility')
            self.Facility = value_
            self.Facility_nsprefix_ = child_.prefix
        elif nodeName_ == 'Street':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Street')
            value_ = self.gds_validate_string(value_, node, 'Street')
            self.Street = value_
            self.Street_nsprefix_ = child_.prefix
        elif nodeName_ == 'City':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'City')
            value_ = self.gds_validate_string(value_, node, 'City')
            self.City = value_
            self.City_nsprefix_ = child_.prefix
        elif nodeName_ == 'State':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'State')
            value_ = self.gds_validate_string(value_, node, 'State')
            self.State = value_
            self.State_nsprefix_ = child_.prefix
        elif nodeName_ == 'Zip' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Zip')
            ival_ = self.gds_validate_integer(ival_, node, 'Zip')
            self.Zip = ival_
            self.Zip_nsprefix_ = child_.prefix
        elif nodeName_ == 'IsGuaranteed' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'IsGuaranteed')
            ival_ = self.gds_validate_integer(ival_, node, 'IsGuaranteed')
            self.IsGuaranteed = ival_
            self.IsGuaranteed_nsprefix_ = child_.prefix
# end class LocationType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExpressMailCommitmentResponse'
        rootClass = ExpressMailCommitmentResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExpressMailCommitmentResponse'
        rootClass = ExpressMailCommitmentResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExpressMailCommitmentResponse'
        rootClass = ExpressMailCommitmentResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExpressMailCommitmentResponse'
        rootClass = ExpressMailCommitmentResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from express_mail_commitment_response import *\n\n')
        sys.stdout.write('import express_mail_commitment_response as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {}

__all__ = [
    "CommitmentType",
    "ExpressMailCommitmentResponse",
    "LocationType"
]
